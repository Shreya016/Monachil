from solution.CSVDataReader import CSVDataReader

class ParseFile:
    def get_reader(self, csv_file):
        return CSVDataReader().read(csv_file)