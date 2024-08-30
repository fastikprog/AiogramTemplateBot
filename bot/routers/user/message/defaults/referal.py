from aiogram import Router, Bot

from aiogram.types import Message, CallbackQuery

from aiogram.filters import Command
from loader import UserButtonsManager
from utils.filters.handlers import IsThatCall
from utils.Middleware.filters.database import UserExsiting

from aiogram.types import Message

from utils.database.models import User

router = Router(
    name='referal'
)

router.message.middleware.register(
    UserExsiting()
)

router.callback_query.middleware.register(
    UserExsiting()
)


@router.message(
    Command('referal')
)
@router.callback_query(
    IsThatCall('ref_system')
)
async def ref_system(
    message: Message | CallbackQuery,
    bot: Bot,
    user: User
) -> None:
    ref_info_text = await user.ref_program_info(bot)

    if hasattr(message, 'data'):
        message = message.message

        return await message.edit_text(
            text=ref_info_text,
            reply_markup=UserButtonsManager.ref_system_inline_button(
                language_code=user.language_code
            )
        )

    await message.answer(
        text="🤝",
        reply_markup=UserButtonsManager.one_button_keyboard()
    )
    return await message.answer(
        text=ref_info_text,
        reply_markup=UserButtonsManager.ref_system_inline_button(
            language_code=user.language_code,
            back_button=False
        )
    )


@router.callback_query(
    IsThatCall('ref_list')
)
async def ref_list(
    call: CallbackQuery,
    user: User
) -> None:
    ref_info_text = await user.my_referals(
        hide_id_length=False,
        hide_username_length=-1
    )

    return await call.message.edit_text(
        text=ref_info_text,
        reply_markup=UserButtonsManager.one_button_inline(
            ButtonText="🔙 Назад",
            ButtonCall="ref_system"
        )
    )
