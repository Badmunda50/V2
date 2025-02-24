import time
from collections import defaultdict
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from AviaxMusic import app
from AviaxMusic.utils.admin_check import admin_check  # Admin check import

# Flood tracking
user_message_counts = defaultdict(lambda: {"count": 0, "timestamp": 0})
FLOOD_LIMIT = 5  # Messages allowed per 5 seconds
MUTE_DURATION = 60  # Mute time in seconds
antispam_enabled = True  # Default: Enabled
antispam_mode = "delete"  # Default mode: delete

@app.on_message(filters.command("antispam") & filters.group)
async def toggle_antispam(client: Client, message: Message):
    global antispam_enabled

    if not await admin_check(message):
        await message.reply_text("❌ You must be an admin to toggle Antispam!")
        return

    if len(message.command) > 1:
        arg = message.command[1].lower()
        if arg == "on":
            antispam_enabled = True
            await message.reply_text("✅ Antispam is now enabled!")
        elif arg == "off":
            antispam_enabled = False
            await message.reply_text("🚫 Antispam is now disabled!")
        else:
            await message.reply_text("⚙️ Use `/antispam on` or `/antispam off`")
    else:
        await message.reply_text("⚙️ Use `/antispam on` or `/antispam off`")

@app.on_message(filters.command("antispammode") & filters.group)
async def set_antispam_mode(client: Client, message: Message):
    global antispam_mode

    if not await admin_check(message):
        await message.reply_text("❌ You must be an admin to set Antispam mode!")
        return

    if len(message.command) > 1:
        mode = message.command[1].lower()
        if mode in ["mute", "kick", "delete"]:
            antispam_mode = mode
            await message.reply_text(f"✅ Antispam mode set to {mode}!")
        else:
            await message.reply_text("⚙️ Use `/antispammode mute`, `/antispammode kick`, or `/antispammode delete`")
    else:
        await message.reply_text("⚙️ Use `/antispammode mute`, `/antispammode kick`, or `/antispammode delete`")

@app.on_message(filters.text & filters.group)
async def antispam(client: Client, message: Message):
    if not antispam_enabled:
        return

    user_id = message.from_user.id
    chat_id = message.chat.id
    current_time = time.time()

    # Check last message time
    last_time = user_message_counts[user_id]["timestamp"]
    if current_time - last_time <= 5:
        user_message_counts[user_id]["count"] += 1
    else:
        user_message_counts[user_id]["count"] = 1

    user_message_counts[user_id]["timestamp"] = current_time

    # Apply action if limit exceeded
    if user_message_counts[user_id]["count"] > FLOOD_LIMIT:
        try:
            if antispam_mode == "mute":
                await client.restrict_chat_member(
                    chat_id,
                    user_id,
                    ChatPermissions(),
                    until_date=int(current_time + MUTE_DURATION),
                )
                await message.reply_text(f"🚨 @{message.from_user.username} muted for spamming!")
            elif antispam_mode == "kick":
                await client.kick_chat_member(chat_id, user_id)
                await message.reply_text(f"🚨 @{message.from_user.username} kicked for spamming!")
            elif antispam_mode == "delete":
                await message.delete()

            # Reset user count after action
            user_message_counts[user_id] = {"count": 0, "timestamp": current_time}
        except Exception as e:
            print(f"Failed to perform antispam action: {e}")
