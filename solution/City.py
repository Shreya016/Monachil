from solution.NetworkRequest import NetworkRequest

class City:
    def __init__(self, name):
        self.name = name
        self.latitude, self.longitude = self.get_coords()
    
    def get_coords(self):
        try:
            city_data = NetworkRequest().get(
                f"https://nominatim.openstreetmap.org/search.php?city={self.name}&format=jsonv2&namedetails=0&addressdetails=0&limit=1"
            )
            latitude = city_data[0]["lat"]
            longitude = city_data[0]["lon"]
        except Exception as ex:
            latitude = 0
            longitude = 0
        finally:
            return (latitude, longitude)

    def get_latitude(self):
        return self.latitude
    
    def get_longitude(self):
        return self.longitude
    
    def get_name(self):
        return self.name