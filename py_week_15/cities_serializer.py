from typing import List
from city import City

class CitiesSerializer:
    def __init__(self, city_data: List[dict]):
        self.cities: List[City] = []

        for entry in city_data:
            try:
                city = City(
                    name=entry['name'],
                    population=entry['population'],
                    subject=entry['subject'],
                    district=entry['district'],
                    latitude=float(entry['coords']['lat']),
                    longitude=float(entry['coords']['lon'])
                )
                self.cities.append(city)
            except (ValueError, KeyError) as e:
                print(f"Failed creating City: {e}")
    def get_all_cities(self) -> List[City]:
        return self.cities