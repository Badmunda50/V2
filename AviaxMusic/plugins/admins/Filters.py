import re
from AviaxMusic import Bad as app
from Yukki import Owner
from AviaxMusic.utils.database import *
from AviaxMusic.utils.filters_func import GetFIlterMessage, get_text_reason, SendFilterMessage
from telethon import events, Button
from telethon.tl.types import ChatAdminRights, ChannelParticipantsAdmins

@app.on(events.NewMessage(pattern='/filter'))
async def _filter(event):
    user = event.sender_id
    chat_id = event.chat_id
    chat = await event.get_chat()
    
    if user in Owner:
        pass
    else:
        member = await event.client.get_participant(chat_id, user)
        if member.admin_rights:
            pass
        else:
            msg_text = "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛꜱ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ ."
            await event.reply(msg_text)
            return
    
    if event.is_reply and not len(event.text.split()) == 2:
        await event.reply("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴀɴᴅ ɢɪᴠᴇ ꜰɪʟᴛᴇʀ ɴᴀᴍᴇ ᴀꜰᴛᴇʀ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴀᴠᴇ ɪᴛ")
        return

    filter_name, filter_reason = get_text_reason(event.message)
    
    if event.is_reply and not len(event.text.split()) >= 2:
        await event.reply("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴀɴᴅ ɢɪᴠᴇ ꜰɪʟᴛᴇʀ ɴᴀᴍᴇ ᴀꜰᴛᴇʀ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴀᴠᴇ ɪᴛ!")
        return

    content, text, data_type = await GetFIlterMessage(event.message)
    await add_filter_db(chat_id, filter_name=filter_name, content=content, text=text, data_type=data_type)
    await event.reply(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴀᴠᴇᴅ ꜰɪʟᴛᴇʀ ɪɴ {chat.title} \n\nꜰɪʟᴛᴇʀ ɴᴀᴍᴇ - '{filter_name}'.")


@app.on(events.NewMessage(pattern='^(?!/).+'))
async def FilterChecker(event):
    if not event.message.text:
        return
    
    text = event.message.text
    chat_id = event.chat_id
    
    ALL_FILTERS = await get_filters_list(chat_id)
    if len(ALL_FILTERS) == 0:
        return

    for filter_ in ALL_FILTERS:
        pattern = r"( |^|[^\w])" + re.escape(filter_) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            filter_data = await get_filter(chat_id, filter_)
            if filter_data:
                filter_name, content, text, data_type = filter_data
                await SendFilterMessage(message=event.message, filter_name=filter_name, content=content, text=text, data_type=data_type)
                return  # Ensure only one filter is applied per message
            else:
                pass


@app.on(events.NewMessage(pattern='/filters'))
async def _filters(event):
    chat_id = event.chat_id
    chat_title = (await event.get_chat()).title
    
    if event.is_private:
        chat_title = 'local'
    
    FILTERS = await get_filters_list(chat_id)

    if len(FILTERS) == 0:
        await event.reply(f'ɴᴏ ꜰɪʟᴛᴇʀꜱ ꜰᴏᴜɴᴅ ɪɴ {chat_title}.')
        return

    filters_list = f'ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʟɪꜱᴛ ᴏꜰ ᴀʟʟ ꜰɪʟᴛᴇʀꜱ ɪɴ  {chat_title}:\n'

    for filter_ in FILTERS:
        filters_list += f'- `{filter_}`\n'

    await event.reply(filters_list)


@app.on(events.NewMessage(pattern='/stopall'))
async def stopall(event):
    chat_id = event.chat_id
    chat_title = (await event.get_chat()).title
    user_id = event.sender_id
    user = await event.client.get_participant(chat_id, user_id)
    
    if user_id in Owner:
        pass
    else:
        if user.admin_rights:
            pass
        else:
            msg_text = "ᴏɴʟʏ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀ ᴄᴀɴ ᴅᴏ ᴛʜɪꜱ"
            await event.reply(msg_text)
            return
    
    KEYBOARD = [
        [Button.inline('ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴛᴇʀꜱ ❗', b'custfilters_stopall')],
        [Button.inline("ʟᴇᴛ'ꜱ ᴄᴀɴᴄᴇʟ ɪᴛ 🐬", b'custfilters_cancel')]
    ]

    await event.reply(
        text=f"ᴀʀᴇ ʏᴏᴜ ꜱᴜʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴛᴏᴘ ᴀʟʟ ꜰɪʟᴛᴇʀꜱ ɪɴ {chat_title}?", buttons=KEYBOARD
    )


@app.on(events.CallbackQuery(pattern=b'^custfilters_'))
async def stopall_callback(event):
    chat_id = event.chat_id
    query_data = event.data.decode().split('_')[1]
    user_id = event.sender_id
    user = await event.client.get_participant(chat_id, user_id)

    if user_id in Owner:
        pass
    else:
        if user.admin_rights:
            pass
        else:
            msg_text = "ꜱᴏʀʀʏ ᴛʜɪꜱ ɪꜱ ᴏɴʟʏ ꜰᴏʀ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀ."
            await event.answer(msg_text, alert=True)
            return
            
    if query_data == 'stopall':
        await stop_all_db(chat_id)
        await event.edit("ɪ ᴅᴇʟᴇᴛᴇᴅ ᴀʟʟ ꜰɪʟᴛᴇʀꜱ .")
    elif query_data == 'cancel':
        await event.edit('ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄᴀɴᴄᴇʟʟᴇᴅ')


@app.on(events.NewMessage(pattern='/stopfilter'))
async def stop(event):
    chat_id = event.chat_id
    uid = event.sender_id
    
    if not (len(event.text.split()) >= 2):
        await event.reply('ꜱᴇᴇ ʜᴇʟᴘ ꜱᴇᴄᴛɪᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ')
        return
    
    if uid in Owner:
        pass
    else:
        member = await event.client.get_participant(chat_id, uid)
        if member.admin_rights:
            pass
        else:
            msg_text = "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛꜱ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ "
            await event.reply(msg_text)
            return
    
    filter_name = event.text.split()[1]
    if filter_name not in await get_filters_list(chat_id):
        await event.reply("ɪ ᴅɪᴅɴ'ᴛ ꜰɪɴᴅ ᴛʜɪꜱ ɴᴀᴍᴇ ꜰɪʟᴛᴇʀ !")
        return

    await stop_db(chat_id, filter_name)
    await event.reply(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴛᴏᴘᴘᴇᴅ  '{filter_name}'.")
