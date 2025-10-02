import asyncio

from core.init_bot import(
    bot,
    dp,
    set_bot_commands,
    session
)

from utils.logger import get_logger, setup_logging
import middlewares
import handlers


setup_logging()
log = get_logger("app")


async def main():
    dp.message.outer_middleware(middlewares.msg_mw())
    dp.callback_query.outer_middleware(middlewares.call_mw())
    dp.include_routers(*handlers.handlers)

    await set_bot_commands()

    me = await bot.get_me()
    log.info(f"Started @{me.username}")

    try:
        await dp.start_polling(bot)
    finally:
        await session.close()
        # await redis_client.close()
        log.info("Shutdown complete")


if __name__ == "__main__":
    asyncio.run(main())