from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command
from helpers.decorators import authorized_users_only


@Client.on_message(command("start"))
@authorized_users_only
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am Calls Music, an open-source bot that lets you play music in your groups.

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Source code", url="https://github.com/callsmusic/callsmusic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/callsmusicchat"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/callsmusic"
                    )
                ]
            ]
        )
    )


# @Client.on_message(command("start") & other_filters)
# async def start2(_, message: Message):
#     await message.reply_text(
#         "💁🏻‍♂️ Do you want to search for a YouTube video?",
#         reply_markup=InlineKeyboardMarkup(
#             [
#                 [
#                     InlineKeyboardButton(
#                         "✅ Yes", switch_inline_query_current_chat=""
#                     ),
#                     InlineKeyboardButton(
#                         "No ❌", callback_data="close"
#                     )
#                 ]
#             ]
#         )
#     )
