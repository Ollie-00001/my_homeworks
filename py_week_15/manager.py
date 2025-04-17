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

    def run_game(self):
        print("Добро пожаловать в игру 'Города'!")
        while True:
            player_input = input("Введите название города: ").strip().lower()
            if not self.city_game.human_turn(player_input):
                print("Неверный ввод. Попробуйте снова.")
                break
    
            if self.city_game.check_game_over():
                print("Поздравляем! Вы победили, у компьютера закончились варианты.")
                break

            if self.city_game.computer_turn() is None:
                print("Вы выиграли! Компьютер не смог назвать город.")
                break

            if self.city_game.check_game_over():
                print("Компьютер выиграл. У вас больше нет возможных ходов.")
                break
            