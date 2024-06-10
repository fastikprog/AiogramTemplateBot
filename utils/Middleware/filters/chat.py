from aiogram.types import Message

from aiogram import BaseMiddleware

from typing import List, Union, Callable, Awaitable, Any, Dict

class ChatTypeMiddleware(BaseMiddleware):
    ALLOWED_CHAT_TYPES = {'private', 'group', 'supergroup', 'channel'}

    def __init__(
        self,
        chat_types: Union[str, List[str]],
    ):
        """
        Initializes a ChatTypeMiddleware object. This middleware is used to filter incoming messages
        based on their chat type and the presence of certain data.

        Parameters:
        - chat_types: Union[str, List[str]]. A single chat type or a list of chat types.
          Possible values: 'private', 'group', 'supergroup', 'channel'.
        """
        super().__init__()

        if isinstance(chat_types, str):
            chat_types = [chat_types]

        self.chat_types = set(chat_types)

        if not self.chat_types.issubset(self.ALLOWED_CHAT_TYPES):
            raise ValueError("Invalid chat types provided.")

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if event.chat.type not in self.chat_types:
            return

        return await handler(event, data)