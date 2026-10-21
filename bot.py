import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# التوكن الخاص بك
TOKEN = os.environ.get("BOT_TOKEN", "8549143434:AAFqOee_MH3qFLF-AFy6dhs5uQlFPVTTCjY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    welcome_text = (
        f"أهلاً بك يا **{user_name}** في متجر التطبيقات! 🛍️✨\n\n"
        f"يمكنك تصفح أحدث التطبيقات والخدمات مباشرة عبر المتجر أدناه.\n\n"
        f"نتمنى لك تجربة ممتعة! ❤️"
    )

    keyboard = [
        [
            InlineKeyboardButton(
                "📱 فتح متجر التطبيقات", 
                url="https://aymnalsdran5-max.github.io/aemn2bot/"
            )
        ],
        [
            InlineKeyboardButton(
                "👨‍💻 التواصل مع الأدمن", 
                url="https://t.me/aemnalsdran"
            )
        ]
    ]

    await update.message.reply_text(
        text=welcome_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("البوت يعمل بنجاح...")
    app.run_polling()

if __name__ == "__main__":
    main()
