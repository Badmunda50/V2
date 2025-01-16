from enum import Enum, auto
from telethon import Button, events
from AviaxMusic import Bad as app
from AviaxMusic.utils.msg_types import button_markdown_parser
from AviaxMusic.utils.notes_func import NoteFillings
from emojis import decode


async def SendFilterMessage(event, filter_name: str, content: str, text: str, data_type: int):
    chat_id = event.chat_id
    message_id = event.id
    text, buttons = button_markdown_parser(text)

    text = await NoteFillings(event.message, text)
    reply_markup = None
    if len(buttons) > 0:
        reply_markup = event.client.build_reply_markup(buttons)
    else:
        reply_markup = None

    if data_type == 1:
        await event.client.send_message(
            chat_id=chat_id,
            message=text,
            buttons=reply_markup,
            reply_to=message_id
        )

    elif data_type == 2:
        await event.client.send_file(
            chat_id=chat_id,
            file=content,
            buttons=reply_markup,
            reply_to=message_id
        )

    elif data_type == 3:
        await event.client.send_file(
            chat_id=chat_id,
            file=content,
            buttons=reply_markup,
            reply_to=message_id
        )

    elif data_type == 4:
        await event.client.send_file(
            chat_id=chat_id,
            file=content,
            caption=text,
            buttons=reply_markup,
            reply_to=message_id
        )

    elif data_type == 5:
        await event.client.send_file(
            chat_id=chat_id,
            file=content,
            caption=text,
            buttons=reply_markup,
            reply_to=message_id
        )

    elif data_type == 6:
        await event.client.send_file(
            chat_id=chat_id,
            file=content,
            caption=text,
            buttons=reply_markup,
            reply_to=message_id
        )

    elif data_type == 7:
        await event.client.send_file(
            chat_id=chat_id,
            file=content,
            caption=text,
            buttons=reply_markup,
            reply_to=message_id
        )

    elif data_type == 8:
        await event.client.send_file(
            chat_id=chat_id,
            file=content,
            caption=text,
            buttons=reply_markup,
            reply_to=message_id
        )

    elif data_type == 9:
        await event.client.send_file(
            chat_id=chat_id,
            file=content,
            buttons=reply_markup,
            reply_to=message_id
        )


class FilterMessageTypeMap(Enum):
    text = auto()
    sticker = auto()
    animation= auto()
    document = auto()
    photo = auto()
    audio = auto()
    voice = auto()
    video = auto()
    video_note = auto()

async def GetFIlterMessage(event):
    data_type = None
    content = None
    text = str()

    raw_text = event.message.text or event.message.caption
    args = raw_text.split(None, 2)

    if len(args) >= 3 and not event.message.is_reply:
        text = event.message.text.markdown[len(event.message.command[0]) + len(event.message.command[1]) + 4 :]
        data_type = FilterMessageTypeMap.text.value

    if (
        event.message.is_reply
        and event.message.reply_message.text
    ):
        if len(args) >= 2:
            text = event.message.reply_message.text.markdown
            data_type = FilterMessageTypeMap.text.value

    elif (
        event.message.is_reply
        and event.message.reply_message.sticker
    ):
        content = event.message.reply_message.sticker.file_id
        data_type = FilterMessageTypeMap.sticker.value

    elif (
        event.message.is_reply
        and event.message.reply_message.animation
    ):
        content = event.message.reply_message.animation.file_id
        if event.message.reply_message.caption:
            text = event.message.reply_message.caption.markdown
        data_type = FilterMessageTypeMap.animation.value

    elif (
        event.message.is_reply
        and event.message.reply_message.document
    ):
        content = event.message.reply_message.document.file_id
        if event.message.reply_message.caption: 
            text = event.message.reply_message.caption.markdown 
        data_type = FilterMessageTypeMap.document.value

    elif (
        event.message.is_reply
        and event.message.reply_message.photo
    ):
        content = event.message.reply_message.photo.file_id
        if event.message.reply_message.caption:
            text = event.message.reply_message.caption.markdown
        data_type = FilterMessageTypeMap.photo.value

    elif (
        event.message.is_reply
        and event.message.reply_message.audio
    ):
        content = event.message.reply_message.audio.file_id
        if event.message.reply_message.caption:
            text = event.message.reply_message.caption.markdown 
        data_type = FilterMessageTypeMap.audio.value

    elif (
        event.message.is_reply
        and event.message.reply_message.voice
    ):
        content = event.message.reply_message.voice.file_id
        if event.message.reply_message.caption:
            text = event.message.reply_message.caption.markdown
        data_type = FilterMessageTypeMap.voice.value

    elif (
        event.message.is_reply
        and event.message.reply_message.video
    ):
        content = event.message.reply_message.video.file_id 
        if event.message.reply_message.caption:
            text = event.message.reply_message.caption.markdown 
        data_type= FilterMessageTypeMap.video.value

    elif (
        event.message.is_reply
        and event.message.reply_message.video_note
    ):
        content = event.message.reply_message.video_note.file_id
        text = None 
        data_type = FilterMessageTypeMap.video_note.value

    return (
        content,
        text,
        data_type
    )

def get_text_reason(event) -> str:
    """This function returns text, and the reason of the user's arguments

    Args:
        event (Message): Message

    Returns:
        [str]: text, reason
    """
    text = decode(event.text)
    index_finder = [x for x in range(len(text)) if text[x] == '"']
    if len(index_finder) >= 2:
        text = text[index_finder[0]+1: index_finder[1]]
        reason = text[index_finder[1] + 2:]
        if not reason:
            reason = None
    else:
        text = event.command[1]
        reason = ' '.join(event.command[2:])
        if not reason:
            reason = None

    return (
        text,
        reason
    )
