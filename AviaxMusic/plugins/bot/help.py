from math import ceil
from typing import Union
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message, CallbackQuery
from config import START_IMG_URL, BANNED_USERS
from strings import get_command, get_string
from AviaxMusic import app, HELPABLE
from AviaxMusic.utils.decorators.language import LanguageStart
from AviaxMusic.utils.database import get_lang
from AviaxMusic.utils.inline.eg import first_panel

HELP_COMMAND = get_command("HELP_COMMAND")
COLUMN_SIZE = 4  # number of button height
NUM_COLUMNS = 3  # number of button width

class EqInlineKeyboardButton(types.InlineKeyboardButton):
    def __eq__(self, other):
        return self.text == other.text

    def __lt__(self, other):
        return self.text < other.text

    def __gt__(self, other):
        return self.text > other.text

def paginate_modules(page_n, module_dict, prefix, chat=None, close: bool = False):
    if not chat:
        modules = sorted(
            [
                EqInlineKeyboardButton(
                    x.__MODULE__,
                    callback_data="{}_module({},{})".format(
                        prefix, x.__MODULE__.lower(), page_n
                    ),
                )
                for x in module_dict.values()
            ]
        )
    else:
        modules = sorted(
            [
                EqInlineKeyboardButton(
                    x.__MODULE__,
                    callback_data="{}_module({},{},{})".format(
                        prefix, chat, x.__MODULE__.lower(), page_n
                    ),
                )
                for x in module_dict.values()
            ]
        )

    pairs = [modules[i : i + NUM_COLUMNS] for i in range(0, len(modules), NUM_COLUMNS)]
    max_num_pages = ceil(len(pairs) / COLUMN_SIZE) if len(pairs) > 0 else 1
    modulo_page = page_n % max_num_pages

    if len(pairs) > COLUMN_SIZE:
        pairs = pairs[modulo_page * COLUMN_SIZE : COLUMN_SIZE * (modulo_page + 1)] + [
            (
                EqInlineKeyboardButton(
                    "❮",
                    callback_data="{}_prev({})".format(
                        prefix,
                        modulo_page - 1 if modulo_page > 0 else max_num_pages - 1,
                    ),
                ),
                EqInlineKeyboardButton(
                    "ᴄʟᴏsᴇ" if close else "Bᴀᴄᴋ",
                    callback_data="close" if close else "feature",
                ),
                EqInlineKeyboardButton(
                    "❯",
                    callback_data="{}_next({})".format(prefix, modulo_page + 1),
                ),
            )
        ]
    else:
        pairs.append(
            [
                EqInlineKeyboardButton(
                    "ᴄʟᴏsᴇ" if close else "Bᴀᴄᴋ",
                    callback_data="close" if close else "feature",
                ),
            ]
        )

    return pairs

@app.on_message(filters.command(HELP_COMMAND) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
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
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))

        await update.edit_message_text(_["help_1"], reply_markup=keyboard)
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = InlineKeyboardMarkup(
            paginate_modules(0, HELPABLE, "help", close=True)
        )
        if START_IMG_URL:

            await update.reply_photo(
                photo=START_IMG_URL,
                caption=_["help_1"],
                reply_markup=keyboard,
            )

        else:

            await update.reply_text(
                text=_["help_1"],
                reply_markup=keyboard,
            )

@app.on_message(filters.command(HELP_COMMAND) & filters.group & ~BANNED_USERS)
async def help_com_group(client, message: Message):
    keyboard = first_panel()
    await message.reply_text("Here is the help information for the group.", reply_markup=InlineKeyboardMarkup(keyboard))

@app.on_callback_query(filters.regex("feature"))
async def feature_callback(client, callback_query: CallbackQuery):
    keyboard = [
        [
            types.InlineKeyboardButton(
                text="💫 ᴀᴅᴅ ᴍᴇ ᴍᴏʀᴇ ❤️",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            types.InlineKeyboardButton(text="🎧 ᴍᴜsɪᴄ 🎧", callback_data="music"),
            types.InlineKeyboardButton(text="🤖 ᴍᴀɴᴇɢᴇᴍᴇɴᴛ 🤖", callback_data="settings_back_helper"),
        ],
        [types.InlineKeyboardButton(text="✯ ʜᴏᴍᴇ ✯", callback_data="go_to_start")],
    ]
    await callback_query.message.edit_text(
        "Explore a wide range of features designed to enhance your music experience.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

@app.on_callback_query(filters.regex("music"))
async def music_callback(client, callback_query: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        [
            [
                types.InlineKeyboardButton(text="Aᴅᴍɪɴ", callback_data="music_callback hb1"),
                types.InlineKeyboardButton(text="Aᴜᴛʜ", callback_data="music_callback hb2"),
                types.InlineKeyboardButton(
                    text="Bʀᴏᴀᴅᴄᴀsᴛ", callback_data="music_callback hb3"
                ),
            ],
            [
                types.InlineKeyboardButton(
                    text="Bʟ-Cʜᴀᴛ", callback_data="music_callback hb4"
                ),
                types.InlineKeyboardButton(
                    text="Bʟ-Usᴇʀ", callback_data="music_callback hb5"
                ),
                types.InlineKeyboardButton(text="C-Pʟᴀʏ", callback_data="music_callback hb6"),
            ],
            [
                types.InlineKeyboardButton(text="G-Bᴀɴ", callback_data="music_callback hb7"),
                types.InlineKeyboardButton(text="Lᴏᴏᴘ", callback_data="music_callback hb8"),
                types.InlineKeyboardButton(
                    text="Mᴀɪɴᴛᴇɴᴀɴᴄᴇ", callback_data="music_callback hb9"
                ),
            ],
            [
                types.InlineKeyboardButton(text="Pɪɴɢ", callback_data="music_callback hb10"),
                types.InlineKeyboardButton(text="Pʟᴀʏ", callback_data="music_callback hb11"),
                types.InlineKeyboardButton(
                    text="Sʜᴜғғʟᴇ", callback_data="music_callback hb12"
                ),
            ],
            [
                types.InlineKeyboardButton(text="Sᴇᴇᴋ", callback_data="music_callback hb13"),
                types.InlineKeyboardButton(text="Sᴏɴɢ", callback_data="music_callback hb14"),
                types.InlineKeyboardButton(text="Sᴘᴇᴇᴅ", callback_data="music_callback hb15"),
            ],
            [types.InlineKeyboardButton(text="✯ ʙᴀᴄᴋ ✯", callback_data=f"feature")],
        ]
    )

    await callback_query.message.edit(
        "Here are the music options...",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex("back_to_music"))
async def feature_callback(client, callback_query: CallbackQuery):
    keyboard = [
        [
            types.InlineKeyboardButton(
                text="💫 ᴀᴅᴅ ᴍᴇ ᴍᴏʀᴇ ❤️",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            types.InlineKeyboardButton(text="🎧 ᴍᴜsɪᴄ 🎧", callback_data="music"),
            types.InlineKeyboardButton(text="🤖 ᴍᴀɴᴇɢᴇᴍᴇɴᴛ 🤖", callback_data="settings_back_helper"),
        ],
        [types.InlineKeyboardButton(text="✯ ʜᴏᴍᴇ ✯", callback_data="go_to_start")],
    ]
    await callback_query.message.edit_text(
        "Here are the bot features...",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

@app.on_callback_query(filters.regex("music_callback") & ~BANNED_USERS)
@languageCB
async def music_helper_cb(client, CallbackQuery, _):

    callback_data = CallbackQuery.data.strip()

    cb = callback_data.split(None, 1)[1]

    keyboard = back_to_music(_)

    if cb == "hb1":

        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)

    elif cb == "hb2":

        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)

    elif cb == "hb3":

        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)

    elif cb == "hb4":

        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)

    elif cb == "hb5":

        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)

    elif cb == "hb6":

        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)

    elif cb == "hb7":

        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)

    elif cb == "hb8":

        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)

    elif cb == "hb9":

        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)

    elif cb == "hb10":

        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)

    elif cb == "hb11":

        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)

    elif cb == "hb12":

        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)

    elif cb == "hb13":

        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)

    elif cb == "hb14":

        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboard)

    elif cb == "hb15":

        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)
