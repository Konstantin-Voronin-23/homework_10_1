# Создание функций проекта
from typing import Any, List


def filter_by_state(my_list: List[Any], state: str = 'EXECUTED') -> List[Any]:
    """
    Функция фильтрации списков словарей по ключу
    """
    return [i for i in my_list if i['state'] == state]

# result_1 = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])

# print(result_1)


def sort_by_date(my_list: List[Any], reverse_def: bool = True) -> List[Any]:
    """
    Функция сортировки даты по ключу
    """
    return sorted(my_list, key=lambda date: date.get("date", 0), reverse=reverse_def)

# result_2 = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])

# print(result_2)
