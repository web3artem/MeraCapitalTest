import asyncio
import time

from aiohttp import ClientError
from clients.aiohttp_client import AioHTTPClient
from currency.models import Currency
from deribitAPI.api import DeribitAPI
from logger import logger
from sqlalchemy.ext.asyncio import AsyncSession


async def get_price(db: AsyncSession):
    client = AioHTTPClient()
    api = DeribitAPI(client)

    try:
        for i in range(3):
            try:
                btc_usd = await api.get_instrument("BTC_USDT")
                eth_usd = await api.get_instrument("ETH_USDT")

                current_time = int(time.time())

                btc_model = Currency(
                    ticker="btc_usd",
                    price=btc_usd["result"]["index_price"],
                    updated_at=current_time
                )
                eth_model = Currency(
                    ticker="eth_usd",
                    price=eth_usd["result"]["index_price"],
                    updated_at=current_time
                )

                db.add(btc_model)
                db.add(eth_model)
                await db.commit()
                logger.success(f"Данные за {current_time} были успешно сохранены")

            except (ClientError, KeyError) as e:
                logger.error(f"Ошибка при получении данных из api: {e}")
            except Exception as e:
                logger.error(f"Неизвестная ошибка {e}")
            await asyncio.sleep(10)
    finally:
        await client.close()
