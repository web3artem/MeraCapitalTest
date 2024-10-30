from typing import Generator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import settings


class Database:
    def __init__(self):
        self.async_engine = create_async_engine(settings.ASYNC_DATABASE_URL, echo=True)
        self.async_sessionmaker = async_sessionmaker(self.async_engine, class_=AsyncSession, expire_on_commit=False)

    async def get_async_session(self) -> Generator[AsyncSession, None, None]:
        async with self.async_sessionmaker() as session:
            yield session

    async def healtcheck(self) -> dict[str, str]:
        try:
            async with self.async_engine.begin() as conn:
                await conn.execute("SELECT 1")

            return {"healtcheck": "ok"}
        except SQLAlchemyError:
            return {"healtcheck": "false"}


class Base(DeclarativeBase):
    pass


db = Database()
