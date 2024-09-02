from aiogram.types import Message

from aiogram import BaseMiddleware

from typing import Callable, Awaitable, Any, Dict
from ...database.models import User

class UserExsiting(BaseMiddleware):
    def __init__(
        self
    ):
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user = await User.get_or_none(
            id=event.from_user.id
        )
        if not user:
            return await event.answer(
                text='💉 Напишите /start'
            )

        data['user'] = user

        return await handler(event, data)
