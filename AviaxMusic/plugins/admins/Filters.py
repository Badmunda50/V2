import re
from AviaxMusic import app
from Yukki import Owner
from AviaxMusic.utils.database import *
from AviaxMusic.utils.filters_func import GetFIlterMessage, get_text_reason, SendFilterMessage
from pyrogram import filters, enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

@app.on_message(filters.command("filter"))
async def _filter(client, message):
    user = message.from_user.id
    chat_id = message.chat.id 
    chat = message.chat
    if user in Owner:
        pass
    else:
        member = await chat.get_member(user)
        if member.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
            pass
        else:
            msg_text = "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛꜱ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ ."
            return await message.reply_text(msg_text)
    
    if message.reply_to_message and not len(message.command) == 2:
        await message.reply("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴀɴᴅ ɢɪᴠᴇ ꜰɪʟᴛᴇʀ ɴᴀᴍᴇ ᴀꜰᴛᴇʀ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴀᴠᴇ ɪᴛ")  
        return 

    filter_name, filter_reason = get_text_reason(message)
    
    if message.reply_to_message and not len(message.command) >= 2:
        await message.reply("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴀɴᴅ ɢɪᴠᴇ ꜰɪʟᴛᴇʀ ɴᴀᴍᴇ ᴀꜰᴛᴇʀ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴀᴠᴇ ɪᴛ!")
        return

    content, text, data_type = await GetFIlterMessage(message)
    await add_filter_db(chat_id, filter_name=filter_name, content=content, text=text, data_type=data_type)
    await message.reply(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴀᴠᴇᴅ ꜰɪʟᴛᴇʀ ɪɴ {message.chat.title} \n\nꜰɪʟᴛᴇʀ ɴᴀᴍᴇ - '{filter_name}'.")


@app.on_message(~filters.bot & filters.group, group=4)
async def FilterChecker(client, message):
    if not message.text:
        return
    
    text = message.text
    chat_id = message.chat.id
    
    if len(await get_filters_list(chat_id)) == 0:
        return

    ALL_FILTERS = await get_filters_list(chat_id)
    
    for filter_ in ALL_FILTERS:
        if message.command and message.command[0] == 'filter' and len(message.command) >= 2 and message.command[1] == filter_:
            return

        pattern = r"( |^|[^\w])" + re.escape(filter_) + r"( |$|[^\w])"
        
        if re.search(pattern, text, flags=re.IGNORECASE):
            filter_data = await get_filter(chat_id, filter_)
            if filter_data:
                filter_name, content, text, data_type = filter_data
                await SendFilterMessage(message=message, filter_name=filter_, content=content, text=text, data_type=data_type)
            else:
                # Handle the case where the filter is not found
                pass

@app.on_message(filters.command('filters') & filters.group)
async def _filters(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title 
    
    if message.chat.type == 'private':
        chat_title = 'local'
    
    FILTERS = await get_filters_list(chat_id)

    if len(FILTERS) == 0:
        await message.reply(f'ɴᴏ ꜰɪʟᴛᴇʀꜱ ꜰᴏᴜɴᴅ ɪɴ {chat_title}.')
        return

    filters_list = f'ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʟɪꜱᴛ ᴏꜰ ᴀʟʟ ꜰɪʟᴛᴇʀꜱ ɪɴ  {chat_title}:\n'

    for filter_ in FILTERS:
        filters_list += f'- `{filter_}`\n'

    await message.reply(filters_list)


@app.on_message(filters.command('stopall'))
async def stopall(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title 
    user_id = message.from_user.id
    user = await client.get_chat_member(chat_id, message.from_user.id)
    
    if user_id in Owner:
        pass
    else:
        member = await message.chat.get_member(user_id)
        if member.status == enums.ChatMemberStatus.OWNER:
            pass
        else:
            msg_text = "ᴏɴʟʏ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀ ᴄᴀɴ ᴅᴏ ᴛʜɪꜱ"
            return await message.reply_text(msg_text)
    
    KEYBOARD = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴛᴇʀꜱ ❗', callback_data='custfilters_stopall')],
        [InlineKeyboardButton(text="ʟᴇᴛ'ꜱ ᴄᴀɴᴄᴇʟ ɪᴛ 🐬", callback_data='custfilters_cancel')]]
    )

    await message.reply_text(
        text=f"ᴀʀᴇ ʏᴏᴜ ꜱᴜʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴛᴏᴘ ᴀʟʟ ꜰɪʟᴛᴇʀꜱ ɪɴ {chat_title}?",reply_markup=KEYBOARD
    )


@app.on_callback_query(filters.regex("^custfilters_"))
async def stopall_callback(client, callback_query: CallbackQuery):  
    chat_id = callback_query.message.chat.id 
    query_data = callback_query.data.split('_')[1]  
    user_id = callback_query.from_user.id
    user = await client.get_chat_member(chat_id, user_id)

    if user_id in Owner:
        pass
    else:
        if user.status == enums.ChatMemberStatus.OWNER:
            pass
        else:
            msg_text = "ꜱᴏʀʀʏ ᴛʜɪꜱ ɪꜱ ᴏɴʟʏ ꜰᴏʀ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀ."
            return await callback_query.answer(msg_text, show_alert=True)
            
    if query_data == 'stopall':
        await stop_all_db(chat_id)
        await callback_query.edit_message_text(text="ɪ ᴅᴇʟᴇᴛᴇᴅ ᴀʟʟ ꜰɪʟᴛᴇʀꜱ .")

    elif query_data == 'cancel':
        await callback_query.edit_message_text(text='ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄᴀɴᴄᴇʟʟᴇᴅ ')


@app.on_message(filters.command('stopfilter'))
async def stop(client, message):
    chat_id = message.chat.id
    uid = message.from_user.id
    
    if not (len(message.command) >= 2):
        await message.reply('ꜱᴇᴇ ʜᴇʟᴘ ꜱᴇᴄᴛɪᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ')
        return
    
    if uid in Owner:
        pass
    else:
        member = await message.chat.get_member(uid)
        if member.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
            pass
        else:
            msg_text = "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛꜱ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ "
            return await message.reply_text(msg_text)
    
    filter_name = message.command[1]
    if filter_name not in await get_filters_list(chat_id):
        await message.reply("ɪ ᴅɪᴅɴ'ᴛ ꜰɪɴᴅ ᴛʜɪꜱ ɴᴀᴍᴇ ꜰɪʟᴛᴇʀ !")
        return

    await stop_db(chat_id, filter_name)
    await message.reply(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴛᴏᴘᴘᴇᴅ  '{filter_name}'.")
