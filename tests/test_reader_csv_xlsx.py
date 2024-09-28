import csv
import os

from src.reader_csv_xlsx import read_operation_xlsx, read_operation_csv
from unittest.mock import patch
import pandas as pd


@patch("csv.DictReader")
def test_read_operation_csv(mock_read):
    mock_read.return_value = ""

    assert read_operation_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")) == {"Yes": 20, "No": 11}
