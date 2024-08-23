from .message_mw import init_messages_mw
from .updates_mw import init_updates_mw

async def init_mw(
        
) -> None:
    await init_updates_mw()
    await init_messages_mw()