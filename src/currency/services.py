from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Currency
from .schemas import GetCurrencyResponse, LastCurrencyResponse, CurrencyPriceByDateResponse


class CurrencyService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_currency_data(self, ticker: str):
        """Получение всех полей по тикеру"""
        query = select(Currency).where(Currency.ticker == ticker)
        res = await self.db.execute(query)
        ticker_data = res.scalars().all()
        data = [GetCurrencyResponse(ticker=instance.ticker,
                                    price=instance.price,
                                    updated_at=instance.updated_at) for instance in ticker_data]
        return data

    async def get_last_currency_price(self, ticker: str):
        """Получение последней цены тикера"""
        query = (
            select(Currency)
            .where(Currency.ticker == ticker)
            .order_by(Currency.id.desc())
            .limit(1)
        )
        res = await self.db.execute(query)
        latest_currency = res.scalars().first()
        return LastCurrencyResponse(ticker=latest_currency.ticker,
                                    price=latest_currency.price)

    async def get_currency_price_by_date(self, ticker: str, start_date: int, end_date: int):
        """Получение цены валюты в диапазоне от start_date до end_date"""
        query = (
            select(Currency)
            .where(Currency.ticker == ticker,
                   and_(Currency.updated_at >= start_date,
                        Currency.updated_at <= end_date))
        )
        res = await self.db.execute(query)
        currency_instances = res.scalars().all()
        data = [CurrencyPriceByDateResponse(ticker=instance.ticker,
                                            price=instance.price,
                                            updated_at=instance.updated_at) for instance in currency_instances]
        return data
