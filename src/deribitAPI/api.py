from logger import logger
from src.clients.aiohttp_client import AioHTTPClient
from aiohttp import ClientSession


class DeribitAPI:
    def __init__(self, http_client: AioHTTPClient):
        self.http_client = http_client

    async def get_instrument(self, ticker: str):
        url = f"https://test.deribit.com/api/v2/public/ticker?instrument_name={ticker}"
        try:
            return await self.http_client.get(url)
        except Exception as e:
            logger.error(f"При отправлении запроса на ticker?instrument_name={ticker} возникла ошибка {e}")
