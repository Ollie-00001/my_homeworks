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

class CSVFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            return "Файл не найден"
        except Exception as e:
            return f"Ошибка при чтении: {e}"

    def write(self, data):
        if not data or not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
            return "Данные должны быть списком словарей"
        try:
            with open(self.filename, 'w', encoding='utf-8', newline='') as file:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            return "Запись выполнена успешно"
        except Exception as e:
            return f"Ошибка при записи: {e}"

    def append(self, data):
        if not data or not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
            return "Данные должны быть списком словарей"
        try:
            existing_data = []
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    existing_data = list(reader)

            combined_data = existing_data + data
            with open(self.filename, 'w', encoding='utf-8', newline='') as file:
                fieldnames = combined_data[0].keys() if combined_data else data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(combined_data)
            return "Добавление выполнено успешно"
        except Exception as e:
            return f"Ошибка при добавлении: {e}"
        
class JSONFileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return "Файл не найден"
        except Exception as e:
            return f"Ошибка при чтении: {e}"

    def write(self, data):
        if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
            return "Данные должны быть списком словарей"
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            return "Запись выполнена успешно"
        except Exception as e:
            return f"Ошибка при записи: {e}"

    def append(self, data):        
        if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
            return "Данные должны быть списком словарей"
        try:
            existing_data = []
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    existing_data = json.load(file)
                    if not isinstance(existing_data, list):
                        existing_data = []

            combined_data = existing_data + data

            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(combined_data, file, ensure_ascii=False, indent=4)
            return "Добавление выполнено успешно"
        except Exception as e:
            return f"Ошибка при добавлении: {e}"
        
if __name__ == "__main__":
    txt_handler = TxtFileHandler("test.txt")
    print(txt_handler.write("Первая строка"))
    print(txt_handler.append("Вторая строка"))
    print(txt_handler.read())

    csv_handler = CSVFileHandler("test.csv")
    csv_data = [{"name": "Егор", "age": "22"}, {"name": "Алина", "age": "21"}]
    print(csv_handler.write(csv_data))
    print(csv_handler.append([{"name": "Иван", "age": "25"}]))
    print(csv_handler.read())

    json_handler = JSONFileHandler("test.json")
    json_data = [{"id": 1, "title": "Book"}, {"id": 2, "title": "Pen"}]
    print(json_handler.write(json_data))
    print(json_handler.append([{"id": 3, "title": "Notebook"}]))
    print(json_handler.read())