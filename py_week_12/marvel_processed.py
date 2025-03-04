from marvel import full_dict
from pprint import pprint
from typing import List, Dict, Set, Optional

# 2. Получаем список ID фильмов, вводимых пользователем
user_input = input("Введите ID фильмов через пробел: ")
id_list: List[Optional[int]] = list(map(lambda x: int(x) if x.isdigit() else None, user_input.split()))

