import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait, UserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram.types import InlineKeyboardMarkup
from fsub import *
from fsub.database.data import *
# Pastikan is_fsubs, decode, get_messages, start_button, fsub_button sudah di-import lewat 'from fsub import *' atau panggil manual di sini

# ==================== 1. JALUR USER SUDAH JOIN ====================
@Bot.on_message(filters.command("start") & filters.private & is_fsubs)
async def start_command(client, message):
    user_id = message.from_user.id
    if not await present_user(user_id):
        try:
            await add_user(user_id)
        except:
            pass
            
    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except BaseException:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except Exception:
                return
            if start <= end:
                ids = range(start, end + 1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except Exception:
                return
        temp_msg = await message.reply("<code>Tunggu Sebentar...</code>")
        try:
            messages = await get_messages(client, ids)
        except Exception:
            await message.reply_text("<b>Telah Terjadi Error </b>🥺")
            return
        await temp_msg.delete()

        # Ambil ID bot untuk pengecekan setting ke database
        bot_id = client.me.id if client.me else (await client.get_me()).id

        for msg in messages:
            cust = await caption_info(bot_id)
            if bool(cust) and bool(msg.document):
                caption = cust.format(
                    previouscaption=msg.caption.html if msg.caption else "",
                    filename=msg.document.file_name,
                )
            else:
                caption = msg.caption.html if msg.caption else ""
                
            dd = await disable_info(bot_id)
            anti = await anti_info(bot_id)
            reply_markup = msg.reply_markup if dd else None
            try:
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    protect_content=anti,
                    reply_markup=reply_markup,
                )
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    protect_content=anti,
                    reply_markup=reply_markup,
                )
            except (PeerIdInvalid, UserIsBlocked):
                return
            except Exception:
                pass
    else:
        out = await start_button(client)
        await message.reply_text(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=f"@{message.from_user.username}"
                if message.from_user.username
                else None,
                mention=message.from_user.mention,
                id=message.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(out),
            disable_web_page_preview=True,
            quote=True,
        )
    return


# ==================== 2. JALUR USER BELUM JOIN (DIKUNCI) ====================
# Ditambahkan ~is_fsubs (artinya: TIDAK / BELUM memenuhi kriteria join channel)
@Bot.on_message(filters.command("start") & filters.private & ~is_fsubs)
async def not_joined(client, message):
    buttons = await fsub_button(client, message)
    await message.reply(
        text=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=f"@{message.from_user.username}"
            if message.from_user.username
            else None,
            mention=message.from_user.mention,
            id=message.from_user.id,
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True,
    )
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except Exception:
                return
        temp_msg = await message.reply("<code>Tunggu Sebentar...</code>")
        try:
            messages = await get_messages(client, ids)
        except Exception:
            await message.reply_text("<b>Telah Terjadi Error </b>🥺")
            return
        await temp_msg.delete()

        for msg in messages:
            cust = await caption_info(client.me.id)
            if bool(cust) & bool(msg.document):
                caption = cust.format(
                    previouscaption=msg.caption.html if msg.caption else "",
                    filename=msg.document.file_name,
                )

            else:
                caption = msg.caption.html if msg.caption else ""
            dd = await disable_info(client.me.id)
            anti = await anti_info(client.me.id)
            reply_markup = msg.reply_markup if dd else None
            try:
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    protect_content=anti,
                    reply_markup=reply_markup,
                )
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    protect_content=anti,
                    reply_markup=reply_markup,
                )
            except (PeerIdInvalid, UserIsBlocked):
                return
            except Exception:
                pass
    else:
        out = await start_button(client)
        await message.reply_text(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=f"@{message.from_user.username}"
                if message.from_user.username
                else None,
                mention=message.from_user.mention,
                id=message.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(out),
            disable_web_page_preview=True,
            quote=True,
        )


    return


@Bot.on_message(filters.command("start") & filters.private)
async def not_joined(client, message):
    buttons = await fsub_button(client, message)
    await message.reply(
        text=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=f"@{message.from_user.username}"
            if message.from_user.username
            else None,
            mention=message.from_user.mention,
            id=message.from_user.id,
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True,
    )


