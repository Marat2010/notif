import sqlalchemy
from .base import metadata
import datetime

messages = sqlalchemy.Table(
    "messages",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("creation_time", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("sending_status", sqlalchemy.String),
    sqlalchemy.Column("broadcast_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('broadcasts.id'), nullable=False),
    sqlalchemy.Column("client_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('clients.id'), nullable=False),
)

"""
Сущность "сообщение" имеет атрибуты: 

• уникальный id сообщения 

• дата и время создания (отправки) 

• статус отправки 

• id рассылки, в рамках которой было отправлено сообщение 

• id клиента, которому отправили 
"""