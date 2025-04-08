import json

def read_json_file(file_path="operations.json") -> list[dict]:
    """Функция для чтения json файла с операциями транзакций"""
    try:
        with open("operations.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as error:
        print(f"Ошибка: файл {file_path} не найден! ")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: файл {file_path} содержит некорректный JSON! ")
        return None
