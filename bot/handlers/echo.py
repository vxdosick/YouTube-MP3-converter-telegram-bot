from telegram import Update, InputFile
from telegram.ext import ContextTypes
from telegram.constants import ChatType

import aiohttp
from io import BytesIO

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != ChatType.PRIVATE:
        return
    
    url = update.message.text.strip()

    if not url.startswith("http"):
        await update.message.reply_text(
            "❌ Seems like you sent me an invalid link.\n"
            "🔗 Please send me the link to the YouTube video you want to convert.\n"
            "📄 Or try the /help command.\n"
        )
        return
    
    await update.message.reply_text("⌛ Processing...")