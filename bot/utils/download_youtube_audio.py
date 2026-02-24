import os
import yt_dlp

def download_youtube_audio(url: str):

    os.makedirs("outputs", exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': 'outputs/%(title).200s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'keepvideo': False,
        'quiet': True,
        'no_warnings': True,
        'restrictfilenames': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            base = ydl.prepare_filename(info)
            mp3_path = os.path.splitext(base)[0] + '.mp3'

            title = info.get('title', 'Unknown Audio')

            if os.path.exists(mp3_path):
                return mp3_path, title
            return None, "Audio not found"

    except Exception as e:
        return None, f"Error yt-dlp: {str(e)[:150]}"