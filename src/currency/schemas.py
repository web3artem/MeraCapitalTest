from pydantic import BaseModel

class GetCurrencyResponse(BaseModel):
    ticker: str
    price: float
    updated_at: int


class LastCurrencyResponse(BaseModel):
    ticker: str
    price: float


class CurrencyPriceByDateResponse(BaseModel):
    ticker: str
    price: float
    updated_at: int