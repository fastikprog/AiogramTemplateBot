from aiogram import Router, Bot

from aiogram.types import Message

from aiogram.filters import CommandStart

from utils.database.models import User

router = Router(
    name='test'
)

@router.message(
    CommandStart()
)
async def start(
    message: Message
) -> None:
    user_id = message.from_user.id  # Получаем id пользователя из сообщения
    username = message.from_user.username

    user, created = await User.get_or_create(
        id=user_id,
        defaults={'username': username}
    )

    if created:
        # Новый пользовотель
        ...

    print(user)
    print(created)

    await message.answer("👋<b>Привет!</b> Это шаблон телеграм бота от @fastikprog\nПо вопросам к нему. \n🪛 <i>Репозитория</i>: https://github.com/fastikprog/AiogramTemplateBot")
