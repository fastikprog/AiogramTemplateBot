from bot import dp

from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, MEMBER, KICKED
from aiogram.types import ChatMemberUpdated

async def init_updates_mw(
        
) -> None:
    @dp.my_chat_member(
        ChatMemberUpdatedFilter(member_status_changed=KICKED)
    )
    async def user_blocked_bot(event: ChatMemberUpdated):
        print(event.from_user.id)

    @dp.my_chat_member(
        ChatMemberUpdatedFilter(member_status_changed=MEMBER)
    )
    async def user_unblocked_bot(event: ChatMemberUpdated):
        print(event.from_user.id)