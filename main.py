# Импорты
import os

from src.utils import get_operations_list
from src.reader_csv_xlsx import read_operation_csv, read_operation_xlsx
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.search import search_by_word
from src.widget import get_date, mask_account_card

# Путь до папки "data"
PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "data")

if __name__ == "__main__":
    # Приветствие и выбор формата файла
    getting_information_from = int(
        input(
            """Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
        )
    )

    if getting_information_from == 1:
        print("Для обработки выбран JSON-файл.")
        transactions = get_operations_list(os.path.join(PATH_TO_FILE, "operations.json"))

    elif getting_information_from == 2:
        print("Для обработки выбран CSV-файл.")
        transactions = read_operation_csv(os.path.join(PATH_TO_FILE, "transactions.csv"))

    elif getting_information_from == 3:
        print("Для обработки выбран XLSX-файл.")
        transactions = read_operation_xlsx(os.path.join(PATH_TO_FILE, "transactions_excel.xlsx"))

    else:
        print("Некорректный ввод")
    # Выбор фильтрации по статусу
    while True:
        status_filter = input(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        )

        if status_filter.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print(f"Статус операции '{status_filter.upper()}' недоступен.")
            continue

    filter_transactions = filter_by_state(transactions, status_filter.upper())
    # Сортировка по дате
    sorted_date = input("Отсортировать операции по дате? Да/Нет\n")

    if sorted_date.lower() == "да":
        revers = input("Отсортировать по возрастанию или по убыванию?\n")

        if revers.lower() == "по возрастанию":
            transaction_sorted_date = sort_by_date(filter_transactions, False)
        elif revers.lower() == "по убыванию":
            transaction_sorted_date = sort_by_date(filter_transactions)
        else:
            print("Некорректный ввод сортировка по умолчанию( по убыванию)")
            transaction_sorted_date = sort_by_date(filter_transactions)
    else:
        transaction_sorted_date = filter_transactions
    # Фильтрация по операциям в рублях
    filter_by_rub = input("Выводить только рублевые транзакции? Да/Нет\n")

    if filter_by_rub.lower() == "да":
        transactions_rub = filter_by_currency(transaction_sorted_date, "RUB")

    else:
        transactions_rub = transaction_sorted_date

    # Фильтрация по ключевому слову
    filter_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if filter_by_word.lower() == "да":
        user_word = input("Введите слово")
        search_in_transactions = search_by_word(transactions_rub, user_word)
    else:
        search_in_transactions = transactions_rub
    # Результат
    print("Распечатываю итоговый список транзакций...\n")

    if not search_in_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
      #  print(f"Всего банковских операций в выборке: {(search_in_transactions)}")

        for transaction in search_in_transactions:
            transaction["date"] = get_date(transaction["date"])

            try:
                if transaction["description"] == "" "Открытие вклада":
                    print(
                        f"{transaction['date']}\nОткрытие вклада\n{mask_account_card(transaction['to'])}\nСумма: "
                        f"{transaction['amount']} {transaction['currency_name']}\n"
                    )
            except KeyError:
                print(
                    f"{transaction['date']}\nОткрытие вклада\n{mask_account_card(transaction['to'])}\nСумма:"
                    f" {transaction["operationAmount"]['amount']} {transaction["operationAmount"]["currency"]["name"]}\n"
                )

            try:
                if transaction['description'] in ["Перевод организации","Перевод с карты на карту",
                                                  "Перевод со счета на счет", "Перевод с карты на счет"]:
                    print(f"{transaction['date']} {transaction['description']}\n{mask_account_card(transaction['to'])} "
                          f"-> {mask_account_card(transaction['from'])}\nСумма: {transaction['amount']}"
                          f" {transaction['currency_name']}\n")
            except KeyError:
                print(f"{transaction['date']} {transaction['description']}\n{mask_account_card(transaction['to'])} "
                      f"-> {mask_account_card(transaction['from'])}\nСумма: {transaction["operationAmount"]['amount']}"
                      f" {transaction["operationAmount"]["currency"]["name"]}\n")

############################################################################