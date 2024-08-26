from tortoise import fields
from tortoise.models import Model
from tortoise.fields import ForeignKeyRelation

from aiogram.utils.deep_linking import create_start_link
from aiogram import Bot
from datetime import datetime, timedelta


class User(Model):
    id = fields.BigIntField(pk=True)  # Идентификатор пользователя
    username = fields.CharField(
        max_length=32, null=True)  # @username пользователя
    # Заблокировал ли пользователь бота
    is_block_bot = fields.BooleanField(default=False)
    # Язык пользователя, например 'en', 'ru'
    language_code = fields.CharField(max_length=10, null=False)
    balance = fields.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)  # Баланс пользователя
    ban = fields.BooleanField(default=False)  # Имеет ли доступ к боту
    referrer: ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User', related_name='referrals', null=True
    )  # Пользователь, который пригласил данного пользователя
    # Дата и время создания записи о пользователе
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, is_block_bot={self.is_block_bot}, language_code={self.language_code}, created_at={self.created_at}, balance={self.balance}, ban={self.ban}, referrer={self.referrer})"

    async def ref_program_info(self, bot: Bot) -> str:
        # Создание реферальной ссылки
        link = await create_start_link(bot, self.id, encode=True)

        # Получение текущего времени
        now = datetime.now()
        start_of_today = datetime(now.year, now.month, now.day)
        start_of_week = start_of_today - \
            timedelta(days=start_of_today.weekday())  # Начало недели
        start_of_month = datetime(now.year, now.month, 1)  # Начало месяца

        # Подсчет рефералов за различные периоды
        ref_count_all_time = await self.referrals.all().count()  # Количество всех рефералов
        # Рефералы за сегодня
        ref_count_today = await self.referrals.filter(created_at__gte=start_of_today).count()
        # Рефералы за неделю
        ref_count_week = await self.referrals.filter(created_at__gte=start_of_week).count()
        # Рефералы за месяц
        ref_count_month = await self.referrals.filter(created_at__gte=start_of_month).count()

        # Форматирование вывода в HTML
        info = (
            f"👤 <b>Реферальная программа</b>\n"
            f"🔗 <b>Ваша реферальная ссылка:</b> <a href='{
                link}'>Нажмите здесь</a>\n\n"
            f"📅 <b>Рефералы за сегодня:</b> {ref_count_today}\n"
            f"📆 <b>Рефералы за неделю:</b> {ref_count_week}\n"
            f"🗓️ <b>Рефералы за месяц:</b> {ref_count_month}\n"
            f"🌟 <b>Всего рефералов:</b> {ref_count_all_time}"
        )
        return info
