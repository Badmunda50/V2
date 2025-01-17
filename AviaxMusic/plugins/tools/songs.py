import os
import asyncio
import yt_dlp
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from youtube_search import YoutubeSearch
import requests
from AviaxMusic import app

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}

# Define the threshold for command spamming (e.g., 2 commands within 5 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5

# Path to the cookies file (make sure you have the cookies.txt file in the same directory or provide the full path)
COOKIES_FILE = 'cookies/example.txt'

# Quality options for songs
SONG_QUALITY_OPTIONS = {
    'low': 'worstaudio',
    'medium': 'bestaudio[ext=m4a]',
    'high': 'bestaudio'
}

# Quality options for videos
VIDEO_QUALITY_OPTIONS = {
    '144p': '144',
    '240p': '240',
    '360p': '360',
    '480p': '480',
    '720p': '720',
    '1080p': '1080',
    '1440p': '1440',
    '2160p': '2160',
}

async def send_quality_buttons(message: Message, query: str, type: str, thumbnail: str):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"Low Quality", callback_data=f"{type}_{query}_low"), 
         InlineKeyboardButton(f"Medium Quality", callback_data=f"{type}_{query}_medium"), 
         InlineKeyboardButton(f"High Quality", callback_data=f"{type}_{query}_high")]
    ])
    await message.reply_photo(photo=thumbnail, caption="Select quality:", reply_markup=keyboard)

async def send_video_quality_buttons(message: Message, query: str, thumbnail: str):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"144p", callback_data=f"video_{query}_144p"), 
         InlineKeyboardButton(f"240p", callback_data=f"video_{query}_240p"),
         InlineKeyboardButton(f"360p", callback_data=f"video_{query}_360p")],
        [InlineKeyboardButton(f"480p", callback_data=f"video_{query}_480p"), 
         InlineKeyboardButton(f"720p", callback_data=f"video_{query}_720p"),
         InlineKeyboardButton(f"1080p", callback_data=f"video_{query}_1080p")],
        [InlineKeyboardButton(f"1440p", callback_data=f"video_{query}_1440p"), 
         InlineKeyboardButton(f"2160p", callback_data=f"video_{query}_2160p")]
    ])
    await message.reply_photo(photo=thumbnail, caption="Select quality:", reply_markup=keyboard)

@app.on_message(filters.command("song"))
async def download_song(_, message: Message):
    user_id = message.from_user.id
    current_time = time()
    
    # Spam protection: Prevent multiple commands within a short time
    last_message_time = user_last_message_time.get(user_id, 0)
    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            hu = await message.reply_text(f"**{message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ**")
            await asyncio.sleep(3)
            await hu.delete()
            return
    else:
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time
    
    # Extract query from the message
    query = " ".join(message.command[1:])
    if not query:
        await message.reply("Please provide a song name or URL to search for.")
        return

    # Searching for the song using YouTubeSearch
    results = YoutubeSearch(query, max_results=1).to_dict()
    if not results:
        await message.reply("⚠️ No results found. Please make sure you typed the correct name.")
        return

    thumbnail = results[0]["thumbnails"][0]
    
    # Sending quality selection buttons
    await send_quality_buttons(message, query, 'song', thumbnail)

@app.on_message(filters.command("video"))
async def download_video(_, message: Message):
    user_id = message.from_user.id
    current_time = time()
    
    # Spam protection: Prevent multiple commands within a short time
    last_message_time = user_last_message_time.get(user_id, 0)
    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            hu = await message.reply_text(f"**{message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ**")
            await asyncio.sleep(3)
            await hu.delete()
            return
    else:
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time
    
    # Extract query from the message
    query = " ".join(message.command[1:])
    if not query:
        await message.reply("Please provide a video name or URL to search for.")
        return

    # Searching for the video using YouTubeSearch
    results = YoutubeSearch(query, max_results=1).to_dict()
    if not results:
        await message.reply("⚠️ No results found. Please make sure you typed the correct name.")
        return

    thumbnail = results[0]["thumbnails"][0]
    
    # Sending quality selection buttons
    await send_video_quality_buttons(message, query, thumbnail)

@app.on_callback_query(filters.regex(r"^(song|video)_(.+)_(low|medium|high|144p|240p|360p|480p|720p|1080p|1440p|2160p)$"))
async def callback_query_handler(client, query):
    type, query_text, quality = query.data.split("_")
    
    if type == "song":
        ydl_opts = {
            "format": SONG_QUALITY_OPTIONS[quality],  # Options to download audio in selected quality
            "noplaylist": True,  # Don't download playlists
            "quiet": True,
            "logtostderr": False,
            "cookiefile": COOKIES_FILE,  # Path to your cookies.txt file
        }
    else:
        ydl_opts = {
            "format": f"bestvideo[ext=mp4][height<={VIDEO_QUALITY_OPTIONS[quality]}]+bestaudio/best[ext=mp4][height<={VIDEO_QUALITY_OPTIONS[quality]}]",  # Options to download video in selected quality
            "noplaylist": True,  # Don't download playlists
            "quiet": True,
            "logtostderr": False,
            "cookiefile": COOKIES_FILE,  # Path to your cookies.txt file
        }

    try:
        # Searching for the song or video using YouTubeSearch
        m = await query.message.reply("🔄 **Searching...**")
        results = YoutubeSearch(query_text, max_results=1).to_dict()
        if not results:
            await m.edit("**⚠️ No results found. Please make sure you typed the correct name.**")
            return

        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        
        # Download thumbnail
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        views = results[0]["views"]
        channel_name = results[0]["channel"]

        # Now, download the audio or video using yt_dlp
        await m.edit("📥 **Downloading...**")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            file = ydl.prepare_filename(info_dict)
            ydl.download([link])

        # Parsing duration (in seconds)
        dur = sum(int(x) * 60 ** i for i, x in enumerate(reversed(duration.split(":"))))
        
        # Sending the audio or video to the user
        await m.edit("📤 **Uploading...**")
        if type == "song":
            await query.message.reply_audio(
                file,
                thumb=thumb_name,
                title=title,
                caption=f"{title}\nRequested by ➪ {query.from_user.mention}\nViews ➪ {views}\nChannel ➪ {channel_name}",
                duration=dur
            )
        else:
            await query.message.reply_video(
                file,
                thumb=thumb_name,
                caption=f"{title}\nRequested by ➪ {query.from_user.mention}\nViews ➪ {views}\nChannel ➪ {channel_name}",
                duration=dur
            )

        # Cleanup downloaded files
        os.remove(file)
        os.remove(thumb_name)
        await m.delete()

    except Exception as e:
        await m.edit("⚠️ **An error occurred!**")
        print(f"Error: {str(e)}")
