import csv
import sys
from City import City

FILE = 'city_health_stats.csv'

def go(headers):
    c = City(FILE)
    color_matrix = {}
    for i in headers:
        if i not in c.headers:
            print ("Did not enter a valid header")
            sys.exit(0)
        color_matrix[i] = c.thresholds(i)

if __name__ == "__main__":

    num_args = len(sys.argv)

    if num_args != 3:
        print ("usage: python3 " + sys.argv[0] + " <first header> " + "<second header>")
        sys.exit(0)

    headers = [sys.argv[1], sys.argv[2]

    go(headers)



