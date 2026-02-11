from telegram import Bot
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

# Utils
import os
from dotenv import load_dotenv

# Handlers
from bot.handlers.start import start
from bot.handlers.convert import convert
from bot.handlers.echo import echo
from bot.handlers.help import help
from bot.handlers.unknown import unknown

# Callbacks


# Define tokens, environment variables and other variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# TB App creating
bot = Bot(TOKEN)
app = Application.builder().token(TOKEN).build()

# Register handlers and callbacks
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("convert", convert))
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, echo))
app.add_handler(MessageHandler(filters.COMMAND, unknown))
# app.add_handler(CallbackQueryHandler(save_cv, pattern=r"^save_cv"))
# app.add_handler(CallbackQueryHandler(delete_cv, pattern=r"^delete_cv"))

# Run the bot by polling
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(app.run_polling())