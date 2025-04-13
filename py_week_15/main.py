from json_reader import JSONReader
from cities_serializer import CitiesSerializer

def main():
    reader = JSONReader('cities.json')
    city_data = reader.read_file()

    serializer = CitiesSerializer(city_data)
    cities = serializer.get_all_cities()

    for city in cities:
        print(city)
    
if __name__ == '__main__':
    main()