from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from AnonXMusic import app

admin, owner = ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER
muted = {}

@app.on_message(filters.command("كتم", "") & filters.group & filters.reply)
async def ktm(_: Client, message: Message):
    replied = message.reply_to_message
    user_id = message.from_user.id
    userB_id = replied.from_user.id
    chat_id = message.chat.id
    if userB_id in muted: return await message.reply("- هذا المستخدم مكتوم بالفعل!")
    member = await app.get_chat_member(chat_id, user_id)
    memberB = await app.get_chat_member(chat_id, userB_id)
    if user_id == userB_id: await message.reply("- لا يمكنك كتم نفسك.", reply_to_message_id=message.id)
    elif member.status == owner:
        if muted.get(str(chat_id)): muted[str(chat_id)].append(userB_id)
        else: muted[str(chat_id)] = [userB_id]
        await message.reply(f" ≭︰العضو ↫ ❲{replied.from_user.mention}❳\n≭︰تم كتمه")
    elif memberB.status in [admin, owner]: await message.reply("- لايمكنك كتم مشرف او مالك.", reply_to_message_id=message.id)
    elif member.status == admin:
        if muted.get(str(chat_id)): muted[str(chat_id)].append(userB_id)
        else: muted[str(chat_id)] = [userB_id]
        await message.reply(f"≭︰العضو ↫ ❲{replied.from_user.mention}❳\n≭︰تم كتمه")
    else: await message.reply("- يجب أن تكون ادمن في هذا الجروب على الاقل لتتمكن من كتم المستخدمين", reply_to_message_id=message.id)
        
        
@app.on_message(filters.command("الغاء الكتم", "") & filters.group & filters.reply)
async def unktm(_: Client, message: Message):
    replied = message.reply_to_message
    user_id = message.from_user.id
    userB_id = replied.from_user.id
    chat_id = message.chat.id
    member = await app.get_chat_member(chat_id, user_id)
    if member.status not in [admin, owner]:await message.reply("- يجب أن تكون ادمن في هذا الجروب على الاقل لتتمكن من استخدام هذا الامر.", reply_to_message_id=message.id)
    elif muted.get(str(chat_id)) is None: await message.reply("- لا يوجد أي مكتومين في هذه الدردشه.", reply_to_message_id=message.id)
    elif userB_id not in muted[str(chat_id)]: await message.reply("- هذا العضو لم يتم كتمه مسبقا.", reply_to_message_id=message.id)
    elif member.status in [admin, owner]:
        muted[str(chat_id)].remove(userB_id)
        await message.reply(f"≭︰العضو ↫ ❲{replied.from_user.mention}❳\n≭︰تم الغاء كتمه")


@app.on_message(filters.command("المكتومين", "") & filters.group)
async def maktom(_: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    member = await app.get_chat_member(chat_id, user_id)
    if member.status not in [admin, owner]:await message.reply("- يجب أن تكون ادمن في هذا الجروب على الاقل لتتمكن من استخدام هذا الامر.", reply_to_message_id=message.id)
    elif muted.get(str(chat_id)) is None: await message.reply("- لا يوجد أي مكتومين في هذه الدردشه.", reply_to_message_id=message.id)
    else: 
        names = "\n".join([f"- [{(await app.get_chat(id)).first_name}](tg://openmessage?user_id={id})" for id in muted[str(chat_id)]])
        caption = f"- قائمة الأشخاص المكتومين: \n\n{names}"
        await message.reply(caption, reply_to_message_id=message.id)


@app.on_message(filters.command("مسح المكتومين", "") & filters.group)
async def ms7maktom(_: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    member = await app.get_chat_member(chat_id, user_id)
    if member.status not in [admin, owner]:await message.reply("- يجب أن تكون ادمن في هذا الجروب على الاقل لتتمكن من استخدام هذا الامر.", reply_to_message_id=message.id)
    elif muted.get(str(chat_id)) is None: await message.reply("- لا يوجد أي مكتومين في هذه الدردشه.", reply_to_message_id=message.id)
    else:
        muted.clear()
        await message.reply("- تم مسح المكتومين.", reply_to_message_id=message.id)
    

@app.on_message(filters.text & filters.group & filters.bot, group=920)
@app.on_message(filters.text & filters.group, group=928)
async def ktmf(_: Client, message: Message):
    print(muted)
    if muted.get(str(message.chat.id)) is None: pass
    elif message.from_user.id in muted[str(message.chat.id)]:
        try:await message.delete()
        except:await message.reply(f"- عزيزي المالك لم استطع كتم المستخدام {message.from_user.mention} لعدم حصولي على صلاحية حذف الرسائل")

# 𝗪𝗥𝗜𝗧𝗧𝗘𝗡 𝗕𝗬 : @BENN_DEV
# 𝗦𝗢𝗨𝗥𝗖𝗘 : @BENfiles
      
