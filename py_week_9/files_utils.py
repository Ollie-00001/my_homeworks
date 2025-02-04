import json
import csv
import yaml

def read_json(file_path: str, encoding: str = 'utf-8'):
    try:
        with open(file_path, encoding=encoding) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'File {file_path} not found')
    except json.JSONDecodeError:
        print(f'File {file_path} is not a valid JSON')

def write_json(file_path: str, data, encoding: str = 'utf-8') -> None:
    try:
        with open(file_path, 'w', encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=False)
    except json.JSONDecodeError:
        print(f'File {file_path} is not a valid JSON')

def append_json(file_path: str, *data, encoding: str = 'utf-8') -> None:
    try:
        existing_data = read_json(file_path) or []
        if not isinstance(existing_data, list):
            print(f"Warning: JSON file should contain a list to append data.")
            return
        existing_data.extend(data)
        write_json(file_path, existing_data, encoding)
    except json.JSONDecodeError:
        print(f'File {file_path} is not a valid JSON')

def read_csv(file_path: str, delimiter: str = ';', encoding: str = 'utf-8-sig'):
    try:    
        with open(file_path, encoding=encoding) as f:
            return list(csv.reader(f, delimiter=delimiter))
    except FileNotFoundError:
        print(f'File {file_path} not found')
    except csv.Error:
        print(f'File {file_path} is not a valid CSV')
        
def write_csv(*data, file_path: str, delimiter: str = ';', encoding: str = 'utf-8-sig') -> None:
    try:
        with open(file_path, 'w', encoding=encoding) as f:
            writer = csv.writer(f, delimiter=delimiter)
            writer.writerows(data)
    except csv.Error:
        print(f'File {file_path} is not a valid CSV')
        
def append_csv(*data, file_path: str, delimiter: str = ';', encoding: str = 'utf-8-sig') -> None:
    try:
        with open(file_path, 'a', encoding=encoding) as f:
            writer = csv.writer(f, delimiter=delimiter)
            writer.writerows(data)
    except csv.Error:
        print(f'File {file_path} is not a valid CSV')

def read_txt(file_path: str, encoding: str = 'utf-8'):
    try:
        with open(file_path, encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        print(f'File {file_path} not found')
    except UnicodeDecodeError:
        print(f'File {file_path} is not a valid TXT')
    
def write_txt(file_path: str, data, encoding = 'utf-8') -> None:
    try:
        with open(file_path, 'w', encoding=encoding) as f:
            if isinstance(data, (list, tuple)):
                f.write(' '.join(map(str, data)))
            else:
                f.write(str(data))
    except UnicodeDecodeError:
        print(f'File {file_path} is not a valid TXT')

def append_txt(file_path: str, data, encoding='utf-8') -> None:
    try:
        with open(file_path, 'a', encoding=encoding) as f:
            if isinstance(data, (list, tuple)):
                f.write(' '.join(map(str, data)) + '\n')
            else:
                f.write(str(data) + '\n')
    except UnicodeDecodeError:
        print(f'File {file_path} is not a valid TXT')

def read_yaml(file_path: str, encoding: str = 'utf-8'):
    try:
        with open(file_path, encoding=encoding) as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f'File {file_path} not found')
    except yaml.YAMLError:
        print(f'File {file_path} is not a valid YAML')
    except IsADirectoryError:
        print(f'{file_path} is a directory, not a file')
    except ValueError:
        print(f'{file_path} is empty or corrupted')