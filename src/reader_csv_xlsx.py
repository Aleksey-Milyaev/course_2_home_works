import csv

import pandas as pd


def read_operation_csv(file_path: str = "") -> list:
    """Функция считывания операций из файла.csv"""
    try:
        with open(file_path, encoding="UTF8") as file:
            reader_csv = csv.DictReader(file, delimiter=";")
            transactions_dict = [row for row in reader_csv]
        return transactions_dict
    except FileNotFoundError:
        return []


def read_operation_xlsx(file_path: str = "") -> list:
    """Функция считывания операций из файла.xlsx"""
    try:
        transactions = pd.read_excel(file_path)
        transactions_dict = transactions.to_dict(orient="records")
        return transactions_dict
    except FileNotFoundError:
        return []
