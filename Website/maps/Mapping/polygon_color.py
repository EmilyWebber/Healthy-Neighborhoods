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
            cords = []

            geo = row[COORD]
            bad_char = "MULTIPOLYGON"
            lsd = geo.replace("(", "").replace(")", "")
            cleaned = re.sub(bad_char, '', lsd)
            l = cleaned.split(",")
            if community == "Mckinley Park":
                community = "McKinley Park"

            if community == "Norwood Park":
                l = l [:1328]
                ##(correction for empty space in polygon AKA annexation of norridge
            if community == "Ohare":
                community = "O'Hare"
                l = l[:-197]
                ## correction for empty space in polygon AKA RIP Groot industries
            for each in l:

                a = each.split()
                lat = float(a[1])
                lon = float(a[0])

                cords.append([lat, lon])
            comm_dict[community] = {"cords": cords}
        # print (len(comm_dict))
        return comm_dict 

def main():
    comm_dict = community_dict(FILE)
    ##print(["{}: {}".format(x, len(comm_dict[x])) for x in list(comm_dict.keys())])    
    ##return json.dumps(comm_dict)
    return comm_dict
'''
if __name__=="__main__":
    main()
    filename = "CommAreas.csv"

    comm_dict = community_dict(filename)
'''
    ##print([len(comm_dict[x]) for x in list(comm_dict.keys())])   

def get_len(comm_dict):
    community = "Norwood Park"
    coord_list = comm_dict[community]["cords"]
    for i, x in enumerate(coord_list):
        if (41.97 < x[0] < 42):
            print("[{}]: {}  --  {}  --  {}".format(i, coord_list[i - 1], coord_list[i], coord_list[i+1]))

 