import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from AnshiRobot import telethn as bot,BOT_NAME
from AnshiRobot import telethn as tgbot
from AnshiRobot.events import register

edit_time = 5
f""" ======================={BOT_NAME}====================== """
file1 = "https://files.catbox.moe/bz6ud1.jpg"
file2 = "https://files.catbox.moe/3oteb5.jpg"
file3 = "https://files.catbox.moe/gnl6ia.jpg"
file4 = "https://files.catbox.moe/1qxnxj.jpg"
file5 = "https://files.catbox.moe/49llcm.jpg"
""" ======================={BOT_NAME}====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("ɪɴғᴏʀᴍᴀᴛɪᴏɴ", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"⬤ ʜᴇʏ {firstname} ♥︎\n\n● ᴄʟɪᴄᴋ ᴏɴ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴀʙᴏᴜᴛ ʏᴏᴜ",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE += f"● ғɪʀsᴛ ɴᴀᴍᴇ ➥ {PRO.first_name} \n"
        LILIE += f"● ʟᴀsᴛ ɴᴀᴍᴇ ➥ {PRO.last_name}\n"
        LILIE += f"● ʏᴏᴜ ʙᴏᴛ ➥ {PRO.bot} \n"
        LILIE += f"● ʀᴇsᴛʀɪᴄᴛᴇᴅ ➥ {PRO.restricted} \n"
        LILIE += f"● ᴜsᴇʀ ɪᴅ ➥ {boy}\n"
        LILIE += f"● ᴜsᴇʀɴᴀᴍᴇ ➥ @{PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")
        
        
__mod_name__ = "˹ᴍʏɪɴғᴏ˼"

__help__ = """

 ⬤ /myinfo ➥ ᴄʜᴋ ᴏᴡɴ ɪɴғᴏʀᴍᴀᴛɪᴏɴ
 """

__command_list__ = ["myinfo"]

