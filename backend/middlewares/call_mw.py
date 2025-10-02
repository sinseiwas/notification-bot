from aiogram import BaseMiddleware
from collections.abc import Awaitable, Callable
from typing import Any

from utils.logger import setup_logging, get_logger

from aiogram.types import CallbackQuery

setup_logging()
log = get_logger("app")


class Middleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, dict[str, Any]], Awaitable[Any]],
        callback: CallbackQuery,
        data: dict[str, Any],
    ) -> Any:
        try:
            result = await handler(callback, data)
            log.info(f"Message @{callback.data} by user: @{callback.from_user.username} handled")
            return await result
        except Exception as e:
            log.exception(f"Exception is: {e}")
