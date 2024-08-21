from aiogram.types import *
from aiogram.filters import BaseFilter

from typing import Union
    
class ChatTypeFilter(BaseFilter):
    def __init__(self, chat_type: Union[str, list]):
        """ 
        Initializes a ChatTypeFilter object. This filter is used to filter messages based on their chat type.

        Parameters:
        - chat_type: str or list. A single chat type or a list of chat types.
        Possible values: 'private', 'group', 'supergroup', 'channel'.

        Note:
        - The chat_type parameter is converted to a list if it's a single string.
        """
        self.chat_type = chat_type if isinstance(chat_type, list) else [chat_type]

    async def __call__(self, obj) -> bool:
        if isinstance(obj, (CallbackQuery, Message)):
            return obj.message.chat.type if isinstance(obj, CallbackQuery) else obj.chat.type in self.chat_type
        
        return False

class ChatIdFilter(BaseFilter):
    def __init__(
            self,
            chat_id: Union[int, list]
        ):
        if isinstance(chat_id, int):
            chat_id = [chat_id]  # Convert to list if it's an integer

        self.chat_id = chat_id

    async def __call__(self, obj):
        if isinstance(obj, (CallbackQuery, Message)):
            return obj.message.chat.id if isinstance(obj, CallbackQuery) else obj.chat.id in self.chat_id
        
        return False