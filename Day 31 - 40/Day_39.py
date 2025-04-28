# telegram bot ghf
import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, ApplicationBuilder, ContextTypes, filters
from telegram.request import HTTPXRequest

TOKEN = "7945188969:AAGqv31lZK0YaRjVTDqBXgTiCJyt1hyICnc"  # 🔥 Replace with your actual token

# Create the main folders and subdirectories
main_folders = ["ቁጥር", "ዜማ"]
WEEKDAY_ORDER = ["ዘዘወትር","ሰኑይ","ሠሉስ","ረቡዕ","ሐሙስ","አርብ","ቀዳሚት-ሰንበት","ሰንበተ-ከርስቲያን-ቅድስት"
]


for folder in main_folders:
    os.makedirs(folder, exist_ok=True)
    for day in WEEKDAY_ORDER:
        os.makedirs(os.path.join(folder, day), exist_ok=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["ዜማ", "ቁጥር"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)

import os

async def handle_text_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(text)

    # Initialize base folders
    base_folders = ["ቁጥር", "ዜማ"]

    # --- Handle 'Main Menu' ---
    if text == "Main Menu":
        context.user_data.clear()
        keyboard = [[folder] for folder in base_folders]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Select a main folder:", reply_markup=reply_markup)
        return

    # --- Handle 'Back' ---
    if text == "Back":
        if 'current_path' in context.user_data:
            current_path = context.user_data['current_path']
            parent_path = os.path.dirname(current_path)

            # If at top level, back to main menu
            if parent_path in ["", ".", None]:
                context.user_data.clear()
                keyboard = [[folder] for folder in base_folders]
                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
                await update.message.reply_text("Select a main folder:", reply_markup=reply_markup)
                return
            else:
                context.user_data['current_path'] = parent_path
                await list_directory(update, context, parent_path)
                return
        else:
            await update.message.reply_text("Already at the top.")
            return

    # --- Handle folder or file navigation ---
    if 'current_path' not in context.user_data:
        # Starting from main folder
        if text in base_folders:
            path = text
            context.user_data['current_path'] = path
            await list_directory(update, context, path)
        else:
            await update.message.reply_text("Please select a main folder first.")
    else:
        current_path = context.user_data['current_path']
        next_path = os.path.join(current_path, text)

        if os.path.isdir(next_path):
            # Go inside the folder
            context.user_data['current_path'] = next_path
            await list_directory(update, context, next_path)
        elif os.path.isfile(next_path):
            # Send the file
            await context.bot.send_document(chat_id=update.effective_chat.id, document=open(next_path, "rb"))
        else:
            await update.message.reply_text("Invalid option.")


async def list_directory(update: Update, context: ContextTypes.DEFAULT_TYPE, path):
    if not os.path.exists(path):
        await update.message.reply_text("Path does not exist.")
        return

    items = os.listdir(path)

    # --- If we are at the day level, sort by WEEKDAY_ORDER ---
    if path in ["ቁጥር", "ዜማ"]:
        items = sorted(items, key=lambda x: WEEKDAY_ORDER.index(x) if x in WEEKDAY_ORDER else 999)
    else:
        items.sort()  # Otherwise just normal alphabetical sorting inside subfolders

    if not items:
        await update.message.reply_text("Folder is empty.")
        return

    keyboard = [["Main Menu", "Back"]]
    for item in items:
        keyboard.append([item])
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(f"Contents of '{path}':", reply_markup=reply_markup)


async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'selected_day' not in context.user_data or 'selected_folder' not in context.user_data:
        await update.message.reply_text("Please select 'ቁጥር' or 'ዜማ' and then a day first.")
        return

    file = update.message.document or update.message.photo[-1]
    file_id = file.file_id
    file_name = file.file_name if hasattr(file, "file_name") else f"{random.randint(0, 99999)}.jpg"

    folder = context.user_data['selected_folder']
    day = context.user_data['selected_day']
    file_path = os.path.join(folder, day, file_name)

    # Download file using byte stream (faster)
    new_file = await context.bot.get_file(file_id)
    file_bytes = await new_file.download_as_bytearray()

    # Write the file fast
    with open(file_path, 'wb') as f:
        f.write(file_bytes)

    await update.message.reply_text(f"✅ File saved fast in '{folder}/{day}' as: {file_name}")

if __name__ == '__main__':
    request = HTTPXRequest(connect_timeout=300.0, read_timeout=300.0)

    app = ApplicationBuilder().token(TOKEN).request(request).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO, handle_file))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text_buttons))

    print("Bot is running...")
    app.run_polling()
