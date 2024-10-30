from pydantic import BaseModel

class CurrencySchema(BaseModel):
    ticker: str
    price: float
    updated_at: int


class LastCurrencyPrice(BaseModel):
    ticker: str
    price: float


class CurrencyPriceByDate(BaseModel):
    ticker: str
    price: float
    updated_at: int