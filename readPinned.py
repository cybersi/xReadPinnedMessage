from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import re
import asyncio

TOKEN = 'YOUR_TOKEN'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Read Pinned Bot is Active.')

async def check_address(update: Update, context: CallbackContext) -> None:
    # Determine if the update is from a channel post or a regular message
    message = update.channel_post if update.channel_post else update.message

    # Regular expression for the address format
    pattern = re.compile(r'\b[a-z0-9]{5}(?:-[a-z0-9]{5}){9}-[a-z0-9]{3}\b', re.IGNORECASE)
    
    # Searching text for the pattern
    if message.text:
        match = pattern.search(message.text)
        if match:
            # Prepare the image file ID or URL
            #image_file_id = 'YOUR_IMAGE_FILE_ID'
            image_url = 'https://i.imgur.com/RftQLCB.jpg'

            # Reply with the image
            await context.bot.send_photo(
                chat_id=message.chat_id,
                #photo=image_file_id,  
                photo=image_url,
                reply_to_message_id=message.message_id,
                #caption=f"Address recognized: {match.group()}"
            )

            # Reply with the text
            #await context.bot.send_message(chat_id=message.chat_id, text=f"Address recognized: {match.group()}")

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Adding handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_address))

    # Start the Bot and run it until it is stopped
    application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
