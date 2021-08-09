import sys
import shutil
import psutil

from pyrogram import Client, filters
from helpers.functions import humanbytes
from config import BOT_USERNAME


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@Client.on_message(filters.command(["stats",f"stats@{BOT_USERNAME}"]))
async def stats(client, message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    await message.reply_text(
        text=f"**💫 Bot Stats Of Ani-Music 💫** \n\n**🤖 Bot Version:** `V2.9.1` \n\n**👥 Users:** \n ↳**PM'ed Users:** xyz \n\n**💾 Disk Usage,** \n ↳**Total Disk Space:** `{total}` \n ↳**Used:** `{used}({disk_usage}%)` \n ↳**Free:** `{free}` \n\n**🎛 Hardware Usage,** \n ↳**CPU Usage:** `{cpu_usage}%` \n ↳**RAM Usage:** `{ram_usage}%`",
        parse_mode="Markdown",
        quote=True
    )
    
 #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
