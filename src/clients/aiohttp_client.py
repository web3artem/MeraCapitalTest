import ssl
from typing import Any
from pip._vendor import certifi

import aiohttp
from aiohttp import TCPConnector, ClientResponseError

from src.logger import logger


class AioHTTPClient:
    def __init__(self):
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        self.session = aiohttp.ClientSession(connector=TCPConnector(ssl=ssl_context))

    async def get(self, url: str, params: str = None) -> dict[str, Any]:
        async with self.session.get(url, params=params) as response:
            response.raise_for_status()
            return await response.json()

    async def close(self):
        await self.session.close()
