import os
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

    # 1. زر شفاف (Inline Button) يفتح المتجر كتطبيق مصغر داخل تليجرام
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

    # 2. زر ثابت أسفل الشاشة بجانب خانة الكتابة (Menu Button / Keyboard Button)
    reply_keyboard = [
        [
            KeyboardButton(
                text="📱 فتح متجر التطبيقات", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]

    # إرسال الرسالة مع الأزرار
    await update.message.reply_text(
        text=welcome_text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard),
        parse_mode="Markdown"
    )

    # إضافة الزر السفلي لخانة المحادثة
    await update.message.reply_text(
        text="يمكنك أيضاً فتح المتجر في أي وقت من الزر بالأسفل 👇",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("البوت يعمل بنجاح...")
    app.run_polling()

if __name__ == "__main__":
    main()
