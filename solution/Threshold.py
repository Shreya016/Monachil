class Threshold:

    def __init__(self, dist=0.05, rain=8.0):
        self.distance_threshold = dist
        self.rain_threshold = rain

    def get_distance_threshold(self):
        return self.distance_threshold
    
    def get_rain_threshold(self):
        return self.rain_threshold
    
    def set_distance_threshold(self, dist):
        self.distance_threshold = dist
    
    def set_rain_threshold(self, rain):
        self.rain_threshold = rain