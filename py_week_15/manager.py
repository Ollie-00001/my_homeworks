from json_reader import JSONReader
from cities_serializer import CitiesSerializer
from city_game import CityGame

class GameManager:
    def __init__(self, json_reader: JSONReader, cities_serializer: CitiesSerializer, city_game: CityGame):
        self.json_reader = json_reader
        self.cities_serializer = cities_serializer
        self.city_game = city_game

    def __call__(self):
        self.run_game()