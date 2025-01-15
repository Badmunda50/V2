import uvloop

uvloop.install()

from pyrogram import Client as PyrogramClient, errors
from pyrogram.enums import ChatMemberStatus, ParseMode
from telethon import TelegramClient

import config
from ..logging import LOGGER


class Aviax(PyrogramClient):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="AviaxMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            LOGGER(__name__).info(f"Attempting to send message to LOG_GROUP_ID: {config.LOG_GROUP_ID}")
            await self.send_message(
                chat_id=config.LOG_GROUP_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
            LOGGER(__name__).info(f"Message sent successfully to LOG_GROUP_ID: {config.LOG_GROUP_ID}")
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}.\nException: {ex}"
            )
            exit()

        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        LOGGER(__name__).info(f"Bot member status in the group: {a.status}")
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot as an admin in your log group/channel."
            )
            exit()
        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()


class Bad(TelegramClient):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Telethon Bot...")
        super().__init__(
            'telethon_session',
            api_id=config.API_ID,
            api_hash=config.API_HASH
        )

    async def start(self):
        await super().start(bot_token=config.BOT_TOKEN)
        me = await self.get_me()
        self.id = me.id
        self.name = me.first_name + " " + (me.last_name or "")
        self.username = me.username
        self.mention = f"@{self.username}"

        try:
            LOGGER(__name__).info(f"Attempting to send message to LOG_GROUP_ID: {config.LOG_GROUP_ID}")
            await self.send_message(
                config.LOG_GROUP_ID,
                f"» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ2 :\n\nɪᴅ : {self.id}\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
            )
            LOGGER(__name__).info(f"Message sent successfully to LOG_GROUP_ID: {config.LOG_GROUP_ID}")
        except Exception as ex:
            LOGGER(__name__).error(
                f"Telethon Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}.\nException: {ex}"
            )
            exit()
        LOGGER(__name__).info(f"Telethon Bot Started as {self.name}")

    async def stop(self):
        await super().stop()


async def main():
    telethon_bot = Bad()
    await telethon_bot.start()
    
    pyrogram_bot = Aviax()
    await pyrogram_bot.start()

import asyncio
asyncio.run(main())
