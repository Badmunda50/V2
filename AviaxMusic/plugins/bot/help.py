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


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboardone = first_help_back_markup(_)
    keyboardtwo = second_help_back_markup(_)
    keyboardthree = third_help_back_markup(_)
    keyboardfour = fourth_help_back_markup(_)
    try:
       await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboardone)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboardone)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboardone)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboardone)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboardone)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboardone)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboardone)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboardone)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboardone)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboardone)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboardone)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboardone)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboardone)
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboardone)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboardone)
    elif cb == "hb16":
        await CallbackQuery.edit_message_text(helpers.HELP_16, reply_markup=keyboardtwo)
    elif cb == "hb17":
        await CallbackQuery.edit_message_text(helpers.HELP_17, reply_markup=keyboardtwo)
    elif cb == "hb18":
        await CallbackQuery.edit_message_text(helpers.HELP_18, reply_markup=keyboardtwo)
    elif cb == "hb19":
        await CallbackQuery.edit_message_text(helpers.HELP_19, reply_markup=keyboardtwo)
    elif cb == "hb20":
        await CallbackQuery.edit_message_text(helpers.HELP_20, reply_markup=keyboardtwo)
    elif cb == "hb21":
        await CallbackQuery.edit_message_text(helpers.HELP_21, reply_markup=keyboardtwo)
    elif cb == "hb22":
        await CallbackQuery.edit_message_text(helpers.HELP_22, reply_markup=keyboardtwo)
    elif cb == "hb23":
        await CallbackQuery.edit_message_text(helpers.HELP_23, reply_markup=keyboardtwo)
    elif cb == "hb24":
        await CallbackQuery.edit_message_text(helpers.HELP_24, reply_markup=keyboardtwo)
    elif cb == "hb25":
        await CallbackQuery.edit_message_text(helpers.HELP_25, reply_markup=keyboardtwo)
    elif cb == "hb26":
        await CallbackQuery.edit_message_text(helpers.HELP_26, reply_markup=keyboardtwo)
    elif cb == "hb27":
        await CallbackQuery.edit_message_text(helpers.HELP_27, reply_markup=keyboardtwo)
    elif cb == "hb28":
        await CallbackQuery.edit_message_text(helpers.HELP_28, reply_markup=keyboardtwo)
    elif cb == "hb29":
        await CallbackQuery.edit_message_text(helpers.HELP_29, reply_markup=keyboardtwo)
    elif cb == "hb30":
        await CallbackQuery.edit_message_text(helpers.HELP_30, reply_markup=keyboardtwo)
    elif cb == "hb31":
        await CallbackQuery.edit_message_text(helpers.HELP_31, reply_markup=keyboardthree)
    elif cb == "hb32":
        await CallbackQuery.edit_message_text(helpers.HELP_32, reply_markup=keyboardthree)
    elif cb == "hb33":
        await CallbackQuery.edit_message_text(helpers.HELP_33, reply_markup=keyboardthree)
    elif cb == "hb34":
        await CallbackQuery.edit_message_text(helpers.HELP_34, reply_markup=keyboardthree)
    elif cb == "hb35":
        await CallbackQuery.edit_message_text(helpers.HELP_35, reply_markup=keyboardthree)
    elif cb == "hb36":
        await CallbackQuery.edit_message_text(helpers.HELP_36, reply_markup=keyboardthree)
    elif cb == "hb37":
        await CallbackQuery.edit_message_text(helpers.HELP_37, reply_markup=keyboardthree)
    elif cb == "hb38":
        await CallbackQuery.edit_message_text(helpers.HELP_38, reply_markup=keyboardthree)
    elif cb == "hb39":
        await CallbackQuery.edit_message_text(helpers.HELP_39, reply_markup=keyboardthree)
    elif cb == "hb40":
        await CallbackQuery.edit_message_text(helpers.HELP_40, reply_markup=keyboardthree)
    elif cb == "hb41":
        await CallbackQuery.edit_message_text(helpers.HELP_41, reply_markup=keyboardthree)
    elif cb == "hb42":
        await CallbackQuery.edit_message_text(helpers.HELP_42, reply_markup=keyboardthree)
    elif cb == "hb43":
        await CallbackQuery.edit_message_text(helpers.HELP_43, reply_markup=keyboardthree)
    elif cb == "hb44":
        await CallbackQuery.edit_message_text(helpers.HELP_44, reply_markup=keyboardthree)
    elif cb == "hb45":
        await CallbackQuery.edit_message_text(helpers.HELP_45, reply_markup=keyboardthree)
    elif cb == "hb46":
        await CallbackQuery.edit_message_text(helpers.HELP_46, reply_markup=keyboardfour)
    elif cb == "hb47":
        await CallbackQuery.edit_message_text(helpers.HELP_47, reply_markup=keyboardfour)
    elif cb == "hb48":
        await CallbackQuery.edit_message_text(helpers.HELP_48, reply_markup=keyboardfour)
    elif cb == "hb49":
        await CallbackQuery.edit_message_text(helpers.HELP_49, reply_markup=keyboardfour)
    elif cb == "hb50":
        await CallbackQuery.edit_message_text(helpers.HELP_50, reply_markup=keyboardfour)
    elif cb == "hb51":
        await CallbackQuery.edit_message_text(helpers.HELP_51, reply_markup=keyboardfour)
    elif cb == "hb52":
        await CallbackQuery.edit_message_text(helpers.HELP_52, reply_markup=keyboardfour)
    elif cb == "hb53":
        await CallbackQuery.edit_message_text(helpers.HELP_53, reply_markup=keyboardfour)
    elif cb == "hb54":
        await CallbackQuery.edit_message_text(helpers.HELP_54, reply_markup=keyboardfour)
    elif cb == "hb55":
        await CallbackQuery.edit_message_text(helpers.HELP_55, reply_markup=keyboardfour)
    elif cb == "hb56":
        await CallbackQuery.edit_message_text(helpers.HELP_56, reply_markup=keyboardfour)
    elif cb == "hb57":
        await CallbackQuery.edit_message_text(helpers.HELP_57, reply_markup=keyboardfour)
    elif cb == "hb58":
        await CallbackQuery.edit_message_text(helpers.HELP_58, reply_markup=keyboardfour)
    elif cb == "hb59":
        await CallbackQuery.edit_message_text(helpers.HELP_59, reply_markup=keyboardfour)
    elif cb == "hb60":
        await CallbackQuery.edit_message_text(helpers.HELP_60, reply_markup=keyboardfour)
    

