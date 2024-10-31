import pytest

from src.main import app


def test_get_currency_data(client):
    response = client.get("http://0.0.0.0:8000/get_currency_data_by_ticker?ticker=btc_usd")
    assert response.status_code == 200
    assert "result" in response.json()
    assert response.json()["result"][0]["ticker"] == "btc_usd"


def test_get_last_currency_price(client):
    response = client.get("http://0.0.0.0:8000/get_last_price_by_ticker?ticker=eth_usd")
    assert response.status_code == 200
    assert "result" in response.json()
    assert response.json()["result"]["ticker"] == "eth_usd"


def test_get_currency_price_by_date(client):
    response = client.get(
        "http://0.0.0.0:8000/get_currency_price_by_date?ticker=eth_usd&start_time=20-10-2024&end_time=10-11-2024")
    assert response.status_code == 200
    assert "result" in response.json()
    assert response.json()["result"][0]["ticker"] == "eth_usd"
