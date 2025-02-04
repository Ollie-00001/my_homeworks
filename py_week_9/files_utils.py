import json
import csv

def read_json(file_path: str, encoding: str = 'utf-8'):
    with open(file_path, encoding=encoding) as f:
        return json.load(f)

def write_json(file_path: str, data, encoding: str = 'utf-8'):
    with open(file_path, 'w', encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False)

def append_json(*data, file_path: str, encoding: str = 'utf-8'):
    with open(file_path, 'a', encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False)

def read_csv(file_path: str, delimiter: str = ';', encoding: str = 'utf-8'):
    with open(file_path, encoding=encoding) as f:
        return list(csv.reader(f, delimiter=delimiter))
    
def write_csv(*data, file_path: str, delimiter: str = ';', encoding: str = 'utf-8'):
    with open(file_path, 'w', encoding=encoding) as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerows(data)
        
