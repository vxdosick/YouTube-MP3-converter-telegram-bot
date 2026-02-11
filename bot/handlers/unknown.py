from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatType

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != ChatType.PRIVATE:
        return
    
    await update.message.reply_text(
        "❌ Unknown command.\n"
        "🔗 Please send me the link to the YouTube video you want to convert.\n"
        "📄 Or try the /help command.\n"
        )