from bot import bot, dp
import asyncio

from utils.Middleware.filters.chat import ChatTypeMiddleware

import routers.user.message.start as start
from data.config import SecretConfig

config = SecretConfig()


async def init() -> None:
    dp.include_routers(
        start.router
    )

    If_ALWAYS_PRIVATE = config.get_secret(
        key='If_ALWAYS_PRIVATE',
        default=0
    )
    If_ALWAYS_PRIVATE = False if int(If_ALWAYS_PRIVATE) == 0 else True

    if If_ALWAYS_PRIVATE:
        dp.message.middleware.register(
            ChatTypeMiddleware(
                chat_types=['private']
            )
        )

    await bot.delete_webhook()

    await dp.start_polling(
        bot,
    )

if __name__ == '__main__':
    asyncio.run(
        init()
    )
