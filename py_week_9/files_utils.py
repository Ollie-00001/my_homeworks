import json

def read_json(file_path: str, encoding: str = 'utf-8'):
    with open(file_path, encoding=encoding) as f:
        return json.load(f)

