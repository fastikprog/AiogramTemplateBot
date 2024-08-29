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
    dev_info = "👋<b>Привет!</b> Это шаблон телеграм бота от @fastikprog\nПо вопросам касательно шаблону к нему. \n🪛 <i>Репозитория</i>: https://github.com/fastikprog/AiogramTemplateBot"

    if hasattr(message, 'data'):
        message = message.message

        return await message.edit_text(
            text=dev_info,
            reply_markup=UserButtonsManager.one_button_inline(
                ButtonText="🏠 В меню",
                ButtonCall="menu"
            )
        )

    return await message.answer(
        text=dev_info,
        reply_markup=UserButtonsManager.one_button_keyboard(
            ButtonText="🏠Главное меню🏠"
        )
    )
