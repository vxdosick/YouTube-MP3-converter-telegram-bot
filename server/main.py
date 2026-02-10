# Imports
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from telegram import Update
from bot.bot import app as tg_app, bot
from dotenv import load_dotenv

# Telegram bot initialization
async def init_telegram():
    await bot.initialize()
    await tg_app.initialize()

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