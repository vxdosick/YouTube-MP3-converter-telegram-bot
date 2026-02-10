from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatType

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != ChatType.PRIVATE:
        return
    
    user_id = update.effective_user.id