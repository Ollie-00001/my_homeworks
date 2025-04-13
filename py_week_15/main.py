from json_reader import JSONReader
from cities_serializer import CitiesSerializer

def main():
    reader = JSONReader('C:\Main\my_projects\python_413\my_homeworks\py_week_15\cities.json')
    city_data = reader.read_file()

    serializer = CitiesSerializer(city_data)
    cities = serializer.get_all_cities()

    for city in cities:
        print(city)
    
if __name__ == '__main__':
    main()