import csv
import sys
from City import City


FILE = 'city_health_stats.csv'
      
    

if __name__ == "__main__":

    c = City(FILE)
    print (c)
