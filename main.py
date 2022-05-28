from fastapi import FastAPI
from core.config import settings
from db.base import database
from endpoints import broadcasts
import uvicorn

app = FastAPI(title="Notify exchange")
app.include_router(broadcasts.router, prefix="/broadcasts", tags=["broadcasts"])


@app.get("/")
async def root():
    return {"my message": "Hello Marat"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.server_host, port=settings.server_port, reload=True)

# -------------------------------------------------------------------------
    # uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)


