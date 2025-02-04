import json
from typing import Any, Optional, List

def read_json(file_path: str, encoding: str = "utf-8") -> Optional[Any]:
    try:
        with open(file_path, encoding=encoding) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка чтения JSON-файла {file_path}: {e}")
