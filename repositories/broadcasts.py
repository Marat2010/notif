import datetime
from typing import List, Optional, Mapping
from db.broadcasts import broadcasts
from models.broadcast import Broadcast, BroadcastIn
# from core.config import
from .base import BaseRepository


class BroadcastRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Mapping]:
        query = broadcasts.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[Broadcast]:
        query = broadcasts.select().where(broadcasts.c.id == id)
        broadcast = await self.database.fetch_one(query)
        if broadcast is None:
            return None
        return Broadcast.parse_obj(broadcast)

    async def create(self, b: BroadcastIn) -> Broadcast:
        broadcast = Broadcast(
            launch_time=b.launch_time,
            message_text=b.message_text,
            clients_filter=b.clients_filter,
            end_time=b.end_time,
        )
        values = {**broadcast.dict()}
        values.pop("id", None)
        query = broadcasts.insert().values(**values)
        broadcast.id = await self.database.execute(query)
        return broadcast

    async def update(self, id: int, b: BroadcastIn) -> Broadcast:
        broadcast = Broadcast(
            id=id,
            launch_time=b.launch_time,
            message_text=b.message_text,
            clients_filter=b.clients_filter,
            end_time=b.end_time,
        )
        values = {**broadcast.dict()}
        values.pop("id", None)
        query = broadcasts.update().where(broadcasts.c.id == id).values(**values)
        await self.database.execute(query)
        return broadcast

    async def get_by_filter(self, clients_filter: str) -> Broadcast:
        query = broadcasts.select().where(broadcasts.c.clients_filter == clients_filter)
        broadcast = await self.database.fetch_one(query)
        if broadcast is None:
            return None
        return Broadcast.parse_obj(broadcast)


# ------------------------------------
    # async def get_all(self, limit: int = 100, skip: int = 0) -> List[Broadcast]:
# launch_time=datetime.datetime.utcnow(),
# end_time=datetime.datetime.strptime(b.end_time, "%Y/%m/%d %H:%M:%S"),
# end_time=datetime.datetime,
# launch_time = datetime.datetime.utcnow(),
# end_time = datetime.datetime.utcnow(),
#         print("====Time---- ", broadcast.end_time)
#         print("=======TZ---- ", broadcast.end_time.tzname())


