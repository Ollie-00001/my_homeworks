import json
import os
from typing import Any
from abc import ABC, abstractmethod

class AbstractFile(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def append(self, data):
        pass

class JsonFile(AbstractFile):
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
    
    def write(self, data: Any) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    def append(self, data: Any) -> None:
        if os.path.exists(self.file_path):
            content = self.read()
            if isinstance(content, list):
                content.append(data)
            else:
                content = [content, data]
        else:
            content = [data]
        self.write(content)

class TxtFile(AbstractFile):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> str:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def write(self, data: str) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(data)

    def append(self, data: str) -> None:
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(data)

class CsvFile(AbstractFile):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> list[list[str]]:
        with open(self.file_path, 'r', newline='', encoding='utf-8') as f:
            return list(csv.reader(f))

    def write(self, data: list[list[str]]) -> None:
        with open(self.file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    def append(self, data: list[str]) -> None:
        with open(self.file_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data)