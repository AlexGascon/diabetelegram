import uuid

from pynamodb.attributes import NumberAttribute, UnicodeAttribute
from pynamodb.models import Model

from diabetelegram.models.base import BaseMeta


def generate_expense_id():
    return uuid.uuid4().hex

class Expense(Model):
    class Meta(BaseMeta):
        table_name = "algasbot-expenses"

    CATEGORIES = [
        'coca cola',
        'eating out',
        'fun money',
        'supermercado'
    ]

    id = UnicodeAttribute(hash_key=True, default=generate_expense_id)
    category = UnicodeAttribute()
    amount = NumberAttribute(null=True)
    notes = UnicodeAttribute(null=True)
