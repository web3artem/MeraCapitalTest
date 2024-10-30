from typing import Literal, Union
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import db
from .schemas import CurrencySchema, LastCurrencyPrice, CurrencyPriceByDate
from .services import CurrencyService
from .utils import convert_datetime_to_unix

router = APIRouter(
    tags=['currency']
)


@router.get("/get_currency_data_by_ticker")
async def get_currency_data(ticker: Literal["btc_usd", "eth_usd"],
                            db: AsyncSession = Depends(db.get_async_session)) -> dict:
    """Получение информации по тикеру"""
    service = CurrencyService(db)
    currency_instances = await service.get_currency_data(ticker)
    data = [CurrencySchema(ticker=instance.ticker,
                                  price=instance.price,
                                  updated_at=instance.updated_at) for instance in currency_instances]
    return {"result": data}


@router.get("/get_last_price_by_ticker")
async def get_last_currency_price(ticker: Literal["btc_usd", "eth_usd"],
                                  db: AsyncSession = Depends(db.get_async_session)):
    """Получение последней цены по тикеру"""
    service = CurrencyService(db)
    currency_instance = await service.get_last_currency_price(ticker)
    data = LastCurrencyPrice(ticker=currency_instance.ticker,
                                 price=currency_instance.price)
    return {"result": data}


@router.get("/get_currency_price_by_date")
async def get_currency_price_by_date(ticker: Literal["btc_usd", "eth_usd"],
                                     start_time: Union[str, int],
                                     end_time: Union[str, int],
                                     db: AsyncSession = Depends(db.get_async_session)):
    """Получение цены в промежутке от start_time до end_time"""
    if isinstance(start_time, str):
        start = convert_datetime_to_unix(start_time)
        end = convert_datetime_to_unix(end_time)

    if start and end:
        service = CurrencyService(db)
        currency_instances = await service.get_currency_price_by_date(ticker, start, end)
        data = [CurrencyPriceByDate(ticker=instance.ticker,
                                    price=instance.price,
                                    updated_at=instance.updated_at) for instance in currency_instances]
        return {"result": data}
    else:
        raise HTTPException(status_code=404, detail="Дата должна быть в UNIX формате либо DD-MM-YY")