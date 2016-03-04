# function to turn Community CSV into a dictionary

#header = ['the_geom', 'AREA', 'PERIMETER', 'COMAREA_', 'COMAREA_ID', 'AREA_NUMBE', 'COMMUNITY', 'AREA_NUM_1', 'SHAPE_AREA', 'SHAPE_LEN']

import csv
import re
from itertools import islice
COORD = 0
COMM = 6

def community_dict (filename):
    '''
    Takes csv and returns dictionary of communities, each with a list of dicts 
    for each point.
    example: 
    {'DOUGLAS': [{'lat': '-87.60914087617012', 'long': '41.8446925034611'},
    {'lat': '-87.60914874756925', 'long': '41.84466159923116'},...]

    '''

    comm_dict =  {}
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        for row in islice(reader,1,2):
            community = row[COMM]
            comm_dict[community] = []
            geo = row[COORD]
            bad_char = "MULTIPOLYGON"
            lsd = geo.replace("(", "").replace(")", "")
            cleaned = re.sub(bad_char, '', lsd)
            l = cleaned.split(",")
            for each in l:
                point = {}
                a = each.split()
                lat1 = a[0]
                lon2 = a[1]
                point["lat"] = lat1
                point["long"] = lon2
                comm_dict[community].append(point)
        return comm_dict
                
if __name__=="__main__":

    filename = "CommAreas.csv"

community_dict(filename)

