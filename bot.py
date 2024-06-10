from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties 

from aiogram.utils.token import TokenValidationError

from data.config import SecretConfig

config = SecretConfig()

try:
    bot = Bot(
        token=config.get_secret('BOT_API_TOKEN', None),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            allow_sending_without_reply=True
        )
    )
except TokenValidationError:
    print('Не правильный ключ устоновлен в .env')
    exit(404)

dp = Dispatcher(

)