from typing import Union
from pyrogram.types import InputMediaPhoto
import random 
from config import SUPPORT_GROUP
from pyrogram.enums import ChatType
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message, CallbackQuery
from config import START_IMG_URL
from config import BANNED_USERS
from strings import get_command, get_string, helpers
from AviaxMusic import app
from AviaxMusic.misc import SUDOERS
from AviaxMusic.utils.database import get_lang
from AviaxMusic.utils.decorators.language import LanguageStart, languageCB
from AviaxMusic.utils.inline.eg import *

HELP_COMMAND = get_command("HELP_COMMAND")

# first help page
@app.on_message(filters.command(HELP_COMMAND) & filters.private & ~BANNED_USERS)
@app.on_callback_query(
    filters.regex("gotohelp") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        user = update.from_user.mention
        keyboard = first_panel(_, True)
        await update.edit_message_text(
            _["help_1"].format(user),reply_markup=keyboard
        )
    else:
        user = update.from_user.mention
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = first_panel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(user),
            reply_markup=keyboard,
      )
# second help page


@app.on_callback_query(filters.regex("secondhelppanel") & ~BANNED_USERS)
@languageCB
async def second_help_panel(client, callback_query: CallbackQuery, _):
    try:
        await callback_query.answer()
    except:
        pass    
    try:
        
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            buttons = second_panel(_, True)  
            user = callback_query.from_user.mention
            await callback_query.edit_message_text(
                _["help_1"].format(user),  
                reply_markup=buttons
            )
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")

# third help pannel

@app.on_callback_query(filters.regex("thirdhelppanel") & ~BANNED_USERS)
@languageCB
async def second_help_panel(client, callback_query: CallbackQuery, _):
    try:
        await callback_query.answer()
    except:
        pass    
    try:
        
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            buttons = third_panel(_, True)  
            user = callback_query.from_user.mention
            await callback_query.edit_message_text(
                _["help_1"].format(user),  
                reply_markup=buttons
            )
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")


# four help pannel

@app.on_callback_query(filters.regex("fourthhelppanel") & ~BANNED_USERS)
@languageCB
async def second_help_panel(client, callback_query: CallbackQuery, _):
    try:
        await callback_query.answer()
    except:
        pass    
    try:
        
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            buttons = fourth_panel(_, True)  
            user = callback_query.from_user.mention
            await callback_query.edit_message_text(
                _["help_1"].format(user),  
                reply_markup=buttons
            )
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")



@app.on_message(filters.command(HELP_COMMAND) & filters.group & ~BANNED_USERS)
@languageCB
async def help_com_group(client, message: Message, _):
    keyboard = first_panel(_, True)
    await message.reply_photo(photo=START_IMG_URL,
                              caption=_["help_2"],
                              reply_markup=keyboard
                             )

