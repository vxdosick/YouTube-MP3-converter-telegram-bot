from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatType
import asyncio

import os
from bot.utils.download_youtube_audio import download_youtube_audio
from bot.utils.rate_limit_function import is_rate_limited

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != ChatType.PRIVATE:
        return
    
    user_id = update.effective_user.id
    
    if is_rate_limited(user_id):
        await update.message.reply_text(
            "⏳ You are being rate limited.\n"
            "Please wait a few seconds before sending another message."
        )
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

    loop = asyncio.get_running_loop()
    mp3_path, result = await loop.run_in_executor(None, download_youtube_audio, url)

    if mp3_path is None:
        await update.message.reply_text(f"❌ {result}")
        return

    try:
        with open(mp3_path, "rb") as audio_file:
            await context.bot.send_audio(
                chat_id=update.effective_chat.id,
                audio=audio_file,
                title=result,
                filename=os.path.basename(mp3_path),
                caption=f"🎵 {result}\n\nDownload using vx's bot ❤️",
                read_timeout=90,
                write_timeout=90,
            )
        # await update.message.reply_text("🎉 Done!")
    except Exception as e:
        print(e)
        await update.message.reply_text(f"❌ Something went wrong")
    finally:
        try:
            if os.path.exists(mp3_path):
                os.remove(mp3_path)
        except:
            pass
