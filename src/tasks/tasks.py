import time

import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from aiohttp import ClientError
from src.clients.aiohttp_client import AioHTTPClient
from src.currency.models import Currency
from src.deribitAPI.api import DeribitAPI
from src.logger import logger


async def get_price(db: AsyncSession):
    client = AioHTTPClient()
    api = DeribitAPI(client)

    try:
        while True:
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
            await asyncio.sleep(60)
    finally:
        await client.close()
