from aiogram import Router, Bot

from aiogram.types import Message

from aiogram.filters import CommandStart
from utils.filters.chat import ChatTypeFilter

from aiogram.fsm.storage.base import StorageKey

router = Router(
    name='test'
)

# Обработчик команды /start
@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer("Привет! Как тебя зовут?")
