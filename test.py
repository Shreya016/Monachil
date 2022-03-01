import unittest
from solution.City import City
from solution.RainData import RainData
from solution.RainDataStorageList import RainDataStorageList
from solution.RainyDatesDS import RainyDatesDS

from solution.Threshold import Threshold

class UnitTests(unittest.TestCase):
    def test_City(self):
        city = City("New York")
        self.assertEqual(city.get_name(), "New York")
        self.assertEqual(city.get_latitude(), "40.7127281")
        self.assertEqual(city.get_longitude(), "-74.0060152")
        self.assertEqual(city.get_coords(), ("40.7127281", "-74.0060152"))
    
    def test_threshold(self):
        thresh = Threshold(0.01, 5.0)
        self.assertEqual(thresh.get_distance_threshold(), 0.01)
        self.assertEqual(thresh.get_rain_threshold(), 5.0)
        thresh = Threshold()
        self.assertEqual(thresh.get_distance_threshold(),0.05)
        self.assertEqual(thresh.get_rain_threshold(),8.0)
    
    def test_rainy_dates_ds(self):
        obj = RainyDatesDS()
        obj.add((1,5))
        obj.add((1,5))
        obj.add((1,5))
        self.assertEqual(len(obj), 3)
        for i in obj:
            self.assertEqual(i, (1,5))
        self.assertEqual(obj.get(0),(1,5))
        
    def test_rain_data_storage_list(self):
        obj = RainDataStorageList()
        self.assertEqual(obj.get_max_capacity(), 10e10)
        obj.add((1,5))
        for i in obj:
            self.assertEqual(i, (1,5))
    
    def test_rain_data(self):
        obj = RainData()
        file_name = "/Users/shreyaarora/Downloads/chirps20GlobalPentadP05_1da0_1624_398c.csv"
        obj.get_from_file(file_name)
        rain_list = obj.get_rain_data()
        for i in rain_list:
            self.assertEqual(i, ['2021-08-01T00:00:00Z','30.024994','-122.975006','NaN'])
            break
        city = City("San Jose")
        obj.process_city_data(city)
        rainy_days_list = obj.get_rainy_days()
        for i in rainy_days_list:
            self.assertEqual(i, ('2021-10-16', '11.689456'))
            break
        obj = RainData()
        obj.get_from_file(file_name)
        rain_list = obj.get_rain_data()
        city = City("Orlando")
        obj.process_city_data(city)
        rainy_days_list = obj.get_rainy_days()
        self.assertEqual(0, len(rainy_days_list))
        for i in rainy_days_list:
            self.assertEqual(i, ('', ''))
            break
        

if __name__ == '__main__':
    unittest.main()