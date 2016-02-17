import csv
import sys
from City import City
import support
import statistics

FILE = 'city_health_stats.csv'

def switch_measurement_for_threshold_assignment(city, neighborhoods, header1, header2):
    '''
    Walk through a list of tuples (neighborhood, m1, m2) and switch out the measurement 
    For it's threshold assignment
    '''   
    rt = []
    thresholds1 = city.get_thresholds(header1)
    thresholds2 = city.get_thresholds(header2)

    for n, m1, m2 in neighborhoods:

        for idx, (low, high) in enumerate(thresholds1):
            if (m1 >= low) and (m1 <= high):
                m1_idx = support.index_matrix[idx]
        
        for idx, (low, high) in enumerate(thresholds2):
            if (m2 >= low) and (m2 <= high):
                m2_idx = support.index_matrix[idx]

        color = support.color_matrix[(m1_idx, m2_idx)]
        rt.append((n, color))

    return rt

def go(header1, header2):
    c = City(FILE)
    neighborhoods = c.get_neighborhoods(header1, header2)
    neighborhoods = switch_measurement_for_threshold_assignment(c, neighborhoods, header1, header2)
    print (neighborhoods)

    
if __name__ == "__main__":
    num_args = len(sys.argv)

    if num_args != 3:
        print ("usage: python3 " + sys.argv[0] + " <first header> " + "<second header>")
        sys.exit(0)
    
    headers = [sys.argv[1], sys.argv[2]]
    
    for h in headers:
        if h not in support.valid_headers:
            print ("Did not enter a valid header")
            sys.exit(0)

    go(headers[0], headers[1])
