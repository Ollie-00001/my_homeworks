import json

def read_json(file_path: str, encoding: str = 'utf-8'):
    with open(file_path, encoding=encoding) as f:
        return json.load(f)

def write_json(file_path: str, data, encoding: str = 'utf-8'):
    with open(file_path, 'w', encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False)