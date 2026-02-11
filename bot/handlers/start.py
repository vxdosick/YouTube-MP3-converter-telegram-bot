from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatType

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != ChatType.PRIVATE:
        return
    
    await update.message.reply_text(
        "👋 Hello, I am a YouTube video to MP3 converter.\n"
        "🔊 Simply send me a link to the video, and I will send you only the audio in MP3 format.\n"
        "🍭 Enjoy using it.\n"
        )