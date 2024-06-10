from aiogram import BaseMiddleware
from aiogram.types import Message

from typing import List, Union, Callable, Awaitable, Any, Dict

import time

class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, time_period: Union[int, float] = 0.5):
        """
        Initializes an AntiFloodMiddleware object. This middleware is used to filter incoming messages
        and prevent flooding based on the time period between messages from the same user.

        Parameters:
        - time_period: int. The time period (in seconds) within which multiple messages are considered as flooding.
          Default is 5 seconds.
        """
        super().__init__()
        self.time_period = time_period
        self.user_last_message_time = {}

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        now = time.time()
        user_id = event.from_user.id
        
        last_message_time = self.user_last_message_time.get(user_id)
        
        if last_message_time is not None and now - last_message_time < self.time_period:
            return await event.answer(
                text='<b>⚠️ Не спам!</b>',
                disable_notification=True
            )
            # TODO: Добавить счет после которого человек летит в бан на x время 
        else:
            self.user_last_message_time[user_id] = now
            return await handler(event, data)