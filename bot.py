from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties 

from data.config import SecretConfig

config = SecretConfig()

bot = Bot(
    token=config.get_secret('BOT_API_TOKEN', None),
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
        allow_sending_without_reply=True
    )
)

dp = Dispatcher(

)