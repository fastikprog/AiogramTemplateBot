from aiogram import Router
from aiogram.types import Message

from aiogram.filters import Command
from utils.Middleware.filters.database import UserExsiting

from aiogram.types import Message

router = Router(
    name='dev'
)

router.message.middleware.register(
    UserExsiting()
)

@router.message(
    Command('dev')
)
async def start(
    message: Message
) -> None:
    await message.answer(
        text="👋<b>Привет!</b> Это шаблон телеграм бота от @fastikprog\nПо вопросам касательно шаблону к нему. \n🪛 <i>Репозитория</i>: https://github.com/fastikprog/AiogramTemplateBot"
    )
