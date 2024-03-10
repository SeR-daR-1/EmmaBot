from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AnonXMusic import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/zc_cw":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("zc_cw", msg.from_user.id)
            verification_status = "تم التحقق من الاشتراك في القناة ✅"
        except UserNotParticipant:
            verification_status = "لم يتم التحقق من الاشتراك في القناة ❌"
            if "https://t.me/zc_cw".isalpha():
                link = "https://t.me/zc_cw"
            else:
                chat_info = await bot.get_chat("zc_cw")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n⌯︙{verification_status}",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("التحقق من الاشتراك", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN : @cczza")
