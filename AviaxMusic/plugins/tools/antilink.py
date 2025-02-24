import re
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions

# Regex for detecting links
LINK_REGEX = re.compile(r"https?://\S+")

# Dictionary to store antilink settings for different chats
antilink_enabled = {}

async def is_admin(client, message: Message) -> bool:
    """Check if the user is an admin."""
    chat_id = message.chat.id
    user_id = message.from_user.id

    member = await client.get_chat_member(chat_id, user_id)
    return member.status in ["administrator", "creator"]

@Client.on_message(filters.command("antilink") & filters.group)
async def toggle_antilink(client, message: Message):
    """Enable or disable antilink in the group."""
    chat_id = message.chat.id

    if not await is_admin(client, message):
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

@Client.on_message(filters.text | filters.caption & filters.group)
async def antilink(client, message: Message):
    """Detect and delete messages containing links."""
    chat_id = message.chat.id

    if antilink_enabled.get(chat_id, False):
        text = message.text or message.caption
        if text and LINK_REGEX.search(text):
            try:
                await message.delete()
                await message.reply_text(
                    f"🚫 Links are not allowed, @{message.from_user.username}!",
                    quote=True
                )
            except Exception as e:
                print(f"Failed to delete message: {e}")
