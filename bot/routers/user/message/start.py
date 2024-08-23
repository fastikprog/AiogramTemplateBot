from aiogram import Router, Bot

from aiogram.types import Message

from aiogram.filters import CommandStart

router = Router(
    name='test'
)

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer("👋<b>Привет!</b> Это шаблон телеграм бота от @fastikprog\nПо вопросам к нему. \n🪛 <i>Репозитория</i>: https://github.com/fastikprog/AiogramTemplateBot")
