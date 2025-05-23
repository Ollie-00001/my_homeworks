import json
import csv
import yaml
from typing import Any, Optional, List

def read_json(file_path: str, encoding: str = "utf-8") -> Optional[Any]:
    """
    Читает данные из JSON-файла.
    :param file_path: Путь к JSON-файлу.
    :param encoding: Кодировка файла (по умолчанию "utf-8").
    :return: Данные из файла или None, если чтение не удалось.
    """
    try:
        with open(file_path, encoding=encoding) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка чтения JSON-файла {file_path}: {e}")

def write_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Записывает данные в JSON-файл.
    :param data: Данные для записи.
    :param file_path: Путь к файлу.
    :param encoding: Кодировка файла.
    """  
    try:
        with open(file_path, "w", encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except (TypeError, json.JSONDecodeError) as e:
        print(f"Ошибка записи JSON-файла {file_path}: {e}")

def append_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    """
    Добавляет данные в JSON-файл.
    :param data: Данные для добавления.
    :param file_path: Путь к файлу.
    :param encoding: Кодировка файла.
    """
    existing_data = read_json(file_path, encoding) or []
    if not isinstance(existing_data, list):
        print(f"Ошибка: JSON файл {file_path} должен содержать список.")
        return
    existing_data.extend(data)
    write_json(*existing_data, file_path=file_path, encoding=encoding)

def read_csv(file_path: str, delimiter: str = ";", encoding: str = "utf-8-sig") -> Optional[List[List[str]]]:
    """
    Читает данные из CSV-файла.
    :param file_path: Путь к CSV-файлу.
    :param delimiter: Разделитель полей.
    :param encoding: Кодировка файла.
    :return: Данные из файла в виде списка списков строк.
    """   
    try:
        with open(file_path, encoding=encoding) as f:
            return list(csv.reader(f, delimiter=delimiter))
    except (FileNotFoundError, csv.Error) as e:
        print(f"Ошибка чтения CSV-файла {file_path}: {e}")

def write_csv(*data: List[str], file_path: str, delimiter: str = ";", encoding: str = "utf-8-sig") -> None:
    """
    Записывает данные в CSV-файл.
    :param data: Данные для записи.
    :param file_path: Путь к файлу.
    :param delimiter: Разделитель полей.
    :param encoding: Кодировка файла.
    """
    try:
        with open(file_path, "w", encoding=encoding) as f:
            writer = csv.writer(f, delimiter=delimiter)
            writer.writerows(data)
    except csv.Error as e:
        print(f"Ошибка записи CSV-файла {file_path}: {e}")

def append_csv(*data: List[str], file_path: str, delimiter: str = ";", encoding: str = "utf-8-sig") -> None:
    """
    Добавляет данные в CSV-файл.
    :param data: Данные для добавления.
    :param file_path: Путь к файлу.
    :param delimiter: Разделитель полей.
    :param encoding: Кодировка файла.
    """
    try:
        with open(file_path, "a", encoding=encoding) as f:
            writer = csv.writer(f, delimiter=delimiter)
            writer.writerows(data)
    except csv.Error as e:
        print(f"Ошибка добавления данных в CSV-файл {file_path}: {e}")

def read_txt(file_path: str, encoding: str = "utf-8") -> Optional[str]:
    """
    Читает данные из текстового файла
    :param file_path: Путь к файлу.
    :param encoding: Кодировка файла.
    :return: Содержимое файла в виде строки.
    """
    try:
        with open(file_path, encoding=encoding) as f:
            return f.read()
    except (FileNotFoundError, UnicodeDecodeError) as e:
        print(f"Ошибка чтения текстового файла {file_path}: {e}")

def write_txt(*data: str, file_path: str, encoding: str = "utf-8") -> None:
    """
    Записывает данные в текстовый файл.
    :param data: Данные для записи.
    :param file_path: Путь к файлу.
    :param encoding: Кодировка файла.
    """
    try:
        with open(file_path, "w", encoding=encoding) as f:
            f.write(" ".join(data))
    except UnicodeDecodeError as e:
        print(f"Ошибка записи текстового файла {file_path}: {e}")

def append_txt(*data: str, file_path: str, encoding: str = "utf-8") -> None:
    """
    Добавляет данные в конец текстового файла.
    :param data: Данные для добавления.
    :param file_path: Путь к файлу.
    :param encoding: Кодировка файла.
    """
    try:
        with open(file_path, "a", encoding=encoding) as f:
            f.write(" ".join(data) + "\n")
    except UnicodeDecodeError as e:
        print(f"Ошибка добавления данных в текстовый файл {file_path}: {e}")

def read_yaml(file_path: str) -> Optional[Any]:
    """
    Читает данные из YAML-файла.
    :param file_path: Путь к YAML-файлу.
    :return: Данные из файла или None, если чтение не удалось.
    """
    try:
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f"Ошибка чтения YAML-файла {file_path}: {e}")