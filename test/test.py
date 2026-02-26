import yt_dlp

URL = ""

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'output.%(ext)s',
    'quiet': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])