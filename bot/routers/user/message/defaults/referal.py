from aiogram import Router, Bot

from aiogram.types import Message

from aiogram.filters import Command
from utils.Middleware.filters.database import UserExsiting

from aiogram.types import Message

from utils.database.models import User

router = Router(
    name='referal'
)

router.message.middleware.register(
    UserExsiting()
)

@router.message(
    Command('referal')
)
async def start(
    message: Message,
    bot: Bot,
    user: User  
) -> None:
    ref_info_text = await user.ref_program_info(bot)

    await message.answer(f'{ref_info_text}')
