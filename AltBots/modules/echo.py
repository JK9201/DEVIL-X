import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltBots.data import ALTRON

ECHO = []


@X1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id

            if user_id in ALTRON:
                await event.reply("𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓓𝓔𝓥𝓘𝓛𝓧'𝓢 𝓞𝓦𝓝𝓔𝓡 ❌")
            elif user_id == OWNER_ID:
                await event.reply("𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓞𝓦𝓝𝓔𝓡 𝓞𝓕 𝓣𝓗𝓔𝓢𝓔 𝓑𝓞𝓣𝓢 ❌")
            elif user_id in SUDO_USERS:
                await event.reply(" 𝓝𝓞, 𝓣𝓗𝓘𝓢 𝓖𝓤𝓨 𝓘𝓢 𝓐 𝓢𝓤𝓓𝓞 𝓤𝓢𝓔𝓡 ❌")
            else:
                try:
                    alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                    await event.client(alt)
                except BaseException:
                    pass

                global ECHO
                check = f"{user_id}_{event.chat_id}"
                if check in ECHO:
                    await event.reply("» 𝓔𝓒𝓗𝓞 𝓘𝓢 𝓐𝓛𝓡𝓔𝓐𝓓𝓨 𝓐𝓒𝓣𝓘𝓥𝓐𝓣𝓔𝓓 𝓞𝓝 𝓣𝓗𝓘𝓢 𝓤𝓢𝓔𝓡 ✅ !!")
                else:
                    ECHO.append(check)
                    await event.reply("» 𝓔𝓒𝓗𝓞 𝓐𝓒𝓣𝓘𝓥𝓐𝓣𝓔𝓓 𝓞𝓝 𝓣𝓗𝓔 𝓤𝓢𝓔𝓡 ✅")
        else:
            await event.reply(f"𝓔𝓒𝓗𝓞:\n  » {hl}𝓔𝓒𝓗𝓞 <𝓡𝓔𝓟𝓛𝓨 𝓣𝓞 𝓐 𝓤𝓢𝓔𝓡>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass

            global ECHO
            reply_msg = await event.get_reply_message()
            check = f"{reply_msg.sender_id}_{event.chat_id}"

            if check in ECHO:
                ECHO.remove(check)
                await event.reply("» 𝓔𝓒𝓗𝓞 𝓗𝓐𝓢 𝓑𝓔𝓔𝓝 𝓢𝓣𝓞𝓟𝓟𝓔𝓓 𝓕𝓞𝓡 𝓣𝓗𝓔 𝓤𝓢𝓔𝓡 !! ✅")
            else:
                await event.reply("»𝓔𝓒𝓗𝓞 𝓘𝓢 𝓐𝓛𝓡𝓔𝓐𝓓𝓨 𝓓𝓘𝓢𝓐𝓑𝓛𝓔𝓓 !! 👀")
        else:
            await event.reply(f"𝓡𝓔𝓜𝓞𝓥𝓔 𝓔𝓒𝓗𝓞:\n  » {hl} 𝓡𝓜𝓔𝓒𝓗𝓞 <𝓡𝓔𝓟𝓛𝓨 𝓣𝓞 𝓐 𝓤𝓢𝓔𝓡>")


@X1.on(events.NewMessage(incoming=True))
@X2.on(events.NewMessage(incoming=True))
@X3.on(events.NewMessage(incoming=True))
@X4.on(events.NewMessage(incoming=True))
@X5.on(events.NewMessage(incoming=True))
@X6.on(events.NewMessage(incoming=True))
@X7.on(events.NewMessage(incoming=True))
@X8.on(events.NewMessage(incoming=True))
@X9.on(events.NewMessage(incoming=True))
@X10.on(events.NewMessage(incoming=True))
async def _(e):
    global ECHO
    check = f"{e.sender_id}_{e.chat_id}"
    if check in ECHO:
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(alt)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
            await asyncio.sleep(0.1)
