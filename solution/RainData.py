from solution.ParseFile import ParseFile
from solution.RainDataStorageList import RainDataStorageList
from solution.RainyDatesDS import RainyDatesDS
from solution.City import City
from solution.Threshold import Threshold

class RainData:
    def __init__(self):
        super().__init__()
        self.rain_data = RainDataStorageList()
        self.rainy_days = RainyDatesDS()
        self.thresh = Threshold()

    def get_from_file(self, filename: str):
        with open(filename) as csv_file:
            rain_data_reader = ParseFile().get_reader(csv_file)
            line_count = 0
            for row in rain_data_reader:
                line_count += 1
                if line_count <= 2:
                    # print(f'Column names are {", ".join(row)}')
                    continue
                elif line_count >= self.rain_data.get_max_capacity():
                    break
                self.rain_data.add(row)
    
    def get_rain_data(self):
        return self.rain_data
    
    def process_city_data(self, city: City):
        for row in self.rain_data:
            t, lat, lon, rain = row
            t = t[:10]
            lat_diff = abs(float(lat) - float(city.get_latitude()))
            lon_diff = abs(float(lon) - float(city.get_longitude()))
            if rain != "NaN":
                if float(rain) >= self.thresh.get_rain_threshold():
                    if lat_diff < self.thresh.get_distance_threshold():
                        if lon_diff < self.thresh.get_distance_threshold():
                            self.rainy_days.add((t, rain))
    
    def get_rainy_days(self):
        return self.rainy_days