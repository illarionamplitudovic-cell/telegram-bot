import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")

keyboard = [
    ["❤️ Любовь", "😘 Поцелуй"],
    ["🤗 Обнимашки", "🔥 Секс"],
    ["💬 Серьёзно"],
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Выбирай кнопку 👇", reply_markup=markup)

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").strip()

    if text == "❤️ Любовь":
        await update.message.reply_text("Я тебя люблю ❤️")
    elif text == "😘 Поцелуй":
        await update.message.reply_text("Чмок 😘")
    elif text == "🤗 Обнимашки":
        await update.message.reply_text("Обнял крепко 🤗")
    elif text == "🔥 Секс":
        await update.message.reply_text("🔥")
    elif text == "💬 Серьёзно":
        await update.message.reply_text("Слушаю внимательно.")
    else:
        await update.message.reply_text("Нажми кнопку или напиши /start")

def main():
    if not TOKEN:
        raise RuntimeError("TOKEN env var is missing")

    app = Application
