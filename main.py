from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

keyboard = [
    ["❤️ Любовь", "😘 Поцелуй"],
    ["🤗 Обнимашки", "🔥 Секс"],
    ["💬 Серьёзно"]
]

markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Выбирай кнопку 👇",
        reply_markup=markup
    )

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я тебя люблю ❤️")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handler))

    app.run_polling()

if __name__ == "__main__":
    main()
