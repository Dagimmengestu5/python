import os
import re  # order of the number
import pytz
import random
from datetime import datetime, timezone

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, ApplicationBuilder, ContextTypes, filters
from telegram.request import HTTPXRequest

import gspread
from google.oauth2.service_account import Credentials

# === Telegram Token ===
TOKEN = "7945188969:AAGqv31lZK0YaRjVTDqBXgTiCJyt1hyICnc"  # Replace if needed

# === Google Sheets Setup ===

ethiopia = pytz.timezone("Africa/Addis_Ababa")
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("google_key.json", scopes=scope)
client = gspread.authorize(creds)
sheet = client.open("Telegram Users").sheet1
sheet.append_row(["Test ID", "Name", "Username", "Time"])
print("✅ Row added!")

# === Folder Structure ===
main_folders = ["መሰረተ ትምሕርት", "ቤተ ዜማ", "ሥርዓተ ቅዳሴ"]
WEEKDAY_ORDER = ["የዘወትር ፀሎት", "ውዳሴ ማርያም", "አንቀፀ ብርሃን", "መልክዐ ማርያም", "መልክዐ ኢየሰስ", "መዝሙረ ዳዊት"]

# Fixed structure for 'መሰረተ ትምሕርት'
os.makedirs("መሰረተ ትምሕርት", exist_ok=True)
for day in WEEKDAY_ORDER:
    os.makedirs(os.path.join("መሰረተ ትምሕርት", day), exist_ok=True)

# Dynamic structure for 'ቤተ ዜማ'
os.makedirs("ቤተ ዜማ", exist_ok=True)
os.makedirs("ሥርዓተ ቅዳሴ", exist_ok=True)
def get_sheet(sheet_name: str):
    try:
        creds = Credentials.from_service_account_file("google_key.json", scopes=scope)
        client = gspread.authorize(creds)
        return client.open("Telegram Users").worksheet(sheet_name)
    except Exception as e:
        print(f"❌ Google Sheets Error: {e}")
        return None

# === Handlers ===

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name
    username = user.username or "-"
    user_id = user.id



    timestamp = datetime.now(ethiopia).strftime('%Y-%m-%d %H:%M:%S')

    # timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')



    # Greet user
    await update.message.reply_text(f"ሰላም {name} 👋 እንኳን ወደ መካነ ሕይወት ሰ/ት/ቤት አብነት ትምህርት መማርያ ቦት በደህና መጡ! ")


    # Log to Google Sheet
    sheet = get_sheet("Sheet1")
    if sheet:
        try:
            sheet.append_row([str(user_id), name, username, timestamp])
        except Exception as e:
            print(f"❌ Failed to write user to sheet: {e}")

    # Show menu
    keyboard = [[folder] for folder in main_folders]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("እባክዎ ከስር ያለውን አማራች ይጠቀሙ፡", reply_markup=reply_markup)

async def handle_text_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    base_folders = main_folders
    print(text)


    if text == "Main Menu":
        context.user_data.clear()
        keyboard = [[folder] for folder in base_folders]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Select a main folder:", reply_markup=reply_markup)
        return

    if text == "Back":
        if 'current_path' in context.user_data:
            current_path = context.user_data['current_path']
            parent_path = os.path.dirname(current_path)
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

    # Navigate
    if 'current_path' not in context.user_data:
        if text in base_folders:
            path = text
            context.user_data['current_path'] = path
            await list_directory(update, context, path)
        else:
            await update.message.reply_text("Please select a main folder first.")
    else:
        current = context.user_data['current_path']
        next_path = os.path.join(current, text)
        if os.path.isdir(next_path):
            context.user_data['current_path'] = next_path
            await list_directory(update, context, next_path)
        elif os.path.isfile(next_path):
            # Send the file
            await context.bot.send_document(chat_id=update.effective_chat.id, document=open(next_path, "rb"))

            # Log download to Google Sheet
            try:
                user = update.effective_user
                username = user.username or "-"
                user_id = user.id

                # ethiopia = pytz.timezone("Africa/Addis_Ababa")
                timestamp = datetime.now(ethiopia).strftime('%Y-%m-%d %H:%M:%S')
                file_name = os.path.basename(next_path)
                folder_path = os.path.dirname(next_path)

                # Access the 2nd sheet by name
                download_sheet = client.open("Telegram Users").worksheet("Download Log")
                download_sheet.append_row([str(user_id), username, file_name, folder_path, timestamp])
            except Exception as e:
                print(f"❌ Failed to write download log: {e}")

        else:
            await update.message.reply_text("Invalid option.")



def natural_key(text):  # list number orderd
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', text)]

async def list_directory(update: Update , context: ContextTypes.DEFAULT_TYPE , path):
    if not os.path.exists(path):
        await update.message.reply_text("Path does not exist.")
        return

    items = os.listdir(path)

    if path == "መሰረተ ትምሕርት":
        items = sorted(items, key=lambda x: WEEKDAY_ORDER.index(x) if x in WEEKDAY_ORDER else 999)
    else:
        items.sort(key=natural_key)  # 🔥 FIXED HERE

    if not items:
        await update.message.reply_text("Folder is empty.")
        return

    keyboard = [["Main Menu", "Back"]]
    for item in items:
        keyboard.append([item])
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(f"Contents of '{path}':", reply_markup=reply_markup)


async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'current_path' not in context.user_data:
        await update.message.reply_text("Please select a folder first.")
        return

    file = update.message.document or update.message.photo[-1]
    file_id = file.file_id
    file_name = file.file_name if hasattr(file, "file_name") else f"{random.randint(0, 99999)}.jpg"
    current_path = context.user_data['current_path']
    file_path = os.path.join(current_path, file_name)

    await update.message.reply_text("⏫ Receiving file... Please wait...")

    new_file = await context.bot.get_file(file_id)
    await new_file.download_to_drive(custom_path=file_path)

    await update.message.reply_text(f"✅ File saved to '{file_path}'.")
# 7
# === Run App ===
if __name__ == '__main__':
    request = HTTPXRequest(connect_timeout=300.0, read_timeout=300.0)
    app = ApplicationBuilder().token(TOKEN).request(request).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO, handle_file))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text_buttons))

    print("Bot is running...")
    app.run_polling()
