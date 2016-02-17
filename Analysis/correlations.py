import csv
import sys
from City import City
import constant_data_structures
import statistics

FILE = 'city_health_stats.csv'
L = "l"
M = "m"
H = "h"


def go(header1, header2):
    c = City(FILE)
    thresholds1 = c.get_thresholds(header1)
    thresholds2 = c.get_thresholds(header2)

    
if __name__ == "__main__":
    num_args = len(sys.argv)

    if num_args != 3:
        print ("usage: python3 " + sys.argv[0] + " <first header> " + "<second header>")
        sys.exit(0)
    
    headers = [sys.argv[1], sys.argv[2]]
    
    for h in headers:
        if h not in constant_data_structures.valid_headers:
            print ("Did not enter a valid header")
            sys.exit(0)

    print (go(headers[0], headers[1]))