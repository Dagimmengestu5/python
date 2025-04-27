# Start command
import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, ApplicationBuilder, ContextTypes, filters

TOKEN = "7945188969:AAGqv31lZK0YaRjVTDqBXgTiCJyt1hyICnc"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Add File", callback_data="add_file")],
        [InlineKeyboardButton("Saved Files", callback_data="saved_files")],
        [InlineKeyboardButton("Show File", callback_data="show_file")]
        # [InlineKeyboardButton("open File", callback_data="open_file")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)


# Callback query handler to show file details
async def show_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    files = os.listdir("downloads") if os.path.exists("downloads") else []
    if files:
        keyboard = [
            [InlineKeyboardButton(file, callback_data=f"file_{index}")]
            for index, file in enumerate(files)
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Select a file:", reply_markup=reply_markup)
    else:
        await query.edit_message_text("No files found.")


async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document or update.message.photo[-1]
    file_id = file.file_id
    file_name = file.file_name if hasattr(file, "file_name") else "photo.jpg"

    new_file = await context.bot.get_file(file_id)
    os.makedirs("downloads", exist_ok=True)
    file_path = os.path.join("downloads", file_name)

    await new_file.download_to_drive(file_path)
    await update.message.reply_text(f"File saved as: {file_name}")


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO, handle_file))
    app.add_handler(CallbackQueryHandler(show_file, pattern="^saved_files$"))
    app.add_handler(CallbackQueryHandler(show_file, pattern="^show_file$"))

    print("Bot is running...")
    app.run_polling()
