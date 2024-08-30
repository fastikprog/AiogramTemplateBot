from aiogram import Router
from aiogram.types import Message, CallbackQuery

from aiogram.filters import Command
from loader import UserButtonsManager
from utils.filters.handlers import IsThatCall
from utils.Middleware.filters.database import UserExsiting

from aiogram.types import Message

router = Router(
    name='dev'
)

router.message.middleware.register(
    UserExsiting()
)
router.callback_query.middleware.register(
    UserExsiting()
)


@router.message(
    Command('dev')
)
@router.callback_query(
    IsThatCall('dev_info')
)
async def start(
    message: Message | CallbackQuery
) -> None:
    dev_info = f"<a href='https://github.com/fastikprog/AiogramTemplateBot'>⁬⁯</a>"

    if hasattr(message, 'data'):
        message = message.message

        return await message.edit_text(
            text=dev_info,
            reply_markup=UserButtonsManager.dev_inline_button()
        )
    
    await message.answer(
        text="🧑‍💻",
        reply_markup=UserButtonsManager.one_button_keyboard()
    )
    return await message.answer(
        text=dev_info,
        reply_markup=UserButtonsManager.dev_inline_button(
            back_button=False
        )
    )
