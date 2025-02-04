import json
from typing import Any, Optional, List

def read_json(file_path: str, encoding: str = "utf-8") -> Optional[Any]:
    try:
        with open(file_path, encoding=encoding) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка чтения JSON-файла {file_path}: {e}")

def write_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    try:
        with open(file_path, "w", encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except (TypeError, json.JSONDecodeError) as e:
        print(f"Ошибка записи JSON-файла {file_path}: {e}")

def append_json(*data: dict, file_path: str, encoding: str = "utf-8") -> None:
    existing_data = read_json(file_path, encoding) or []
    if not isinstance(existing_data, list):
        print(f"Ошибка: JSON файл {file_path} должен содержать список.")
        return
    existing_data.extend(data)
    write_json(*existing_data, file_path=file_path, encoding=encoding)

