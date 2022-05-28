from fastapi import Depends, HTTPException, status
from repositories.broadcasts import BroadcastRepository
# from repositories.jobs import JobRepository
from db.base import database
from core.security import JWTBearer, decode_access_token
from models.broadcast import Broadcast


def get_broadcast_repository() -> BroadcastRepository:
    return BroadcastRepository(database)


# def get_job_repository() -> JobRepository:
#     return JobRepository(database)

async def get_current_broadcast(
    broadcasts: BroadcastRepository = Depends(get_broadcast_repository),
    token: str = Depends(JWTBearer()),
) -> Broadcast:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    clients_filter: str = payload.get("sub")
    if clients_filter is None:
        raise cred_exception
    broadcast = await broadcasts.get_by_filter(clients_filter=clients_filter)
    if broadcast is None:
        return cred_exception
    return broadcast

