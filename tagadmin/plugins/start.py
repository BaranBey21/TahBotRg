from pyrogram import Client, filters
from pyrogram.types import Message
from tagadmin import COMMAND_HAND_LER

# -- Constants -- #
START_TEXT = """
Selam {}
Ben sadece.@{}, Tüm Yöneticileri Etiketlemek için basit bir bot'um\
yazarak kolayca gruplandırma @admin or @admins
/help - Show help message
❤️ kaynak kodu - [Github](https://github.com/desvelad/TahBotRg)
__**Türkiye ❤️ için yapılmıştır**__
"""

HELP_TEXT = f"""
{COMMAND_HAND_LER}start - Başlangıç iletisini göster.
{COMMAND_HAND_LER}help - Bu yardım iletisini denetle.
{COMMAND_HAND_LER}donate - Sahibimi bağışlama hakkında bilgi alın.
@admin / @admins - Tag All the admins
"""
# -- Sabitler Bitişi -- #


@Client.on_message(filters.command("help", COMMAND_HAND_LER))
async def help_bot(c: Client, m: Message):

    await m.reply_text(
        HELP_TEXT, parse_mode="markdown", reply_to_message_id=m.message_id
    )
    return


@Client.on_message(filters.command("start", COMMAND_HAND_LER))
async def start_bot(c: Client, m: Message):

    user = m.from_user.first_name
    bot = await c.get_me()

    await m.reply_text(
        START_TEXT.format(user, bot.username),
        disable_web_page_preview=True,
        reply_to_message_id=m.message_id,
        parse_mode="markdown",
    )
    return