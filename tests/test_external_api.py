import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_transaction_amount


@patch("requests.get")
def test_get_transaction_amount(mock_get):
    """Тест функции принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    load_dotenv()
    api_key = os.getenv("APILayer")
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 9824.07},
        "info": {"timestamp": 1727427784, "rate": 92.796296},
        "date": "2024-09-27",
        "result": 911637.307645,
    }
    assert (
        get_transaction_amount(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            }
        )
        == 911637.31
    )
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37",
        headers={"apikey": api_key},
    )


def test_a():
    assert (
        get_transaction_amount(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            }
        )
        == 31957.58
    )
