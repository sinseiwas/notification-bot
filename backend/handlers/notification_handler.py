from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
import platform
import subprocess

from utils.logger import (
    setup_logging,
    get_logger
)

setup_logging()
log = get_logger()

router = Router()


@router.message(Command("notificate"))
async def notificate_cmd(msg: Message):
    try:
        system = platform.system()

        if system == "Darwin":
            subprocess.run([
                "osascript", "-e",
                'display alert "Напоминание" message "Не забудь выключить компьютер и убрать за собой на моём столе!" giving up after 10'
            ])
        elif system == "Windows":
            subprocess.run([
                "powershell", "-Command",
                'Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show("Не забудь выключить компьютер и убрать за собой на моём столе!", "Напоминание", "OK", "Information")'
            ], shell=True)

        await msg.answer(f"Отправил уведомление на {system}")
        log.info("Notification sent")
    except Exception as e:
        log.exception(f"Exception: {e}")
        await msg.answer("Ошибка при отправке уведомления")


