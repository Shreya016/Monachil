from solution.RainyDatesDS import RainyDatesDS

class RainyDaysFormatter:
    def __init__(self, dates: RainyDatesDS):
        self.dates = dates
        pass
        
    def print(self):
        for item in self.dates:
            print(item)
        print("number of rainy 5-days: " + str(len(self.dates)))