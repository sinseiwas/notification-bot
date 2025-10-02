from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start_cmd(msg: Message):
    await msg.answer("Bot is working")


@router.message(Command("get_my_id"))
async def get_chat_id(msg: Message):
    await msg.answer(f"Ваш Chat ID: {msg.from_user.id}")

    