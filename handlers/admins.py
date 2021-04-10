from pyrogram import Client
from pyrogram.types import Message

from helpers.filters import command
from helpers.decorators import errors, full_users_only, super_users_only, group_users_only
from helpers.db import DBHandler, AdminType

dbhd = DBHandler()


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


@Client.on_message(command(["ban"]))
@errors
@full_users_only
async def banuser(client, message: Message):
    user_id = 0
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await dbhd.set_admtype(user_id, AdminType.BAN.value, message.chat.id)
        await client.send_message(message.chat.id, f"@{message.reply_to_message.from_user.username} is banned now")
    else:
        user_tags = message.text.replace("@", "").split(" ")
        user_tags.pop(0)
        for user in await client.get_users(user_tags):
            await dbhd.set_admtype(user.id, AdminType.BAN.value, message.chat.id)
            await client.send_message(message.chat.id, f"@{user.username} is banned now")


@Client.on_message(command(["unban"]))
@errors
@full_users_only
async def removeban(client, message: Message):
    user_id = 0
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await dbhd.set_admtype(user_id, AdminType.NOT_ADMIN.value, message.chat.id)
        await client.send_message(message.chat.id, f"@{message.reply_to_message.from_user.username} isn't banned now")
    else:
        user_tags = message.text.replace("@", "").split(" ")
        user_tags.pop(0)
        for user in await client.get_users(user_tags):
            await dbhd.set_admtype(user.id, AdminType.NOT_ADMIN.value, message.chat.id)
            await client.send_message(message.chat.id, f"@{user.username} isn't banned now")


@Client.on_message(command(["global_ban", "gban"]))
@errors
@super_users_only
async def gbanuser(client, message: Message):
    user_id = 0
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await dbhd.set_admtype(user_id, AdminType.GBAN.value, 0)
        await client.send_message(message.chat.id, f"@{message.reply_to_message.from_user.username} is global banned now")
    else:
        user_tags = message.text.replace("@", "").split(" ")
        user_tags.pop(0)
        for user in await client.get_users(user_tags):
            await dbhd.set_admtype(user.id, AdminType.GBAN.value, 0)
            await client.send_message(message.chat.id, f"@{user.username} is global banned now")


@Client.on_message(command(["global_unban", "gunban"]))
@errors
@super_users_only
async def gunbanuser(client: Client, message: Message):
    user_id = 0
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await dbhd.set_admtype(user_id, AdminType.NOT_ADMIN.value, 0)
        await client.send_message(message.chat.id, f"@{message.reply_to_message.from_user.username} isn't global banned now")
    else:
        user_tags = message.text.replace("@", "").split(" ")
        user_tags.pop(0)
        for user in await client.get_users(user_tags):
            await dbhd.set_admtype(user.id, AdminType.NOT_ADMIN.value, 0)
            await client.send_message(message.chat.id, f"@{user.username} isn't global banned now")


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
