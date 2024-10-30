from time import time
from sqlalchemy import String, Integer, TIMESTAMP, Float, Index
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Currency(Base):
    __tablename__ = "currency"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticker: Mapped[str] = mapped_column(String(length=50))
    price: Mapped[float] = mapped_column(Float)
    updated_at: Mapped[time] = mapped_column(Integer)

    def __repr__(self):
        return f"{self.ticker} | {self.price} | {self.updated_at}"

Index('ix_currency_ticker', Currency.ticker)