from typing import Callable

from pyrogram import Client
from pyrogram.types import Message

from helpers.admins import get_administrators
from config import SUDO_USERS
from helpers.db import DBHandler, AdminType
from pyrogram.types import CallbackQuery

dbhd = DBHandler()


def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f"❗️ {type(e).__name__}: {e}")

    return decorator


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message):
        m = None
        if isinstance(message, CallbackQuery):
            m = message.message
        else:
            m = message
        user_id = m.from_user.id
        group_id = m.chat.id
        allowed = await dbhd.get_allowed(group_id)

        if user_id in SUDO_USERS or await dbhd.get_admin_type(user_id) < AdminType.GROUP.value or await dbhd.get_admin_type(user_id, group_id) == AdminType.GROUP.value:
            return await func(client, message)

        if allowed['all'] == 1 and await dbhd.get_admin_type(user_id) < AdminType.BAN.value and await dbhd.get_admin_type(user_id, group_id) < AdminType.BAN.value:
            return await func(client, message)

        if allowed['admin'] == 1 and await dbhd.get_admin_type(user_id) < AdminType.BAN.value and await dbhd.get_admin_type(user_id, group_id) < AdminType.BAN.value:
            administrators = await get_administrators(message.chat)
            for administrator in administrators:
                if administrator == message.from_user.id:
                    return await func(client, message)

    return decorator


def group_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        user_id = message.from_user.id
        if user_id in SUDO_USERS or await dbhd.get_admin_type(user_id) < AdminType.GROUP.value or await dbhd.get_admin_type(user_id, message.chat.id) < AdminType.NOT_ADMIN.value:
            return await func(client, message)

    return decorator


def super_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        user_id = message.from_user.id
        if user_id in SUDO_USERS or await dbhd.get_admin_type(user_id) == AdminType.SUPER.value:
            return await func(client, message)

    return decorator


def full_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        user_id = message.from_user.id
        if user_id in SUDO_USERS or await dbhd.get_admin_type(user_id) < AdminType.GROUP.value:
            return await func(client, message)

    return decorator
