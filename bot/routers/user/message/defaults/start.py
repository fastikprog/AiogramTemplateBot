from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, or_f, CommandObject
from aiogram.utils.deep_linking import decode_payload
from utils.database.models import User, Referral
from tortoise.transactions import in_transaction

router = Router(name='start')

@router.message(or_f(CommandStart(), CommandStart(deep_link=True)))
async def start(
    message: Message,
    command: CommandObject,
    bot: Bot
) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    language_code = message.from_user.language_code
    referrer = None

    args = command.args
    
    default_data_user = {
        'username': username,
        'language_code': language_code
    }

    if args:
        try:
            ref_id = decode_payload(args)
            referrer = await User.get_or_none(id=int(ref_id))
        except ValueError:
            pass  # Убедитесь, что ref_id не используется, если декодирование не удалось

    async with in_transaction():
        user, created = await User.get_or_create(
            id=user_id,
            defaults=default_data_user
        )

        if created and referrer:
            user.referrer = referrer
            await user.save()

            # Обеспечиваем, что запись о реферале создается только если она не существует
            await Referral.get_or_create(
                user=referrer,
                referred_user=user
            )

            NewRefText = "<b>🆕 У вас новый рефераль</b>"
            await bot.send_message(
                chat_id=referrer.id,
                text=NewRefText
            )

    await message.answer(
        "👋<b>Привет!</b> Это шаблон телеграм бота от @fastikprog\nПо вопросам к нему. \n🪛 <i>Репозитория</i>: https://github.com/fastikprog/AiogramTemplateBot"
    )
