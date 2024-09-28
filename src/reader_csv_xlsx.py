import csv

import pandas as pd
import os


def read_operation_csv(file_path: str="") -> list:
    """Функция считывания операций из файла.csv"""
    with open(file_path, encoding="UTF8") as file:
        reader_csv = csv.DictReader(file, delimiter=";")
        transactions_dict = [row for row in reader_csv]
    return transactions_dict


def read_operation_xlsx(file_path: str) -> list:
    """Функция считывания операций из файла.xlsx"""
    transactions = pd.read_excel(file_path)
    transactions_dict = transactions.to_dict(orient='records')
    return transactions_dict


print(read_operation_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")))