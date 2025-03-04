from marvel import full_dict
from pprint import pprint
from typing import List, Dict, Set, Optional


user_input = input("Введите ID фильмов через пробел: ")
id_list: List[Optional[int]] = list(map(lambda x: int(x) if x.isdigit() else None, user_input.split())) # Получаем список ID фильмов, вводимых пользователем

movies_list: List[Dict] = [{"id": key, **value} for key, value in full_dict.items()] # Перепакуем full_dict в список словарей