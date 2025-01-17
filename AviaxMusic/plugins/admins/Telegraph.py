import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AviaxMusic import app
import requests


def upload_file(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "json": "true"}
    files = {"fileToUpload": open(file_path, "rb")}
    response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        return True, response.text.strip()
    else:
        return False, f"ᴇʀʀᴏʀ: {response.status_code} - {response.text}"


@app.on_message(filters.command(["tgm"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Pʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴏɴ Tᴇʟᴇɢʀᴀᴘʜ"
        )

    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size

    if file_size > 200 * 1024 * 1024:
        return await message.reply_text("Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴍᴇᴅɪᴀ ғɪʟᴇ ᴜɴᴅᴇʀ 200MB.")

    try:
        await message.reply_sticker("CAACAgUAAx0CeFC7pwABAWZbZ4noEUQbvpGd_r8M3NXJqZ2Fz30AAksGAAInF9FXvt_AF2vndqseBA")

        async def progress(current, total):
            try:
                await message.reply_sticker("CAACAgUAAx0CeFC7pwABAWZbZ4noEUQbvpGd_r8M3NXJqZ2Fz30AAksGAAInF9FXvt_AF2vndqseBA")
            except Exception:
                pass

        try:
            local_path = await media.download(progress=progress)
            await message.reply_sticker("CAACAgUAAx0CeFC7pwABAWZiZ4noaXa5fDf8Jh_iHZMvR3gX3acAAtwEAAKyutlXmLbVduyZE6UeBA")

            success, upload_path = upload_file(local_path)

            if success:
                await message.reply_text(
                    f"🌐 | [👉ʏᴏᴜʀ ʟɪɴᴋ ᴛᴀᴘ ʜᴇʀᴇ👈]({upload_path})",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    " ᴛᴀᴘ ᴛᴏ sᴇᴇ ",
                                    url=upload_path,
                                )
                            ]
                        ]
                    ),
                )
            else:
                await message.reply_text(
                    f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ᴜᴘʟᴏᴀᴅɪɴɢ ʏᴏᴜʀ ғɪʟᴇ\n{upload_path}"
                )

            try:
                os.remove(local_path)
            except Exception:
                pass

        except Exception as e:
            await message.reply_text(f"❌ Fɪʟᴇ ᴜᴘʟᴏᴀᴅ ғᴀɪʟᴇᴅ\n\n<i>Rᴇᴀsᴏɴ: {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
                pass
            return
    except Exception:
        pass






import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AviaxMusic import app
import requests


def upload_file(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "json": "true"}
    files = {"fileToUpload": open(file_path, "rb")}
    response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        return True, response.text.strip()
    else:
        return False, f"ᴇʀʀᴏʀ: {response.status_code} - {response.text}"


@app.on_message(filters.command(["tm", "telegraph"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Pʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴏɴ Tᴇʟᴇɢʀᴀᴘʜ"
        )

    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size

    if file_size > 200 * 1024 * 1024:
        return await message.reply_text("Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴍᴇᴅɪᴀ ғɪʟᴇ ᴜɴᴅᴇʀ 200MB.")

    try:
        await message.reply_sticker("CAACAgUAAx0CeFC7pwABAWZbZ4noEUQbvpGd_r8M3NXJqZ2Fz30AAksGAAInF9FXvt_AF2vndqseBA")

        async def progress(current, total):
            try:
                await message.reply_sticker("CAACAgUAAx0CeFC7pwABAWZbZ4noEUQbvpGd_r8M3NXJqZ2Fz30AAksGAAInF9FXvt_AF2vndqseBA")
            except Exception:
                pass

        try:
            local_path = await media.download(progress=progress)
            await message.reply_sticker("CAACAgUAAx0CeFC7pwABAWZiZ4noaXa5fDf8Jh_iHZMvR3gX3acAAtwEAAKyutlXmLbVduyZE6UeBA")

            success, upload_path = upload_file(local_path)

            if success:
                await message.reply_text(
                    f"🌐 | [👉ʏᴏᴜʀ ʟɪɴᴋ ᴛᴀᴘ ʜᴇʀᴇ👈]({upload_path})",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    " ᴛᴀᴘ ᴛᴏ sᴇᴇ ",
                                    url=upload_path,
                                )
                            ]
                        ]
                    ),
                )
            else:
                await message.reply_text(
                    f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ᴜᴘʟᴏᴀᴅɪɴɢ ʏᴏᴜʀ ғɪʟᴇ\n{upload_path}"
                )

            try:
                os.remove(local_path)
            except Exception:
                pass

        except Exception as e:
            await message.reply_text(f"❌ Fɪʟᴇ ᴜᴘʟᴏᴀᴅ ғᴀɪʟᴇᴅ\n\n<i>Rᴇᴀsᴏɴ: {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
                pass
            return
    except Exception:
        pass
