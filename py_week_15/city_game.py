import random
from typing import Optional
from cities_serializer import CitiesSerializer
from city import City

class CityGame:
    def __init__(self, cities_serializer: CitiesSerializer) -> None:
        self.all_cities: list[City] = cities_serializer.get_all_cities()
        self.available_cities: list[City] = self.all_cities.copy()
        self.used_cities: list[City] = []
        self.last_letter: Optional[str] = None
    
    def is_valid_city(self, city: City) -> Optional[City]:
        for city in self.available_cities:
            if city.name.lower() == city.name.lower()[::-1]:
                return city
        return None
    
    def get_last_letter(self, name: str) -> Optional[str]:
        for char in reversed(name.lower()):
            if char.isalpha():
                return char
        return ''
    
    def human_turn(self, city_input: str) -> bool:
        city = self._is_valid_city(city_input)
        if not city:
            print("❌ Такого города нет в списке или он уже использован.")
            return False

        if self.last_letter and not city.name.lower().startswith(self.last_letter):
            print(f"❌ Город должен начинаться на букву '{self.last_letter.upper()}'.")
            return False

        self.available_cities.remove(city)
        self.used_cities.append(city)
        self.last_letter = self._get_last_letter(city.name)
        print(f"✅ Вы выбрали город: {city.name}")
        return True
    
    def computer_turn(self) -> Optional[str]:
        for city in self.available_cities:
            if city.name.lower().startswith(self.last_letter):
                self.available_cities.remove(city)
                self.used_cities.append(city)
                self.last_letter = self._get_last_letter(city.name)
                print(f"🤖 Компьютер называет: {city.name}")
                return city.name
        print("🤖 Компьютер не может продолжить игру.")
        return None

    def check_game_over(self) -> bool:
        for city in self.available_cities:
            if not self.last_letter or city.name.lower().startswith(self.last_letter):
                return False
        return True