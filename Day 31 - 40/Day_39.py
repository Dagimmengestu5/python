from typing import final
from telegram import Update, ForceReplay
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = '7945188969:AAGqv31lZK0YaRjVTDqBXgTiCJyt1hyICnc'


# Save file handler
async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = None
    if update.message.document:
        file = await context.bot.get_file(update.message.document.file_id)
        filename = update.message.document.file_name
    elif update.message.photo:
        file = await context.bot.get_file(update.message.photo[-1].file_id)
        filename = f"{update.message.from_user.id}_photo.jpg"
    else:
        await update.message.reply_text("Send a file or image.")
        return

    file_path = os.path.join("downloads", filename)
    os.makedirs("downloads", exist_ok=True)
    await file.download_to_drive(file_path)

    await update.message.reply_text(f"File saved as {filename}")


# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a file or photo, and I'll save it.")


# Set up and run bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO, handle_file))

    print("Bot is running...")
    app.run_polling()
