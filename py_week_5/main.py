small_dict = {
    'Человек-муравей и Оса: Квантомания': 2023,
    'Стражи Галактики. Часть 3': 2023,
    'Капитан Марвел 2': 2023,
    'Дэдпул 3': 2024,
    'Капитан Америка: Дивный новый мир': 2024,
    'Громовержцы': 2024,
    'Блэйд': 2025,
    'Фантастическая четвёрка': 2025,
    'Мстители: Династия Канга': 2026,
    'Мстители: Секретные войны': 2027,
    'Безымянный фильм о Человеке-пауке': None,
    'Безымянный фильм о Шан-Чи': None,
    'Безымянный фильм о Вечных': None,
    'Безымянный фильм о мутантах': None
}

def search_movies():
    query = input("Введите название фильма или его часть: ").strip().lower()
    found_movies = []

    for movie in small_dict.keys():
        if query in movie.lower():
            found_movies.append(movie)

    if found_movies:
        print("Найденные фильмы:")
        for movie in found_movies:
            print(f"- {movie}")
    else:
        print("Фильмы не найдены.")

def filter_movies_by_year():
    filtered_titles = []
    filtered_dict = {}
    filtered_list_of_dicts = []

    for movie, year in small_dict.items():
        if isinstance(year, int) and year > 2024:
            filtered_titles.append(movie)
            filtered_dict[movie] = year
            filtered_list_of_dicts.append({movie: year})

    print("Фильмы, вышедшие после 2024 года:")
    print("\n".join(filtered_titles) if filtered_titles else "Нет таких фильмов.")

    print("\nСписок названий фильмов:")
    print(filtered_titles)

    print("\nФильтрованный словарь:")
    print(filtered_dict)

    print("\nСписок словарей:")
    print(filtered_list_of_dicts)

if __name__ == "__main__":
    print("Задача 1: Поиск фильмов по названию")
    search_movies()

    print("\nЗадача 2: Фильтрация фильмов по году выхода")
    filter_movies_by_year()