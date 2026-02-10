from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatType

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != ChatType.PRIVATE:
        return
    
    await update.message.reply_text(
        "👋 Hi there! I am your personal AI assistant manager for CV matters 📄.\n"
        "🧑‍💼 Tell me about yourself and your professional experience right here in the chat,"
        "and I will create the perfect CV for you, tailored to your requirements and profession. 💼\n\n"
        )