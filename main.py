import asyncio, signal
from bot import bot, dp

from utils.Middleware.filters.anti_spam import AntiFloodMiddleware
from utils.Middleware.filters.chat import ChatTypeMiddleware

import routers.user.message.start as start

from data.config import SecretConfig

config = SecretConfig()

async def load_config() -> dict:
    """Load configuration settings from SecretConfig."""
    always_private = config.get_secret(key='If_ALWAYS_PRIVATE', default=0)
    interval = float(config.get_secret(key='ANTI_FLOOD_INTERVAL', default=0.5))
    always_private = bool(int(always_private))

    return {
        'always_private': always_private,
        'interval': interval
    }

async def config_and_init() -> None:
    """Load configurations and initialize the bot."""
    configuration = await load_config()
    await init(configuration)

    # Добавляем обработчик сигнала клавиатуры
    signal.signal(signal.SIGINT, stop_bot)

async def stop_bot(sig, frame):
    """Останавливаем бот."""
    await dp.stop_polling()

async def init(configuration: dict) -> None:
    """Initialize the bot with the given configuration."""
    dp.include_routers(start.router)

    if configuration['always_private']:
        dp.message.middleware.register(ChatTypeMiddleware(chat_types=['private']))

    dp.message.middleware.register(AntiFloodMiddleware(time_period=configuration['interval']))

    bot_info = await bot.get_me()

    print(f'Starting polling the bot: https://t.me/{bot_info.username} \nBot information: @{bot_info.username} | ID: {bot_info.id}')
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(config_and_init())
