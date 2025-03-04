from marvel import full_dict
from pprint import pprint
from typing import List, Dict, Set, Optional


user_input = input("Введите ID фильмов через пробел: ")
id_list: List[Optional[int]] = list(map(lambda x: int(x) if x.isdigit() else None, user_input.split())) # Получаем список ID фильмов, вводимых пользователем

movies_list: List[Dict] = [{"id": key, **value} for key, value in full_dict.items()] # Перепакуем full_dict в список словарей

filtered_movies: List[Dict] = list(filter(lambda movie: movie["id"] in id_list, movies_list)) # Фильтрация словарей по ID из user_input

unique_directors: Set[str] = {movie["director"] for movie in movies_list if "director" in movie} # Множество уникальных режиссёров

full_dict_str_year: Dict[int, Dict] = {key: {**value, "year": str(value["year"])} for key, value in full_dict.items()} # Создание копии full_dict с преобразованием 'year' в строку

filtered_by_letter: List[Dict] = list( 
    filter(lambda movie: isinstance(movie, dict) and movie.get("title") and movie["title"].startswith("Ч"), movies_list)  # Фильтрация фильмов, начинающихся на 'Ч'
)

sorted_by_year: List[Dict] = sorted(
    movies_list,
    key=lambda x: int(x['year']) if isinstance(x['year'], str) and x['year'].isdigit() else float('inf')  # Сортировка по одному параметру (например, по году выпуска)
)