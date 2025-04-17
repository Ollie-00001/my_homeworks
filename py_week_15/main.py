from json_reader import JSONReader
from cities_serializer import CitiesSerializer
from city_game import CityGame
from manager import GameManager

def main():
    json_file = JSONReader("C:\Main\my_projects\python_413\my_homeworks\py_week_15\cities.json")
    cities_data = json_file.read_file()
    cities_serializer = CitiesSerializer(cities_data)
    city_game = CityGame(cities_serializer)
    game_manager = GameManager(json_file, cities_serializer, city_game)
    game_manager()

if __name__ == "__main__":
    main()