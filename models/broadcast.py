import datetime
from typing import Optional
from pydantic import BaseModel, \
    validator, EmailStr


class Broadcast(BaseModel):
    id: Optional[str] = None
    launch_time: datetime.datetime
    message_text: str
    clients_filter: str
    end_time: datetime.datetime


class BroadcastIn(BaseModel):
    launch_time: datetime.datetime
    message_text: str
    clients_filter: str
    end_time: datetime.datetime

    # @validator("password2")
    # def password_match(cls, v, values, **kwargs):
    #     if 'password' in values and v != values["password"]:
    #         raise ValueError("passwords don't match")
    #     return v
