from solution.IDataReader import IDataReader
import csv

class CSVDataReader(IDataReader):
	def read(self, csv_file):
		reader = csv.reader(csv_file, delimiter=",")
		return reader