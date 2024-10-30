from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from tasks import get_price
from clients.aiohttp_client import AioHTTPClient
from currency.models import Currency
from currency.routes import router as currency_router

from src.database import db

app = FastAPI()

app.include_router(currency_router)


@app.on_event("startup")
async def start():
    # await get_price(db.async_sessionmaker())
    ...

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str, db: AsyncSession = Depends(db.get_async_session)):
    q = select(Currency)
    res = await db.execute(q)
    currencies = res.scalars().all()
    print(currencies)
    return {"message": f"Hello {name}"}
