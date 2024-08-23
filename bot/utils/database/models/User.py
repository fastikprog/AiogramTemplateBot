from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.BigIntField(pk=True)  
    username = fields.CharField(max_length=255, null=True)  
    is_block_bot = fields.BooleanField(default=False)

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, is_block_bot={self.is_block_bot})"

