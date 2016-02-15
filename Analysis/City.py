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
        headers = data[1]
        for row in data[1:]:
            name = row[1]
            self.city[name] = Neighborhood(headers, row)

    def __str__(self):
        return "So far you've got {} neighborhoods".format(len(self.city))