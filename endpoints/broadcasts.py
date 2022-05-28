from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from repositories.broadcasts import BroadcastRepository
from models.broadcast import Broadcast, BroadcastIn
from .depends import get_broadcast_repository, get_current_broadcast


router = APIRouter()


@router.get("/", response_model=List[Broadcast])
async def read_broadcasts(
        broadcasts: BroadcastRepository = Depends(get_broadcast_repository),
        limit: int = 100,
        skip: int = 0):
    return await broadcasts.get_all(limit=limit, skip=skip)


@router.post("/", response_model=Broadcast)
async def create_broadcast(
        broadcast: BroadcastIn,
        broadcasts: BroadcastRepository = Depends(get_broadcast_repository)):
    return await broadcasts.create(b=broadcast)


@router.put("/", response_model=Broadcast)
async def update_broadcast(
        id: int,
        broadcast: BroadcastIn,
        broadcasts: BroadcastRepository = Depends(get_broadcast_repository),):
    #     current_broadcast: Broadcast = Depends(get_current_broadcast)):
    # old_broadcast = await broadcasts.get_by_id(id=id)
    # if old_broadcast is None or old_broadcast.clients_filter != current_broadcast.clients_filter:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found clients_filter")
    return await broadcasts.update(id=id, b=broadcast)



# ---------------------------------------------------
# @router.put("/", response_model=Broadcast)
# async def update_broadcast(
#         id: int,
#         broadcast: BroadcastIn,
#         broadcasts: BroadcastRepository = Depends(get_broadcast_repository),
#         current_broadcast: Broadcast = Depends(get_current_broadcast)):
#     old_broadcast = await broadcasts.get_by_id(id=id)
#     if old_broadcast is None or old_broadcast.clients_filter != current_broadcast.clients_filter:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found clients_filter")
#     return await broadcasts.update(id=id, b=broadcast)
