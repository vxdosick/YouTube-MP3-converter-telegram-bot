# Imports
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from telegram import Update
from bot.bot import app as tg_app, bot
from ngrok import ngrok
import logging, asyncio

# Utils
import os
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram bot initialization
async def init_telegram():
    await bot.initialize()
    await tg_app.initialize()

async def setup_ngrok_and_webhook():
    authtoken = os.getenv("NGROK_AUTHTOKEN")

    if not authtoken:
        logger.warning("NGROK_AUTHTOKEN not found!")
        return
    
    try:
        listener = await asyncio.to_thread(
            ngrok.forward,
            addr=8000,
            authtoken=authtoken,
        )

        public_url = listener.url().rstrip("/")
        logger.info(f"ngrok tunnel created → {public_url}")

        webhook_url = f"{public_url}/tg-webhook"

        # Устанавливаем webhook
        success = await bot.set_webhook(url=webhook_url)
        
        if success:
            logger.info(f"Webhook set successfully → {webhook_url}")
        else:
            logger.error("Failed to set webhook")

    except Exception as e:
        logger.exception("Error while setting up ngrok", exc_info=e)

# Lifespan
@asynccontextmanager
async def lifespan(server: FastAPI):
    await init_telegram()
    yield

# FastAPI instance
app = FastAPI(lifespan=lifespan)

# Telegram webhook endpoint
@app.post("/tg-webhook")
async def telegram_webhook(request: Request):
    payload = await request.json()
    update = Update.de_json(payload, bot)
    await tg_app.process_update(update)
    return {"ok": True}