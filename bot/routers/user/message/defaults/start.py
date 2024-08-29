from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, or_f, CommandObject
from aiogram.utils.deep_linking import decode_payload
from utils.Middleware.filters.database import UserExsiting
from utils.filters.handlers import IsThatCall, IsThatText
from loader import UserButtonsManager
from utils.database.models import User, Referral
from tortoise.transactions import in_transaction

router = Router(name='start')

router.callback_query.middleware.register(
    UserExsiting()
)


@router.message(
    or_f(
        CommandStart(),
        CommandStart(
            deep_link=True
        ),
        IsThatText("🏠Главное меню🏠")
    )
)
@router.callback_query(
    IsThatCall('menu')
)
async def start(
    message: Message | CallbackQuery,
    bot: Bot,
    user: User | None = None,
    command: CommandObject | None = None,
) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    language_code = message.from_user.language_code
    referrer = None

    menu_text = '🏠 Главное меню'

    if hasattr(message, 'data'):
        message = message.message

        return await message.edit_text(
            text=menu_text,
            reply_markup=UserButtonsManager.start_inline_button(
                language_code=user.language_code
            )
        )

    args = command.args if command else None

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
        text="🏠",
        reply_markup=UserButtonsManager.one_button_keyboard(
            ButtonText="🏠Главное меню🏠"
        )
    )
    return await message.answer(
        text=menu_text,
        reply_markup=UserButtonsManager.start_inline_button(
            language_code=user.language_code
        )
    )
