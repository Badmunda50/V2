import time
from collections import defaultdict
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext
from AviaxMusic import application

# Flood tracking
user_message_counts = defaultdict(lambda: {"count": 0, "timestamp": 0})
FLOOD_LIMIT = 5  # Messages allowed per 5 seconds
MUTE_DURATION = 60  # Mute time in seconds
antispam_enabled = True  # Default: Enabled

async def toggle_antispam(update: Update, context: CallbackContext) -> None:
    global antispam_enabled
    chat_id = update.message.chat_id
    user = update.message.from_user
    
    if not user or not user.id:  # Ensure we have a valid user
        return

    # Get chat administrators
    chat_admins = await context.bot.get_chat_administrators(chat_id)
    admin_ids = [admin.user.id for admin in chat_admins]

    if user.id not in admin_ids:  # Check if user is admin
        await update.message.reply_text("❌ You must be an admin to toggle Antispam!")
        return

    if context.args and context.args[0].lower() == "on":
        antispam_enabled = True
        await update.message.reply_text("✅ Antispam is now enabled!")
    elif context.args and context.args[0].lower() == "off":
        antispam_enabled = False
        await update.message.reply_text("🚫 Antispam is now disabled!")
    else:
        await update.message.reply_text("⚙️ Use `/antispam on` or `/antispam off`")

async def antispam(update: Update, context: CallbackContext) -> None:
    if not antispam_enabled:
        return

    user_id = update.message.from_user.id
    chat_id = update.message.chat_id
    current_time = time.time()

    if user_id in user_message_counts:
        last_time = user_message_counts[user_id]["timestamp"]
        if current_time - last_time <= 5:
            user_message_counts[user_id]["count"] += 1
        else:
            user_message_counts[user_id]["count"] = 1

        user_message_counts[user_id]["timestamp"] = current_time

        if user_message_counts[user_id]["count"] > FLOOD_LIMIT:
            try:
                await context.bot.restrict_chat_member(chat_id, user_id, can_send_messages=False, until_date=int(current_time + MUTE_DURATION))
                await update.message.reply_text(f"🚨 @{update.message.from_user.username} muted for spamming!")
            except Exception as e:
                print(f"Failed to mute user: {e}")

app_instance = application
app_instance.add_handler(CommandHandler("antispam", toggle_antispam))
app_instance.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, antispam))
