import asyncio
import signal
from bot import bot, dp

from utils.Middleware.register import init_mw

from utils.database.database_manager import DatabaseManager

import routers.user.message.defaults.start as start
import routers.user.message.defaults.referal as referal
import routers.user.message.defaults.dev as dev

from aiogram.types import BotCommand

from data.config.secret_config import SecretConfig

config = SecretConfig()

database = DatabaseManager(
    username=config.get_secret(
        key='DATABASE_LOGIN',
        default='root'
    ),
    password=config.get_secret(
        key="DATABASE_PASSWORD"
    ),
    db_name=config.get_secret(
        key="DATABASE_NAME"
    ),
    ip=config.get_secret(
        key="DATABASE_IP",
        default="localhost"
    ),
    port=config.get_secret(
        key="DATABASE_PORT",
        default=3306
    )
)

async def set_bot_commands():
    commands = [
        BotCommand(command="/start", description="⭐️ Начать работу с ботом"),
        BotCommand(command="/referal", description="👥 Реферальная программа"),
        BotCommand(command="/dev", description="🧑‍💻 Разработчик")
        # Добавьте другие команды по мере необходимости
    ]
    await bot.set_my_commands(commands)

async def on_startup():
    await database.init_db()
    await set_bot_commands()

async def on_shutdown():
    await database.close_db()

async def config_and_init() -> None:
    # Инит мидлавров
    await init_mw()
    await init()
    # Добавляем обработчик сигнала клавиатуры
    signal.signal(signal.SIGINT, stop_bot)

async def stop_bot(sig, frame):
    """Останавливаем бот."""
    await dp.stop_polling()

async def init() -> None:
    """Initialize the bot with the given configuration."""
    dp.include_routers(
        start.router,
        referal.router,
        dev.router
    )

    bot_info = await bot.get_me()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    print(f'Starting polling the bot: https://t.me/{
        bot_info.username} \nBot information: @{bot_info.username} | ID: {bot_info.id}')

    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(config_and_init())
