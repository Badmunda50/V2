import re
from AviaxMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from AviaxMusic.utils.admin_check import admin_check  # Importing admin check

# Regex for detecting links
LINK_REGEX = re.compile(r"https?://\S+|https?://(?:[a-zA-Z0-9-]+\.)?Indianotp\.com(?:/\S*)?|https?://(?:[a-zA-Z0-9-]+\.)?[^/]*\.com(?:/\S*)?")

# Dictionary to store antilink settings for different chats
antilink_enabled = {}

@app.on_message(filters.command("antilink") & filters.group)
async def toggle_antilink(client, message: Message):
    """Enable or disable antilink in the group."""
    chat_id = message.chat.id

    if not await admin_check(message):  # Using imported admin check
        await message.reply_text("❌ You must be an admin to toggle Antilink!")
        return

    if len(message.command) > 1:
        arg = message.command[1].lower()
        if arg == "on":
            antilink_enabled[chat_id] = True
            await message.reply_text("✅ Antilink is now enabled!")
        elif arg == "off":
            antilink_enabled[chat_id] = False
            await message.reply_text("🚫 Antilink is now disabled!")
        else:
            await message.reply_text("⚙️ Use `/antilink on` or `/antilink off`")
    else:
        await message.reply_text("⚙️ Use `/antilink on` or `/antilink off`")

@app.on_message(filters.text | filters.caption & filters.group)
async def antilink(client, message: Message):
    """Detect and delete messages containing links."""
    chat_id = message.chat.id

    if antilink_enabled.get(chat_id, False):
        text = message.text or message.caption
        if text and LINK_REGEX.search(text):
            try:
                await message.delete()
                user = message.from_user
                await message.reply_text(
                    f"🚫 Links are not allowed, [{user.first_name}](tg://user?id={user.id})!",
                    quote=True
                )
            except Exception as e:
                print(f"Failed to delete message: {e}")
