from re import findall
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
)
from pyrogram import enums
from Yukki import Owner
from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.types import (
    Chat,
    ChatPermissions,
    ChatMemberUpdated,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    User,
)

from AviaxMusic import app
from AviaxMusic.misc import SUDOERS
from AviaxMusic.utils.error import capture_err
from AviaxMusic.utils.database.weldbb import (
    del_welcome,
    get_welcome,
    set_welcome,
)
from AviaxMusic.utils.database import is_gbanned_user


def extract_text_and_keyb(ikb, text: str, row_width: int = 2):
    keyboard = {}
    try:
        text = text.strip()
        if text.startswith("`"):
            text = text[1:]
        if text.endswith("`"):
            text = text[:-1]

        if "~~" in text:
            text = text.replace("~~", "¤¤")
        text, keyb = text.split("~")
        if "¤¤" in text:
            text = text.replace("¤¤", "~~")

        keyb = findall(r"\[.+\,.+\]", keyb)
        for btn_str in keyb:
            btn_str = re_sub(r"[\[\]]", "", btn_str)
            btn_str = btn_str.split(",")
            btn_txt, btn_url = btn_str[0], btn_str[1].strip()

            if not get_urls_from_text(btn_url):
                continue
            keyboard[btn_txt] = btn_url
        keyboard = ikb(keyboard, row_width)
    except Exception:
        return
    return text, keyboard


async def check_format(ikb, raw_text: str):
    keyb = findall(r"\[.+\,.+\]", raw_text)
    if keyb and not "~" in raw_text:
        raw_text = raw_text.replace("button=", "\n~\nbutton=")
        return raw_text
    if "~" in raw_text and keyb:
        if not extract_text_and_keyb(ikb, raw_text):
            return ""
        else:
            return raw_text
    else:
        return raw_text



def extract_urls(reply_markup):
    urls = []
    if reply_markup.inline_keyboard:
        buttons = reply_markup.inline_keyboard
        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                if button.url:
                    name = (
                        "\n~\nbutton"
                        if i * len(row) + j + 1 == 1
                        else f"button{i * len(row) + j + 1}"
                    )
                    urls.append((f"{name}", button.text, button.url))
    return urls
    
def ikb(data: dict, row_width: int = 2):
    return keyboard(data.items(), row_width=row_width)
    
async def handle_new_member(member, chat):

    try:
        if member.id in SUDOERS:
            return
        if await is_gbanned_user(member.id):
            await chat.ban_member(member.id)
            await app.send_message(
                chat.id,
                f"{member.mention} was globally banned, and got removed,"
                + " if you think this is a false gban, you can appeal"
                + " for this ban in support chat.",
            )
            return
        if member.is_bot:
            return
        return await send_welcome_message(chat, member.id)

    except ChatAdminRequired:
        return


@app.on_chat_member_updated(filters.group, group=6)
@capture_err
async def welcome(_, user: ChatMemberUpdated):
    if not (
        user.new_chat_member
        and user.new_chat_member.status not in {CMS.RESTRICTED}
        and not user.old_chat_member
    ):
        return

    member = user.new_chat_member.user if user.new_chat_member else user.from_user
    chat = user.chat
    return await handle_new_member(member, chat)


async def send_welcome_message(chat: Chat, user_id: int, delete: bool = False):
    welcome, raw_text, file_id = await get_welcome(chat.id)

    if not raw_text:
        return
    text = raw_text
    keyb = None
    if findall(r"\[.+\,.+\]", raw_text):
        text, keyb = extract_text_and_keyb(ikb, raw_text)

    if "{chat}" in text:
        text = text.replace("{chat}", chat.title)
    if "{name}" in text:
        text = text.replace("{name}", (await app.get_users(user_id)).mention)
    if "{id}" in text:
        text = text.replace("{id}", f"`{user_id}`")

    if welcome == "Text":
        m = await app.send_message(
            chat.id,
            text=text,
            reply_markup=keyb,
            disable_web_page_preview=True,
        )
    elif welcome == "Photo":
        m = await app.send_photo(
            chat.id,
            photo=file_id,
            caption=text,
            reply_markup=keyb,
        )
    else:
        m = await app.send_animation(
            chat.id,
            animation=file_id,
            caption=text,
            reply_markup=keyb,
        )


@app.on_message(filters.command("setwelcome") & ~filters.private)
async def set_welcome_func(_, message):
    usage = "You need to reply to a text, gif or photo to set it as greetings.\n\nNotes: caption required for gif and photo."
    key = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="More Help",
                    url=f"t.me/{app.username}?start=greetings",
                )
            ],
        ]
    )
    replied_message = message.reply_to_message
    chat_id = message.chat.id
    admin_id = message.from_user.id
    if admin_id in Owner:
        pass
    else:
        member = await chat.get_member(admin_id)
        if member.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
            if member.privileges.can_change_info:
                pass
            else:
                msg_text = "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛꜱ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ.."
                return await message.reply_text(msg_text)
        else:
            msg_text = "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛꜱ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ."
            return await message.reply_text(msg_text)
    try:
        if not replied_message:
            await message.reply_text(usage, reply_markup=key)
            return
        if replied_message.animation:
            welcome = "Animation"
            file_id = replied_message.animation.file_id
            text = replied_message.caption
            if not text:
                return await message.reply_text(usage, reply_markup=key)
            raw_text = text.markdown
        if replied_message.photo:
            welcome = "Photo"
            file_id = replied_message.photo.file_id
            text = replied_message.caption
            if not text:
                return await message.reply_text(usage, reply_markup=key)
            raw_text = text.markdown
        if replied_message.text:
            welcome = "Text"
            file_id = None
            text = replied_message.text
            raw_text = text.markdown
        if replied_message.reply_markup and not findall(r"\[.+\,.+\]", raw_text):
            urls = extract_urls(replied_message.reply_markup)
            if urls:
                response = "\n".join(
                    [f"{name}=[{text}, {url}]" for name, text, url in urls]
                )
                raw_text = raw_text + response
        raw_text = await check_format(ikb, raw_text)
        if raw_text:
            await set_welcome(chat_id, welcome, raw_text, file_id)
            return await message.reply_text(
                "Welcome message has been successfully set."
            )
        else:
            return await message.reply_text(
                "Wrong formatting, check the help section.\n\n**Usage:**\nText: `Text`\nText + Buttons: `Text ~ Buttons`",
                reply_markup=key,
            )
    except UnboundLocalError:
        return await message.reply_text(
            "**Only Text, Gif and Photo welcome message are supported.**"
        )


@app.on_message(filters.command(["delwelcome", "deletewelcome"]) & ~filters.private)
async def del_welcome_func(_, message):
    if message.from_user.id in Owner:
        pass
    else:
        member = await chat.get_member(message.from_user.id)
        if member.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
            if member.privileges.can_change_info:
                pass
            else:
                msg_text = "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛꜱ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ.."
                return await message.reply_text(msg_text)
        else:
            msg_text = "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛꜱ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ."
            return await message.reply_text(msg_text)
    chat_id = message.chat.id
    await del_welcome(chat_id)
    await message.reply_text("Welcome message has been deleted.")


@app.on_message(filters.command("getwelcome") & ~filters.private)
async def get_welcome_func(_, message):
    chat = message.chat
    if message.from_user.id in Owner:
        pass
    else:
        member = await chat.get_member(message.from_user.id)
        if member.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
            if member.privileges.can_change_info:
                pass
            else:
                msg_text = "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛꜱ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ.."
                return await message.reply_text(msg_text)
        else:
            msg_text = "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛꜱ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ."
            return await message.reply_text(msg_text)
            
    welcome, raw_text, file_id = await get_welcome(chat.id)
    if not raw_text:
        return await message.reply_text("No welcome message set.")
    if not message.from_user:
        return await message.reply_text("You're anon, can't send welcome message.")

    await send_welcome_message(chat, message.from_user.id)

    await message.reply_text(
        f'Welcome: {welcome}\n\nFile_id: `{file_id}`\n\n`{raw_text.replace("`", "")}`'
    )
