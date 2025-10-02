from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TEST, PRODUCTION
from aiogram.client.default import DefaultBotProperties

from core.config import settings


session = AiohttpSession(api=TEST if settings.IS_TEST == True else PRODUCTION)


bot = Bot(
    token=settings.BOT_TOKEN,
    session=session,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

dp = Dispatcher()

async def set_bot_commands():
    commands = [
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="notificate", description="Отправить уведомление на ПК"),
        BotCommand(command="get_my_id", description="Получить свой Chat ID")
    ]
    
    await bot.set_my_commands(commands)