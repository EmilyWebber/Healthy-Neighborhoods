import csv
from Neighborhood import Neighborhood

class City:

    def __init__(self, filename):
        self.city = {}
        data = []
        with open(filename, 'rU') as f:
            fields = csv.reader(f)
            for row in fields:
                data.append(row)
        self.headers = data[1]
        for row in data[1:]:
            name = row[1]
            self.city[name] = Neighborhood(self.headers, row)

    def thresholds(self, header):
        '''
        Takes a header, returns a list of tuples demarking the high, medium, and low thresholds
        '''
        rt = []
        for n in self.city.keys():
            found = n[header]
            if type(found) == float:
                rt.append(found)
        rt.sort()




    def __str__(self):
        return "So far you've got {} neighborhoods".format(len(self.city))