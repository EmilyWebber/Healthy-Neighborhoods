import csv
from Neighborhood import Neighborhood
import statistics

class City:

    def __init__(self, filename):
        self.city = {}
        data = []
        with open(filename, 'rU') as f:
            fields = csv.reader(f)
            for row in fields:
                data.append(row)
        self.headers = data[0]
        for row in data[1:]:
            name = row[1]
            self.city[name] = Neighborhood(data[0], row)

    def get_neighborhoods(self, header1, header2):
        '''
        Takes two headers, returns a list of tuples
        With each neighborhood name and its measurement
        '''
        rt = []
        for n in self.city:
            m = self.city[n].get_measurement(header1)
            o = self.city[n].get_measurement(header2)
            rt.append((n, m, o))
        return rt

    def get_values(self, header):
        '''
        Takes itself and a single header, returns a list of all the neighborhood measurements
        '''
        rt = []
        for n in self.city:
            value = float(self.city[n].get_measurement(header))
            rt.append(value)
        return rt

    def get_thresholds(self, header):
        '''
        Return the low, medium, and high thresholds for the neighborhood
        '''
        values = City.get_values(self, header)
        low = float(min(values))
        high = float(max(values))
        mean = float(statistics.mean(values))
        low_mid = float((mean - low)/ 2)
        high_mid = float((high - mean) / 2)
        return [(low, low_mid), (low_mid, high_mid), (high_mid, high)]


    def __str__(self):
        return "So far you've got {} neighborhoods".format(len(self.city))