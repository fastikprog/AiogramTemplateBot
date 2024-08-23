from bot import dp
from data.config.config_bot import load_bot_config

from utils.Middleware.filters.anti_spam import AntiFloodMiddleware
from utils.Middleware.filters.chat import ChatTypeMiddleware

async def init_messages_mw(
        
) -> None:
    configuration = await load_bot_config()

    if configuration['always_private']:
        dp.message.middleware.register(
            ChatTypeMiddleware(chat_types=['private']))

    dp.message.middleware.register(AntiFloodMiddleware(
        time_period=configuration['interval']))