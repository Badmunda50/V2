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

@app.on_callback_query(filters.regex("gotohelp") & ~BANNED_USERS)
async def feature_callback(client: app, callback_query: CallbackQuery):
    keyboard = [
        [
            InlineKeyboardButton(
                text="💫 ᴀᴅᴅ ᴍᴇ ᴍᴏʀᴇ ❤️",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="🎧 ᴍᴜsɪᴄ 🎧", callback_data="music"),
            InlineKeyboardButton(text="🤖 ᴍᴀɴᴀɢᴇᴍᴇɴᴛ 🤖", callback_data="management"),
            InlineKeyboardButton(text="🤖 ᴀɪ 🤖", callback_data="ai"),
        ],
        [InlineKeyboardButton(text="✯ ʜᴏᴍᴇ ✯", callback_data="go_to_start")],
    ]
    await callback_query.message.edit_text(
        f"<b>**Wᴇʟᴄᴏᴍᴇ ᴛᴏ** {app.mention}\n\n**Exᴘʟᴏʀᴇ ᴀ ᴡɪᴅᴇ ʀᴀɴɢᴇ ᴏғ ғᴇᴀᴛᴜʀᴇs ᴅᴇsɪɢɴᴇᴅ ᴛᴏ ᴇɴʜᴀɴᴄᴇ ʏᴏᴜʀ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ**</b>",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

@app.on_callback_query(filters.regex("music"))
async def music_callback(client: app, callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Aᴅᴍɪɴ", callback_data="music_callback ms1"),
                InlineKeyboardButton(text="Aᴜᴛʜ", callback_data="music_callback ms2"),
                InlineKeyboardButton(
                    text="Bʀᴏᴀᴅᴄᴀsᴛ", callback_data="music_callback ms3"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Bʟ-Cʜᴀᴛ", callback_data="music_callback ms4"
                ),
                InlineKeyboardButton(
                    text="Bʟ-Usᴇʀ", callback_data="music_callback ms5"
                ),
                InlineKeyboardButton(text="C-Pʟᴀʏ", callback_data="music_callback ms6"),
            ],
            [
                InlineKeyboardButton(text="G-Bᴀɴ", callback_data="music_callback ms7"),
                InlineKeyboardButton(text="Lᴏᴏᴘ", callback_data="music_callback ms8"),
                InlineKeyboardButton(
                    text="Mᴀɪɴᴛᴇɴᴀɴᴄᴇ", callback_data="music_callback ms9"
                ),
            ],
            [
                InlineKeyboardButton(text="Pɪɴɢ", callback_data="music_callback ms10"),
                InlineKeyboardButton(text="Pʟᴀʏ", callback_data="music_callback ms11"),
                InlineKeyboardButton(
                    text="Sʜᴜғғʟᴇ", callback_data="music_callback ms12"
                ),
            ],
            [
                InlineKeyboardButton(text="Sᴇᴇᴋ", callback_data="music_callback ms13"),
                InlineKeyboardButton(text="Sᴏɴɢ", callback_data="music_callback ms14"),
                InlineKeyboardButton(text="Sᴘᴇᴇᴅ", callback_data="music_callback ms15"),
            ],
            [InlineKeyboardButton(text="✯ ʙᴀᴄᴋ ✯", callback_data=f"gotohelp")],
        ]
    )

    new_text = "<b>ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴍᴜꜱɪᴄ ᴏᴘᴛɪᴏɴꜱ...</b>"
    if callback_query.message.text != new_text:
        await callback_query.message.edit(
            new_text, reply_markup=keyboard
        )

@app.on_callback_query(filters.regex("music_callback") & ~BANNED_USERS)
@languageCB
async def music_helper_cb(client, CallbackQuery, _):

    callback_data = CallbackQuery.data.strip()

    cb = callback_data.split(None, 1)[1]

    keyboard = back_to_music(_)

    if cb == "ms1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "ms2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "ms3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "ms4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "ms5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "ms6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "ms7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "ms8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "ms9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "ms10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)
    elif cb == "ms11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)
    elif cb == "ms12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)
    elif cb == "ms13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)
    elif cb == "ms14":
        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboard)
    elif cb == "ms15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)

@app.on_callback_query(filters.regex("management"))
async def management_callback(client: app, callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Option 1", callback_data="management_callback hb1"),
                InlineKeyboardButton(text="Option 2", callback_data="management_callback hb2")
            ],
            [InlineKeyboardButton(text="✯ ʙᴀᴄᴋ ✯", callback_data=f"gotohelp")],
        ]
    )

    new_text = "<b>ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴏᴘᴛɪᴏɴs...</b>"
    if callback_query.message.text != new_text:
        await callback_query.message.edit(
            new_text, reply_markup=keyboard
        )

@app.on_callback_query(filters.regex("management_callback") & ~BANNED_USERS)
@languageCB
async def management_helper_cb(client, CallbackQuery, _):

    callback_data = CallbackQuery.data.strip()

    cb = callback_data.split(None, 1)[1]

    keyboard = back_to_music(_)

    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)

@app.on_callback_query(filters.regex("ai"))
async def ai_callback(client: app, callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="Option 1", callback_data="ai_callback ai1"),
                InlineKeyboardButton(text="Option 2", callback_data="ai_callback ai2")
            ],
            [InlineKeyboardButton(text="✯ ʙᴀᴄᴋ ✯", callback_data=f"gotohelp")],
        ]
    )

    new_text = "<b>ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴀɪ ᴏᴘᴛɪᴏɴs...</b>"
    if callback_query.message.text != new_text:
        await callback_query.message.edit(
            new_text, reply_markup=keyboard
        )

@app.on_callback_query(filters.regex("ai_callback") & ~BANNED_USERS)
@languageCB
async def ai_helper_cb(client, CallbackQuery, _):

    callback_data = CallbackQuery.data.strip()

    cb = callback_data.split(None, 1)[1]

    keyboard = back_to_music(_)

    if cb == "ai1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "ai2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)

@app.on_callback_query(filters.regex("back_to_music"))
async def feature_callback(client: app, callback_query: CallbackQuery):
    keyboard = [
        [
            InlineKeyboardButton(
                text="💫 ᴀᴅᴅ ᴍᴇ ᴍᴏʀᴇ ❤️",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="🎧 ᴍᴜsɪᴄ 🎧", callback_data="music"),
            InlineKeyboardButton(text="🤖 ᴍᴀɴᴀɢᴇᴍᴇɴᴛ 🤖", callback_data="management"),
            InlineKeyboardButton(text="🤖 ᴀɪ 🤖", callback_data="ai"),
        ],
        [InlineKeyboardButton(text="✯ ʜᴏᴍᴇ ✯", callback_data="go_to_start")],
    ]
    await callback_query.message.edit_text(
        "<b>ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ʙᴏᴛ ꜰᴇᴀᴛᴜʀᴇs...</b>", reply_markup=InlineKeyboardMarkup(keyboard)
    )

def back_to_music(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"music",
                ),
            ]
        ]
    )
    return upl

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

# third help panel
@app.on_callback_query(filters.regex("thirdhelppanel") & ~BANNED_USERS)
@languageCB
async def third_help_panel(client, callback_query: CallbackQuery, _):
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

# fourth help panel
@app.on_callback_query(filters.regex("fourthhelppanel") & ~BANNED_USERS)
@languageCB
async def fourth_help_panel(client, callback_query: CallbackQuery, _):
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
    
