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
                text="• ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ •",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users",
            ),
        ], 
        [
            InlineKeyboardButton(
                text="• ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs •", callback_data="gotohelp"
            ),
        ],
      [
            InlineKeyboardButton(
               text="• ᴅᴇᴠᴇʟᴏᴘᴇʀ •", 
               url=f"https://t.me/II_BAD_BABY_II",
                    ),
          InlineKeyboardButton(
               text="• ᴏᴡɴᴇʀ •", 
               url=f"https://t.me/II_BAD_BABY_II",
                    ),
      ],
          [
           InlineKeyboardButton(
               text="• ꜱᴜᴘᴘᴏʀᴛ •",
               url=f"https://t.me/PBX_CHAT"
           ),
        ],
    
]
    return buttons
    
