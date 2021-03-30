from asyncio import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

from callsmusic import callsmusic, queues
import asyncio
from helpers.filters import command
from helpers.decorators import errors, authorized_users_only, full_users_only, super_users_only, group_users_only
from helpers.player import play_song
from helpers.db import DBHandler, AdminType

dbhd = DBHandler()


@Client.on_message(command(["pause", "p"]))
@errors
@authorized_users_only
async def pause(_, message: Message):
    if callsmusic.pause(message.chat.id):
        await message.reply_text("⏸ Paused")
    else:
        await message.reply_text("❗️ Nothing is playing")


@Client.on_message(command(["resume", "r"]))
@errors
@authorized_users_only
async def resume(_, message: Message):
    if callsmusic.resume(message.chat.id):
        await message.reply_text("🎧 Resumed")
    else:
        await message.reply_text("❗️ Nothing is paused")


@Client.on_message(command(["stop", "s"]))
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("❗️ Nothing is playing")
    else:
        try:
            queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        await callsmusic.stop(message.chat.id)
        await message.reply_text("✅ Cleared the queue and left the call")


@Client.on_message(command(["skip", "f"]))
@errors
@authorized_users_only
async def skip(client, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("❗️ Nothing is playing")
    else:
        queues.task_done(message.chat.id)
        chat_id = message.chat.id
        try:
            await callsmusic.cover_message[chat_id].delete()
        except:
            print('deleted')

        if queues.is_empty(message.chat.id):
            await callsmusic.stop(message.chat.id)
            m = await client.send_message(message.chat.id, "Done")
            await asyncio.sleep(3)
            await m.delete()
        else:
            song = queues.get(message.chat.id)
            input_filename = None
            m = await client.send_message(chat_id, "🔄 Processing...")
            if "file" in song.keys():
                input_filename = song["file"]
            await play_song(client, m, song, song["requested_by"], file=input_filename, force=True)
            await m.delete()

        sk = await message.reply_text("Skipped.")
        await asyncio.sleep(3)
        await sk.delete()


@Client.on_message(command(["mute", "m"]))
@errors
@authorized_users_only
async def mute(_, message: Message):
    result = callsmusic.mute(message.chat.id)

    if result == 0:
        await message.reply_text("🔇 Muted")
    elif result == 1:
        await message.reply_text("🔇 Already muted")
    elif result == 2:
        await message.reply_text("❗️ Not in voice chat")


@Client.on_message(command(["unmute", "u"]))
@errors
@authorized_users_only
async def unmute(_, message: Message):
    result = callsmusic.unmute(message.chat.id)

    if result == 0:
        await message.reply_text("🔈 Unmuted")
    elif result == 1:
        await message.reply_text("🔈 Already unmuted")
    elif result == 2:
        await message.reply_text("❗️ Not in voice chat")


@Client.on_message(command(["list", "l"]))
@authorized_users_only
async def listq(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("❕ Nothing is streaming.")
    else:
        await message.reply_text("**Queue**\n\n" + queues.qlist(message.chat.id))


@Client.on_message(command(["admin", "ad"]))
@errors
@full_users_only
async def addadmin(client, message: Message):
    user_id = 0
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await dbhd.set_admtype(user_id, AdminType.GROUP.value, message.chat.id)
        await client.send_message(message.chat.id, f"@{message.reply_to_message.from_user.username} is admin now")
    else:
        user_tags = message.text.replace("@", "").split(" ")
        user_tags.pop(0)
        for user in await client.get_users(user_tags):
            await dbhd.set_admtype(user.id, AdminType.GROUP.value, message.chat.id)
            await client.send_message(message.chat.id, f"@{user.username} is admin now")


@Client.on_message(command(["remove_admin", "rad"]))
@errors
@full_users_only
async def removeadmin(client, message: Message):
    user_id = 0
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await dbhd.set_admtype(user_id, AdminType.NOT_ADMIN.value, message.chat.id)
        await client.send_message(message.chat.id, f"@{message.reply_to_message.from_user.username} isn't admin now")
    else:
        user_tags = message.text.replace("@", "").split(" ")
        user_tags.pop(0)
        for user in await client.get_users(user_tags):
            await dbhd.set_admtype(user.id, AdminType.NOT_ADMIN.value, message.chat.id)
            await client.send_message(message.chat.id, f"@{user.username} isn't admin now")


@Client.on_message(command(["global_admin", "gad"]))
@errors
@super_users_only
async def addgadmin(client, message: Message):
    user_id = 0
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await dbhd.set_admtype(user_id, AdminType.FULL.value, 0)
        await client.send_message(message.chat.id, f"@{message.reply_to_message.from_user.username} is global admin now")
    else:
        user_tags = message.text.replace("@", "").split(" ")
        user_tags.pop(0)
        for user in await client.get_users(user_tags):
            await dbhd.set_admtype(user.id, AdminType.FULL.value, 0)
            await client.send_message(message.chat.id, f"@{user.username} is global admin now")


@Client.on_message(command(["remove_global_admin", "rgad"]))
@errors
@super_users_only
async def removegadmin(client: Client, message: Message):
    user_id = 0
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await dbhd.set_admtype(user_id, AdminType.NOT_ADMIN.value, 0)
        await client.send_message(message.chat.id, f"@{message.reply_to_message.from_user.username} isn't global admin now")
    else:
        user_tags = message.text.replace("@", "").split(" ")
        user_tags.pop(0)
        for user in await client.get_users(user_tags):
            await dbhd.set_admtype(user.id, AdminType.NOT_ADMIN.value, 0)
            await client.send_message(message.chat.id, f"@{user.username} isn't global admin now")


@Client.on_message(command(["allow_all"]))
@errors
@group_users_only
async def allowall(client: Client, message: Message):
    await dbhd.set_allowed(message.chat.id, allow_all=1)
    await client.send_message(message.chat.id, "All user are allowed to use MusiCeros commands")


@Client.on_message(command(["allow_admin"]))
@errors
@group_users_only
async def allowadmin(client: Client, message: Message):
    await dbhd.set_allowed(message.chat.id, allow_admins=1)
    await client.send_message(message.chat.id, "Group admin are allowed to use MusiCeros commands")


@Client.on_message(command(["disallow"]))
@errors
@group_users_only
async def disallow(client: Client, message: Message):
    await dbhd.set_allowed(message.chat.id, allow_all=0, allow_admins=0)
    await client.send_message(message.chat.id, "Only bot admins are allowed to use MusiCeros commands")
