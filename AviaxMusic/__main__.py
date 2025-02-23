import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
from telethon import TelegramClient

import config
from AviaxMusic import LOGGER, HELPABLE, app, userbot, Bad, application
from AviaxMusic.core.call import Aviax
from AviaxMusic.misc import sudo
from AviaxMusic.plugins import ALL_MODULES
from AviaxMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    LOGGER("AviaxMusic.plugins").info("Successfully Imported All Modules ")
    await Aviax.start()
    await Bad.start()
    await application.run_polling()
    await application.start()
    await userbot.start()   
    try:
        await Aviax.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AviaxMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Aviax.decorators()
    LOGGER("AviaxMusic").info(
        "bot start")
    await idle()
    await app.stop()
    await Bad.disconnect()
    await application.shutdown()  # Call shutdown method on the instance
    await userbot.stop()
    LOGGER("AviaxMusic").info("Stopping Aviax Music Bot...")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
