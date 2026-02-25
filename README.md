# YouTube to MP3 Telegram Bot
### Bot name: @yt_audiosound_converter_bot

A lightweight, personal Telegram bot that instantly converts YouTube videos (mostly music) into high-quality MP3 files and sends them back to you.

### What this bot does
You send a YouTube link → the bot downloads the best available audio track → converts it to MP3 → sends it back as an audio file playable directly in Telegram.
Main use-case: quick music extraction from YouTube videos without opening browsers, websites or third-party downloaders.

### Key Features
- Accepts **YouTube** links
- Downloads best available audio quality (usually 160–251 kbps Opus/WebM → converted to ~192 kbps MP3)
- File is sent as **Telegram Audio** track (with correct title, artist-friendly playback)
- Original downloaded file is **automatically deleted** after successful delivery (no disk clutter)
- Fast & minimalistic — no registration, no ads, no limits (for personal use)
- Runs locally or in Docker
- Uses modern stack with automatic ngrok tunnel + webhook setup during development
- Clean architecture: FastAPI backend + python-telegram-bot + yt-dlp + ffmpeg

### Bot Commands
- /start - 🚀 Welcome message & short instructions
- /convert - ♻️ Converter instructions
- /help - ⚙️ Show available commands

### Tech Stack
- Python 3.12
- python-telegram-bot
- FastAPI + Uvicorn
- yt-dlp
- ffmpeg (system dependency for audio conversion)
- ngrok
- Docker
- uv — modern dependency & virtual environment manager

### Useful commands
0. Environment creating
```bash
uv venv
```
1. Create .env file in root direction and write inside:
```bash
BOT_TOKEN=...
NGROK_AUTHTOKEN=...
```
2. Venv activation
```bash
source .venv/bin/activate
```
3. Install Dependencies
```bash
uv sync
```
4. Local bot run
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```
5. Creating Docker image
```bash
docker build -t yt-music-bot .
```
6. Start Docker container
```bash
docker run -d \
  --name ytbot \
  -p 8000:8000 \
  --env-file .env \
  -v "$(pwd)/outputs:/app/outputs" \
  --restart unless-stopped \
  yt-music-bot
```
7. Stop container
```bash
docker stop ytbot
```

### Important Notes
For personal use only — not intended for public distribution or commercial purposes
Respect YouTube ToS — this is a private convenience tool
Audio quality depends on what YouTube provides (usually very good for music videos)

Enjoy your music collection — hassle-free 🎧
Made with ❤️ in 2026