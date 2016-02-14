import csv
import sys

FILE = 'city_health_stats.csv'

def generate_correlations():

	with open(FILE, 'rb') as f:
		data = csv.reader(f)
		for row in data:
			print (row)


if __name__ == "__main__":
	generate_correlations()
