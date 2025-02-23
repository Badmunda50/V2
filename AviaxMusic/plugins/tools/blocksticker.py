import requests
from pyrogram import Client, filters
from pymongo import MongoClient
import os
from AviaxMusic import app
from config import MONGO_DB_URI

# MongoDB Setup
client = MongoClient(MONGO_DB_URI)
db = client["StickerBot"]  # Database name
collection = db["BlockedStickers"]  # Collection name

def load_blocked_stickers():
    """Load blocked stickers from MongoDB"""
    return [doc["sticker_pack_link"] for doc in collection.find({}, {"_id": 0, "sticker_pack_link": 1})]

def add_blocked_sticker(sticker_pack_link):
    """Add a sticker pack to MongoDB"""
    if not collection.find_one({"sticker_pack_link": sticker_pack_link}):
        collection.insert_one({"sticker_pack_link": sticker_pack_link})

blocked_sticker_packs = load_blocked_stickers()

@app.on_message(filters.sticker & filters.group)
async def check_sticker(client, message):
    try:
        sticker = message.sticker
        if not sticker or not sticker.set_name:
            return
        
        sticker_pack_link = f"https://t.me/addstickers/{sticker.set_name}"

        print(f"[DEBUG] Received sticker from pack: {sticker_pack_link}")

        if sticker_pack_link in blocked_sticker_packs:
            print(f"[DEBUG] Sticker is in blocklist. Deleting...")
            await message.delete()
            await message.reply(f"⚠️ {message.from_user.first_name} 18+ STICKER is not allowed.")
        else:
            print(f"[DEBUG] Sticker is not in blocklist.")

    except Exception as e:
        print(f"Error in check_sticker: {e}")

@app.on_message(filters.command("packlink") & filters.reply)
async def get_sticker_pack_link(client, message):
    if not message.reply_to_message or not message.reply_to_message.sticker:
        await message.reply("❌ Please reply to a sticker.")
        return

    sticker = message.reply_to_message.sticker
    sticker_pack_link = f"https://t.me/addstickers/{sticker.set_name}"
    await message.reply(f"🖼 Sticker Pack Link: {sticker_pack_link}")

@app.on_message(filters.command("addblock"))
async def add_blocked_sticker_pack(client, message):
    if len(message.command) < 2:
        await message.reply("❌ Usage: /addblock <sticker_pack_link>")
        return

    sticker_pack_link = message.command[1].strip()

    if not sticker_pack_link.startswith("https://t.me/addstickers/"):
        await message.reply("❌ Invalid sticker pack link!")
        return

    if sticker_pack_link in blocked_sticker_packs:
        await message.reply("✅ This sticker pack is already blocked.")
    else:
        add_blocked_sticker(sticker_pack_link)
        blocked_sticker_packs.append(sticker_pack_link)  # Update local cache
        await message.reply(f"🚫 Blocked Sticker Pack: {sticker_pack_link}")
