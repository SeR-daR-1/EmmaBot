from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AnonXMusic import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/+Dq8oYGQ7BBEzMjFk":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("https://t.me/+Dq8oYGQ7BBEzMjFk", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/+Dq8oYGQ7BBEzMjFk".isalpha():
                link = "https://t.me/+Dq8oYGQ7BBEzMjFk"
            else:
                chat_info = await bot.get_chat("https://t.me/+Dq8oYGQ7BBEzMjFk")
                link = chat_info.invite_link
            user_channel_info = await bot.get_chat(msg.from_user.id)
            user_channel_invite_link = await bot.export_chat_invite_link(user_channel_info.id)
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ! \n⌯︙قم بالانضمام إلى قناتك الخاصة من هنا: {user_channel_invite_link}",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("فَلسفة مشاعر .", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat @cczza !")
