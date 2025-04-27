# Start command
import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, ApplicationBuilder, ContextTypes, filters

TOKEN = "7945188969:AAGqv31lZK0YaRjVTDqBXgTiCJyt1hyICnc"

from telegram import ReplyKeyboardMarkup  # Add this import

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Add File", "Saved Files"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)


# New function to handle text button clicks
async def handle_text_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Add File":
        await update.message.reply_text("Please send the file to upload.")
    elif text == "Saved Files":
        files = os.listdir("saved_files") if os.path.exists("saved_files") else []
        if files:
            keyboard = [
                [file] for file in files
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            await update.message.reply_text("Select a file:", reply_markup=reply_markup)
        else:
            await update.message.reply_text("No files found.")
    elif text in os.listdir("saved_files"):
        file_path = os.path.join("saved_files", text)
        if os.path.exists(file_path):
            await context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_path, "rb"))
        else:
            await update.message.reply_text("File not found.")

# Callback query handler to show file details
async def show_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    files = os.listdir("saved_files") if os.path.exists("saved_files") else []
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
    file_name = file.file_name if hasattr(file, "file_name") else "image.jpg"

    new_file = await context.bot.get_file(file_id)
    os.makedirs("saved_files", exist_ok=True)
    file_path = os.path.join("saved_files", file_name)

    await new_file.download_to_drive(file_path)
    await update.message.reply_text(f"File saved in 'saved_files' directory as: {file_name}")


async def add_file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Add File button clicked! Please send the file to upload.")

# Handle when user clicks on a specific saved file
async def send_saved_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    files = os.listdir("saved_files")
    file_index = int(query.data.split("_")[1])  # Extract file index from callback data
    file_name = files[file_index]
    file_path = os.path.join("saved_files", file_name)

    if os.path.exists(file_path):
        await context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_path, "rb"))
    else:
        await query.edit_message_text("File not found.")


async def handle_text_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Add File":
        await update.message.reply_text("Please send the file you want to upload.")

    elif text == "Saved Files":
        files = os.listdir("saved_files") if os.path.exists("saved_files") else []
        if files:
            keyboard = [[file] for file in files]
            keyboard.append(["Back to Main Menu"])
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            await update.message.reply_text("Select a file:", reply_markup=reply_markup)
        else:
            keyboard = [["Back to Main Menu"]]
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            await update.message.reply_text("No files found.", reply_markup=reply_markup)

    elif os.path.exists(os.path.join("saved_files", text)):
        file_path = os.path.join("saved_files", text)
        await context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_path, "rb"))

    elif text == "Main Menu":
        keyboard = [["Add File", "Saved Files"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Choose an option:", reply_markup=reply_markup)

    else:
        await update.message.reply_text("Invalid option. Please use the buttons.")


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO, handle_file))
    app.add_handler(CallbackQueryHandler(show_file, pattern="^saved_files$"))
    # Add another CallbackQueryHandler
    app.add_handler(CallbackQueryHandler(send_saved_file, pattern="^file_"))
    app.add_handler(CallbackQueryHandler(add_file_handler, pattern="^add_file$"))
    # This will handle button clicks based on text
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text_buttons))
    app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO, handle_file))

    print("Bot is running...")
    app.run_polling()
