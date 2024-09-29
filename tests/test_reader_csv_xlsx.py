import os
from unittest.mock import Mock, patch

import pandas as pd

from src.reader_csv_xlsx import read_operation_csv, read_operation_xlsx


@patch("csv.DictReader")
def test_read_operation_csv(mock_read):
    """Тест функции считывания операций из файла.csv"""
    mock_read.return_value = iter(
        [
            {"id": 650703, "state": "EXECUTED", "amount": 16210.0},
            {"id": 3598919, "state": "EXECUTED", "amount": 29740.0},
        ]
    )

    assert read_operation_csv(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
    ) == [
        {"id": 650703, "state": "EXECUTED", "amount": 16210.0},
        {"id": 3598919, "state": "EXECUTED", "amount": 29740.0},
    ]
    mock_read.assert_called_once()

    assert read_operation_csv() == []


def test_read_operation_xlsx():
    """Тест функции считывания операций из файла.xlsx"""
    mock_read = Mock(
        return_value=pd.DataFrame(
            {"id": [650703, 3598919], "state": ["EXECUTED", "EXECUTED"], "amount": [16210.0, 29740.0]}
        )
    )
    pd.read_excel = mock_read
    assert read_operation_xlsx(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")
    ) == [
        {"id": 650703, "state": "EXECUTED", "amount": 16210.0},
        {"id": 3598919, "state": "EXECUTED", "amount": 29740.0},
    ]
    mock_read.assert_called_once()
