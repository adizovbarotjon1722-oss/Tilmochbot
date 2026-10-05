"""Tilmoch — Xitoy · Ingliz · Rus tarjimon (Telegram bot)."""
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from app import config, ocr, scheduler, speech
from app.db import db
from app.handlers import routers
from app.middlewares import SubscriptionMiddleware, UserMiddleware, on_error
from app.translator import translator

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("bot")

COMMANDS = [
    ("start", "Boshlash"),
    ("mode", "Tarjima rejimi"),
    ("iboralar", "Biznes va sayohat iboralari"),
    ("lugat", "Shaxsiy lug'at"),
    ("test", "So'z testi"),
    ("history", "Oxirgi tarjimalar"),
    ("saved", "Saqlanganlar"),
    ("premium", "Premium tariflar"),
    ("referal", "Do'st taklif qilish"),
    ("settings", "Sozlamalar"),
    ("uz", "O'zbekchaga tarjima"),
    ("en", "Inglizchaga tarjima"),
    ("zh", "Xitoychaga tarjima"),
    ("ru", "Ruschaga tarjima"),
    ("tr", "Guruhda tarjima"),
    ("help", "Yordam"),
]

# Start tugmasidan OLDIN ko'rinadigan matn — eng muhim reklama joyi (512 belgigacha)
DESCRIPTION = (
    "🇨🇳 Xitoylik sotuvchi bilan tilni bilmasdan gaplashing!\n\n"
    "🎙 O'zbekcha gapiring — Tilmoch xitoychaga tarjima qilib, ovoz bilan qaytaradi\n"
    "📷 Narx varag'ini rasmga oling — darhol o'zbekchada\n"
    "📄 Invoys va shartnomalar — Word/PDF holida\n"
    "📖 64 ta tayyor biznes ibora: narx, buyurtma, yetkazish\n\n"
    "🇺🇿 O'zbek · 🇨🇳 Xitoy · 🇬🇧 Ingliz · 🇷🇺 Rus\n"
    "🎁 Yangi foydalanuvchilarga 3 kun Premium sovg'a"
)
# Profil va ulashilganda ko'rinadigan qisqa tavsif (120 belgigacha)
SHORT = "Xitoylik hamkor bilan tilni bilmasdan gaplashing: ovoz, rasm, hujjat tarjimasi 🇺🇿🇨🇳🇬🇧🇷🇺"


async def setup_profile(bot: Bot):
    """BotFather'dagi tavsif va buyruqlarni avtomatik o'rnatadi."""
    try:
        await bot.set_my_commands([BotCommand(command=c, description=d) for c, d in COMMANDS])
        if (await bot.get_my_name()).name != config.BOT_NAME:
            await bot.set_my_name(config.BOT_NAME)
        await bot.set_my_description(DESCRIPTION)
        await bot.set_my_short_description(SHORT)
    except Exception as e:
        log.warning("Profilni sozlashda xato: %s", e)


async def main():
    if not config.BOT_TOKEN:
        sys.exit("BOT_TOKEN topilmadi. .env faylini to'ldiring (.env.example dan nusxa oling).")

    await db.connect()
    await translator.start()

    bot = Bot(config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.update.outer_middleware(UserMiddleware())
    dp.message.middleware(SubscriptionMiddleware())
    dp.callback_query.middleware(SubscriptionMiddleware())
    dp.errors.register(on_error)
    for r in routers:
        dp.include_router(r)

    await setup_profile(bot)
    me = await bot.me()
    log.info(
        "Bot ishga tushdi: @%s | AI tarjima: %s | Ovoz: %s | ffmpeg: %s | OCR: %s | To'lov: Stars%s | Kanal: %s",
        me.username, "yoqilgan" if config.LLM_API_KEY else "Google",
        "Whisper" if config.STT_API_KEY else "Google (bepul)",
        "bor" if speech.FFMPEG else "YO'Q — ovozli tarjima ishlamaydi!",
        "AI+Tesseract" if config.LLM_API_KEY else ("Tesseract" if ocr.TESSERACT else "YO'Q"),
        " + Click/Payme" if config.PAYMENT_PROVIDER_TOKEN else "",
        config.REQUIRED_CHANNEL or "—",
    )

    task = asyncio.create_task(scheduler.run(bot))
    try:
        await bot.delete_webhook(drop_pending_updates=False)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        task.cancel()
        await translator.close()
        await db.close()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
