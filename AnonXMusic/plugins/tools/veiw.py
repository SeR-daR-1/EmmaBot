from requests import Session
from requests import Response
from pyrogram import Client, filters
from pyrogram.types import Message
from asyncio import sleep
from AnonXMusic import app
s = Session()

@app.on_message(filters.command("رشق", ""))
async def receiver(_: Client,  message: Message) -> None:
    data = message.text.split(maxsplit=1)
    if len(data) == 1: return await message.reply("- ارسل الرابط مع الأمر", reply_to_message_id=message.id)
    url = data[-1]
    response = views(url)
    if response: await message.reply("- تم رشق المشاهدات بنجاح", reply_to_message_id=message.id)
    else: await message.reply("- حدث خطأ أثناء الرشق،", reply_to_message_id=message.id)

def views(tgurl: str) -> bool:
    params: dict = {
        "jack" : tgurl
    }
    url: str = "https://ava-tar.online/api/kro" # API owner: @uu4uo
    response: Response = s.get(url, params=params).json()
    return True if "تم الرشق بنجاح" in response["text"] else False
