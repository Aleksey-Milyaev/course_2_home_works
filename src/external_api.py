import json
import os
from typing import Any

import requests
from dotenv import load_dotenv


def get_transaction_amount(transaction: dict) -> Any:
    """Функция, принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = transaction["operationAmount"]

    if amount["currency"]["code"] != "RUB":
        load_dotenv()
        api_key = os.getenv("APILayer")
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={amount['currency']['code']}"
            f"&amount={amount['amount']}"
        )
        response = requests.get(url, headers={"apikey": api_key}).json()
        json.dumps(response)
        return round(response["result"], 2)

    return float(amount["amount"])
