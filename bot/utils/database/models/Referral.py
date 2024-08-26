from tortoise import fields
from tortoise.models import Model
from tortoise.fields import ForeignKeyRelation
from .User import User

class Referral(Model):
    id = fields.BigIntField(pk=True)  # Идентификатор реферала
    user: ForeignKeyRelation[User] = fields.ForeignKeyField(
        'models.User', related_name='user_referral', on_delete=fields.CASCADE
    )  # Реферал, пригласивший другого пользователя
    referred_user: ForeignKeyRelation[User] = fields.ForeignKeyField(
        'models.User', related_name='referred_users', on_delete=fields.CASCADE
    )  # Приглашённый пользователь
    created_at = fields.DatetimeField(auto_now_add=True)  # Дата и время создания реферала

    def __str__(self):
        return f"Referral(user_id={self.user.id}, referred_user_id={self.referred_user.id})"