from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command
# from helpers.decorators import authorized_users_only


@Client.on_message(command(["start", f"start@{BOT_USERNAME}]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am MusiCeros, an open-source bot that lets you play music in your groups.

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Source code", url="to be updated"
                    )
                ],
            ]
        )
    )
