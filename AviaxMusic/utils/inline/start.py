from pyrogram.types import InlineKeyboardButton

import config
from AviaxMusic import app

from typing import Union


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons



def private_panel(OWNER: Union[bool, int] = None):
    buttons = [
       [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users",
            ),
        ], 
        [
            InlineKeyboardButton(
                text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs", callback_data="feature"
            ),
        ],
      [
            InlineKeyboardButton(
               text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", 
               user_id=OWNER,
                    ),
          InlineKeyboardButton(
               text="ᴏᴡɴᴇʀ", 
               url=f"https://t.me/itzYuva",
                    ),
      ],
          [
           InlineKeyboardButton(
               text="sᴜᴘᴘᴏʀᴛ",
               url=f"https://t.me/Sigma_Rulez"
           ),
        ],
    
]
    return buttons

