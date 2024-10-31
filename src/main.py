import asyncio

from fastapi import FastAPI, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.tasks import get_price
from src.clients.aiohttp_client import AioHTTPClient
from src.currency.models import Currency
from src.currency.routes import router as currency_router
from src.database import db

app = FastAPI()

app.include_router(currency_router)


@app.on_event("startup")
async def start():
    asyncio.create_task(get_price(db.async_sessionmaker()))
