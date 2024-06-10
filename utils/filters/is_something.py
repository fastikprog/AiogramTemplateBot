from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAlphabetic(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text.isalpha()

class IsNumeric(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text.isdigit()