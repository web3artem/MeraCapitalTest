from typing import Literal, Union
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import db
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
    data = await service.get_currency_data(ticker)
    return {"result": data}


@router.get("/get_last_price_by_ticker")
async def get_last_currency_price(ticker: Literal["btc_usd", "eth_usd"],
                                  db: AsyncSession = Depends(db.get_async_session)):
    """Получение последней цены по тикеру"""
    service = CurrencyService(db)
    data = await service.get_last_currency_price(ticker)
    return {"result": data}


@router.get("/get_currency_price_by_date")
async def get_currency_price_by_date(ticker: Literal["btc_usd", "eth_usd"],
                                     start_time: Union[str, int],
                                     end_time: Union[str, int],
                                     db: AsyncSession = Depends(db.get_async_session)):
    """Получение цены в промежутке от start_time до end_time"""
    if not start_time.isdigit():
        start = convert_datetime_to_unix(start_time)
        end = convert_datetime_to_unix(end_time)

    else:
        start = int(start_time)
        end = int(end_time)

    service = CurrencyService(db)
    data = await service.get_currency_price_by_date(ticker, start, end)
    return {"result": data}
