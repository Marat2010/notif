import sqlalchemy
from .base import metadata
import datetime

broadcasts = sqlalchemy.Table(
    "broadcasts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("launch_time", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("message_text", sqlalchemy.String),
    sqlalchemy.Column("clients_filter", sqlalchemy.String),
    sqlalchemy.Column("end_time", sqlalchemy.DateTime),
)

"""
Сущность "рассылка" имеет атрибуты: 

• уникальный id рассылки 

• дата и время запуска рассылки 

• текст сообщения для доставки клиенту 

• фильтр свойств клиентов, на которых должна быть произведена рассылка (код мобильного оператора, тег) 

• дата и время окончания рассылки: если по каким-то причинам не успели разослать 
  все сообщения - никакие сообщения клиентам после этого времени доставляться не должны 
"""


# -----------------------------------
# sqlalchemy.Column("end_time", sqlalchemy.DateTime, default=datetime.datetime),

