# function to turn Community CSV into a dictionary


import csv
import re
from itertools import islice
COORD = 0
COMM = 6
import json

import os

base_path = os.path.dirname(__file__)
FILE = os.path.abspath(os.path.join(base_path, "CommAreas.csv"))


def community_dict (filename):
    '''
    Takes csv and returns dictionary of communities, each with a list of dicts 
    for each point.
    example: 
    {'DOUGLAS': [{'lat': '-87.60914087617012', 'long': '41.8446925034611'},
    {'lat': '-87.60914874756925', 'long': '41.84466159923116'},...]
## It's opposite?
    #header = ['the_geom', 'AREA', 'PERIMETER', 'COMAREA_', 'COMAREA_ID', 'AREA_NUMBE', 'COMMUNITY', 'AREA_NUM_1', 'SHAPE_AREA', 'SHAPE_LEN']


    '''
    comm_dict =  {}
    with open(filename, 'rt') as f:
        fields = csv.reader(f)
        header = next(fields)
        for row in fields:
        # for row in islice(fields, 0, 2):    
            #Use the above if you are just testing with a few rows
            community = row[COMM].title()
            comm_dict[community] = []
            geo = row[COORD]
            bad_char = "MULTIPOLYGON"
            lsd = geo.replace("(", "").replace(")", "")
            cleaned = re.sub(bad_char, '', lsd)
            l = cleaned.split(",")
            for each in l:
                point = {}
                a = each.split()
                lat1 = float(a[1])
                lon2 = float(a[0])
                point['lat'] = lat1
                point['lng'] = lon2
                location_json = json.dumps({"lat": lat1, "lng": lon2})
                comm_dict[community].append(lat1, lon2)
        # print (len(comm_dict))
        return comm_dict 

def main():
    comm_dict = community_dict(FILE)
    ##print(["{}: {}".format(x, len(comm_dict[x])) for x in list(comm_dict.keys())])    
    return comm_dict
'''
if __name__=="__main__":
    main()
    filename = "CommAreas.csv"

    comm_dict = community_dict(filename)
'''

    ##print([len(comm_dict[x]) for x in list(comm_dict.keys())])    