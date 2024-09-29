# course_2_3_home_works

## Описание

Проект course_2_3_home_work - это проект с домашними заданиями за второй и третий курс

## Возможности проекта
1. Маскировка номера карты и счета
2. Чтение данных из JSON файлов
3. Выводить сумму транзакций в рублях
4. Чтение данных из csv и xlsx файлов
5. Фильтрация по ключевым словам, валюте, времени

## Тестирование
Проект покрыт pytest. Для их запуска выполните команду:
```
poetry run pytest --cov

```

## Установка 
1. Клонируйте репозиторий:
```
git clone https://github.com/Aleksey-Milyaev/cours_2_home_work.git
```
2. Установите зависимости:
```
poetry install
```

## Использование:
При запуске проекта:
1. Выберите тип файла, для чтения транзакций
2. Выберите тип фильтрации: по дате, по операциям в рублях, по ключевому слову
3. Программа выводит на экран результат вашего запроса


## Документация:
Проект автоматически записывает лог файлы модулей: utils, masks. Которые можно 
посмотреть в папке logs: utils.log, masks.log  