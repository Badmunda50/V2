from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext
from AviaxMusic import application
from AviaxMusic.utils.admin import admin_check  # Importing the admin_check function
import re

LINK_REGEX = re.compile(r"https?://\\S+")
antilink_enabled = True  # Default: Enabled

async def toggle_antilink(update: Update, context: CallbackContext) -> None:
    global antilink_enabled
    chat_id = update.message.chat_id
    user = update.message.from_user

    if not user or not user.id:  # Ensure we have a valid user
        return

    # Use the imported admin_check function
    if not await admin_check(update, context):
        await update.message.reply_text("❌ You must be an admin to toggle Antilink!")
        return

    if context.args and context.args[0].lower() == "on":
        antilink_enabled = True
        await update.message.reply_text("✅ Antilink is now enabled!")
    elif context.args and context.args[0].lower() == "off":
        antilink_enabled = False
        await update.message.reply_text("🚫 Antilink is now disabled!")
    else:
        await update.message.reply_text("⚙️ Use `/antilink on` or `/antilink off`")

async def antilink(update: Update, context: CallbackContext) -> None:
    if not antilink_enabled:
        return

    message = update.message.text
    if LINK_REGEX.search(message):
        try:
            await update.message.delete()
            await update.message.reply_text(f"🚫 Links are not allowed, @{update.message.from_user.username}!", quote=True)
        except Exception as e:
            print(f"Failed to delete message: {e}")

app_instance = application
app_instance.add_handler(CommandHandler("antilink", toggle_antilink))
app_instance.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, antilink))
