import os
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN", "8549143434:AAFqOee_MH3qFLF-AFy6dhs5uQlFPVTTCjY")
WEB_APP_URL = "https://aymnalsdran5-max.github.io/aemn2bot/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    welcome_text = (
        f"أهلاً بك يا **{user_name}** في متجر التطبيقات! 🛍️✨\n\n"
        f"يمكنك تصفح أحدث التطبيقات والخدمات مباشرة عبر المتجر أدناه.\n\n"
        f"نتمنى لك تجربة ممتعة! ❤️"
    )

    inline_keyboard = [
        [
            InlineKeyboardButton(
                "📱 فتح متجر التطبيقات", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ],
        [
            InlineKeyboardButton(
                "👨‍💻 التواصل مع الأدمن", 
                url="https://t.me/aemnalsdran"
            )
        ]
    ]

    reply_keyboard = [
        [
            KeyboardButton(
                text="📱 فتح متجر التطبيقات", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]

    await update.message.reply_text(
        text=welcome_text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard),
        parse_mode="Markdown"
    )

    await update.message.reply_text(
        text="يمكنك أيضاً فتح المتجر في أي وقت من الزر بالأسفل 👇",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    )

def main():
    while True:
        try:
            app = Application.builder().token(TOKEN).build()
            app.add_handler(CommandHandler("start", start))
            print("البوت يعمل الآن وجاهز للاستقبال...")
            app.run_polling(drop_pending_updates=True)
        except Exception as e:
            print(f"حدث خطأ، إعادة المحاولة خلال 5 ثوانٍ: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
