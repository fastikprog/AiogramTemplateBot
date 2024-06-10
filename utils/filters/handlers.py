
import re

from aiogram.filters import Filter
from aiogram.fsm.context import FSMContext

from aiogram.types import *

class IsThatText(Filter):
    def __init__(self, *my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message, state: FSMContext) -> bool:       
        return message.text in self.my_text
    
class IsThatTextRe(Filter):
    def __init__(self, *patterns: str) -> None:
        self.patterns = patterns

    async def __call__(self, message: Message, state: FSMContext) -> bool:
        for pattern in self.patterns:
            if re.search(pattern, message.text):
                return True
        return False
    
class IsThatCall(Filter):
    def __init__(self, *my_callbacks: str) -> None:
        self.my_callbacks = my_callbacks

    async def __call__(self, call: CallbackQuery, state: FSMContext) -> bool:
        return call.data in self.my_callbacks

class IsThatCallStartWith(Filter):
    def __init__(self, my_callback: str) -> None:
        self.my_callback = my_callback

    async def __call__(self, call: CallbackQuery) -> bool:
        return call.data.startswith(self.my_callback)