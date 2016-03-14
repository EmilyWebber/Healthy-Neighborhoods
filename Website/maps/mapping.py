# function to turn Community CSV into a dictionary


import csv
import re
import json
import os

COORD = 0
COMM = 6


base_path = os.path.dirname(__file__)
FILE = base_path + "/static/maps/Data/CommAreas.csv"


def community_dict (filename):
    '''
    Takes csv and returns dictionary of communities, each with a list of dicts 
    for each point.
    example: 
    {'DOUGLAS': [{'long': '-87.60914087617012', 'lat': '41.8446925034611'},
    {'long': '-87.60914874756925', 'lat': '41.84466159923116'},...]
    #header = ['the_geom', 'AREA', 'PERIMETER', 'COMAREA_', 'COMAREA_ID', 'AREA_NUMBE', 'COMMUNITY', 'AREA_NUM_1', 'SHAPE_AREA', 'SHAPE_LEN']
    '''

    comm_dict =  {}
    with open(filename, 'rt') as f:
        fields = csv.reader(f)
        header = next(fields)

        for row in fields:
            community = row[COMM].title()
            cords = []

            geo = row[COORD]
            bad_char = "MULTIPOLYGON"
            lsd = geo.replace("(", "").replace(")", "")
            cleaned = re.sub(bad_char, '', lsd)
            l = cleaned.split(",")
            
            ## Correction for capitalization
            if community == "Mckinley Park":
                community = "McKinley Park"

            if community == "Norwood Park":
                l = l [:1328]
                ## Correction for empty space (partition of Norridge)
            if community == "Ohare":
                community = "O'Hare"
                l = l[:-197]
                ## Correction for empty space (O'Hare jetty)
            
            for each in l:
                cord_pair = each.split()
                lat = float(cord_pair[1])
                lon = float(cord_pair[0])

                cords.append([lat, lon])
            comm_dict[community] = {"cords": cords}

    return comm_dict 


def main():
    comm_dict = community_dict(FILE)
    return comm_dict