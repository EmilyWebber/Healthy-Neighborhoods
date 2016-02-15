import csv
import sys

FILE = 'city_health_stats.csv'

def read_file(FILE):
    data = []
    with open(FILE, 'rU') as f:
        fields = csv.reader(f)
        for row in fields:
            data.append(row) 
    return data[0], data[1:]         
    

if __name__ == "__main__":
	
    headers, fields = read_file(FILE)

