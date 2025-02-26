import csv
import json
import os

class TxtFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return "Файл не найден"
        except Exception as e:
            return f"Ошибка при чтении: {e}"

    def write(self, data):
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write(str(data))
            return "Запись выполнена успешно"
        except Exception as e:
            return f"Ошибка при записи: {e}"

    def append(self, data):
        try:
            with open(self.filename, 'a', encoding='utf-8') as file:
                file.write(str(data) + '\n')
            return "Добавление выполнено успешно"
        except Exception as e:
            return f"Ошибка при добавлении: {e}"

