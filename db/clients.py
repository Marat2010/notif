import sqlalchemy
from .base import metadata
# import datetime

clients = sqlalchemy.Table(
    "clients",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("phone_number", sqlalchemy.String, unique=True),
    sqlalchemy.Column("operator_code", sqlalchemy.String),
    sqlalchemy.Column("tag", sqlalchemy.String),
    sqlalchemy.Column("time_zone", sqlalchemy.String),
)

# from sqlalchemy_utils import PhoneNumber
# sqlalchemy.Unicode        tag     Timezone
#   emails: List[Email]
#   phonenumbers: List[PhoneNumber]

"""
Сущность "клиент" имеет атрибуты: 

• уникальный id клиента 

• номер телефона клиента в формате 7XXXXXXXXXX (X - цифра от 0 до 9) 

• код мобильного оператора 

• тег (произвольная метка) 

• часовой пояс 
"""
