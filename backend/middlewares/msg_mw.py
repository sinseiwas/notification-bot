from collections.abc import Callable, Awaitable
from typing import Any

from utils.logger import setup_logging, get_logger

from aiogram import BaseMiddleware
from aiogram.types import Message

setup_logging()
log = get_logger("app")


class Middleware(BaseMiddleware):
    album_data: dict[str, list] = {}

    def __init__(self, latency: int | float = 1):
        self.latency = latency

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        msg: Message,
        data: dict[str, Any],
    ) -> Any:
        try:
            result = await handler(msg, data)
            log.info(f"Message @{msg.text} by user: @{msg.from_user.username} handled")
            return result
        except Exception as e:
            log.exception(f"Exception is: {e}")
