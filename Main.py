from solution.City import City
from solution.RainData import RainData
from solution.RainyDaysFormatter import RainyDaysFormatter


def main():
    file_name = "/Users/shreyaarora/Downloads/chirps20GlobalPentadP05_1da0_1624_398c.csv"
    rain_data_obj = RainData()
    rain_data_obj.get_from_file(file_name)
    city_name = str(input("Enter city name:[San Jose]") or "San Jose")
    city = City(city_name)
    rain_data_obj.process_city_data(city)
    rainy_days = rain_data_obj.get_rainy_days()
    RainyDaysFormatter(rainy_days).print()

if __name__ == '__main__':
    main()