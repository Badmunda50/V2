from AviaxMusic import app
from pyrogram import client,filters
from config import LOG_GROUP_ID, OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests 


Button = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
      text=f"ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴀʀʟɪɴɢ ❣️",
      url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users",
      )
]
]
)
  
  

@app.on_message(filters.command("apod"))
async def advice(_, message):
    response = requests.get("https://api.safone.dev/astronomy")
    if response.status_code == 200:
        x = response.json()
        if x:
            date = x.get("date", "")
            img = x.get("imageUrl", "")
            explain = x.get("explanation", "")
            caption = f"Tᴏᴅᴀʏ's [{date}] ᴀsᴛʀᴏɴᴏᴍɪᴄᴀʟ ᴇᴠᴇɴᴛ:\n\n{explain}"
            await message.reply_photo(img, caption=caption, reply_markup=Button)
        else:
            await message.reply_text("ꜱᴏʀʀʏ ᴛᴏᴅᴀʏ ꜱᴇʀᴠᴇʀ ɪꜱ ᴅᴇᴀᴅ ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴛᴏᴍᴏʀʀᴏᴡ..")
    else:
        await message.reply_text("ꜱᴏʀʀʏ ᴛᴏᴅᴀʏ ꜱᴇʀᴠᴇʀ ɪꜱ ᴅᴇᴀᴅ ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴛᴏᴍᴏʀʀᴏᴡ..")
