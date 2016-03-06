import csv
import sys
import City
import support
##import statistics
import csv
import os

base_path = os.path.dirname(__file__)
FILE = os.path.abspath(os.path.join(base_path, "Data/city_health_stats.csv" ))
##FILE = 'Data/city_health_stats.csv'
DEFAULT_KEY = None
DEFAULT_VALUE = []


def get_headers(filename = FILE):
    '''
    Takes a filename, returns a list of the column headers
    '''
    with open(filename, 'rU') as f:
        fields = csv.reader(f)
        cols =  next(fields)
    return cols[2:]

def initialize_city_dict(headers):
    '''
    Takes a list of headers, creates an inner dictionary for each variable
    With every other variable and the default key 
    '''
    city = {}
    for i in headers:
        other = [x for x in headers if x != i]
        inner = {DEFAULT_KEY:DEFAULT_VALUE}
        for each in other:
            inner[each] = DEFAULT_VALUE
        city[i] = inner
    return city

def populate_city(filename):
    city_class = City.City(filename)
    headers = city_class.get_headers()
    city_dict = initialize_city_dict(headers)
    recurse_through_city(city_dict, city_class, 0)
    return city_dict

def recurse_through_city(city_dict, city_class, level):

    headers = list(city_dict.keys())

    level += 1
    
    if level == 2:
        return headers

    for i in headers:
        lower = recurse_through_city(city_dict[i], city_class, level)
        for each in lower:
            found = city_dict[i][each]
            if found == DEFAULT_VALUE:
                city_dict[i][each] = assign_neighborhoods(city_class, i, each)

    return headers


# I'm not happy with this implementation - I don't think it's necessary to compute
# the thresholds every time we assign neighborhoods.
# I think it would be better to compute this when initializing the city, drop it off in a dict,
# And then just reference it here

def assign_neighborhoods(city_class, header1, header2):
    '''
    Takes an instance of the class City and two headers,
    Calls City.get_neighborhoods and walks through the list of return tuples,
    Checking threshold values and assigning a low, medium, or high tag to the measurement
    Uses both tags to assign a color
    Returns a list of tuples of neighborhoods and their color assignment
    '''   
    rt = []
    thresholds1 = city_class.get_thresholds(header1)

    if header2 == DEFAULT_KEY:
        for n, m in city_class.get_neighborhoods(header1, header2):
            for idx, (low, high) in enumerate(thresholds1):
                if (m >= low) and (m <= high):
                    m_idx = support.index_matrix[idx]
            color = support.color_matrix[(m_idx, DEFAULT_KEY)]
            rt.append((n, color))
        return rt


    thresholds2 = city_class.get_thresholds(header2)
    for n, m1, m2 in city_class.get_neighborhoods(header1, header2):

        for idx, (low, high) in enumerate(thresholds1):
            if (m1 >= low) and (m1 <= high):
                m1_idx = support.index_matrix[idx]
        
        for idx, (low, high) in enumerate(thresholds2):
            if (m2 >= low) and (m2 <= high):
                m2_idx = support.index_matrix[idx]

        color = support.color_matrix[(m1_idx, m2_idx)]
        rt.append((n, color))

    return rt

'''
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    else:
        variable_dict = populate_city(FILE)
        print(variable_dict[sys.argv[1]][sys.argv[2]])
        ## Prints list of tuples ("neighborhood name", color value)
'''
def main(variable_1, variable_2 = None):
    variable_dict = populate_city(FILE)
    return variable_dict[variable_1][variable_2]
