import asyncio
from aiogram.filters import BaseFilter
from aiogram.types import InlineQuery

from aiogram import Bot

from typing import Any, Union, Optional

class DebouncedInlineQueryFilter(BaseFilter):
    """
    A filter to debounce inline queries in an asynchronous Telegram bot.

    This filter ensures that only the most recent inline query from each user is processed,
    cancelling any previous pending queries within a specified timeout period.

    Attributes:
        inline_handler (function): The handler function to process the inline query.
        timeout (Union[int, float], optional): The timeout period in seconds before executing the handler. Defaults to 3.0 seconds.
        tasks (dict): A dictionary to keep track of pending tasks per user.

    Methods:
        __call__(inline_query: InlineQuery, bot: Bot):
            Asynchronously handle an inline query, canceling any previous pending task for the same user.
        delayed_query_handler(inline_query: InlineQuery, bot: Bot, query_handler: function):
            Asynchronously delay the handling of an inline query by the specified timeout period.
    """
    
    def __init__(
        self,
        inline_handler: Any[function],
        timeout: Optional[Any[Union[int, float]]] = 3.0,
    ):
        self.timeout = timeout
        self.inline_handler = inline_handler
        self.tasks = {}

    async def __call__(
        self,
        inline_query: InlineQuery,
        bot: Bot
    ):
        """
        Handle the inline query with a debounce mechanism.

        Args:
            inline_query (InlineQuery): The inline query to be handled.
            bot (Bot): The bot instance to use for handling the query.
        """
        user_id = inline_query.from_user.id

        if user_id in self.tasks:
            self.tasks[user_id].cancel()

        self.tasks[user_id] = asyncio.create_task(
            self.delayed_query_handler(
                inline_query,
                bot,
                self.inline_handler
            )
        )

        try:
            await self.tasks[
                user_id
            ]
        except asyncio.CancelledError:
            return

    async def delayed_query_handler(
        self,
        inline_query: Any[InlineQuery],
        bot: Any[Bot],
        query_handler: Any[function]
    ):
        """
        Delay handling the inline query by the specified timeout.

        Args:
            inline_query (InlineQuery): The inline query to be handled.
            bot (Bot): The bot instance to use for handling the query.
            query_handler (function): The handler function to process the inline query.
        """
        await asyncio.sleep(
            delay=self.timeout
        )
        await query_handler(
            inline_query,
            bot
        )