import json
from typing import Any, List

class JSONReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_file(self) -> List[dict[str, Any]]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            print(f'File {self.file_path} not found')
            return []
        except json.JSONDecodeError:
            print(f'Error decoding JSON in file {self.file_path}')
            return []
        except Exception as e:
            print(f'Error reading file {self.file_path}: {e}')
            return []