from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hii Guys! {message.from_user.first_name}!</b>

Aku Pemutar Musik!, Aku Akan Mutar Musik Di-Grup Kamu!.

Apabila Ingin Menggunakan Aku, Masukin Aku Ke Grup Dulu, Sama Assistennya, Kalau Kurang Lengkap Bisa Klik Dibawah Ini Kotak-Kotak!.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🐣 Owner Music!", url="https://t.me/afterdaytoxic"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/humangabutguys"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/captionanakmuda"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
