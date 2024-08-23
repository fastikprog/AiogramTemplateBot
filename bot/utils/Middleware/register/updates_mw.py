from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.types import ChatMemberUpdated
from utils.database.models.User import User
from bot import dp

STATUS_TO_BLOCK = {
    ChatMemberStatus.MEMBER: False,
    ChatMemberStatus.KICKED: True
}

async def init_updates_mw() -> None:
    @dp.my_chat_member()
    async def new_chat_status(event: ChatMemberUpdated):
        new_status = event.new_chat_member.status
        user_id = event.from_user.id

        is_block_bot = STATUS_TO_BLOCK.get(new_status, False)

        try:
            user, _ = await User.get_or_create(id=user_id)
            user.is_block_bot = is_block_bot
            await user.save()
        except Exception as e:
            print(f"Error updating user status: {e}")
