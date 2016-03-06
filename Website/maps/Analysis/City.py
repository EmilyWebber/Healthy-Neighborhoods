import csv
from Neighborhood import Neighborhood
#import statistics

DEFAULT_KEY = None


class City:

    def __init__(self, filename):
        self.neighborhoods = {}

        data = []
        with open(filename, 'rU') as f:
            fields = csv.reader(f)
            for row in fields:
                data.append(row)
        self.headers = data[0]
        for row in data[1:]:
            name = row[1]
            row = City.clean_row(row)
            self.neighborhoods[name] = Neighborhood(data[0], row)


    # this is just a quick fix for now, but it's not a long-term solution
    # this is changing all the empty cells to zeros
    @staticmethod
    def clean_row(row):
        rt = []
        for i in row:
            try:
                f = float(i)
                rt.append(i)
            except:
                rt.append(0.0)
        return rt

    def get_neighborhoods(self, header1, header2):
        '''
        Takes two headers, returns a list of tuples
        With each neighborhood name and its measurement
        If the second header is the default, then only grab one measurement instead of two
        '''
        rt = []
        if header2 == DEFAULT_KEY:
            for n in self.neighborhoods.keys():
                m = self.neighborhoods[n].get_measurement(header1)
                rt.append((n, m))
            return rt

        for n in self.neighborhoods.keys():
            m = self.neighborhoods[n].get_measurement(header1)
            o = self.neighborhoods[n].get_measurement(header2)
            rt.append((n, m, o))
        return rt

    def get_values(self, header):
        '''
        Takes itself and a single header, returns a list of all the neighborhood measurements
        '''
        rt = []
        for n in self.neighborhoods:
            try:
                value = self.neighborhoods[n].get_measurement(header)
                rt.append(float(value))
            except:
                pass
        return rt

    def get_headers(self):
        return self.headers

    def get_thresholds(self, header):
        '''
        Return the low, medium, and high thresholds for the neighborhood
        '''
        values = City.get_values(self, header)
        low = float(min(values))
        high = float(max(values))
        ##mean = float(statistics.mean(values))
        mean = float(sum(values) / len(values))
        low_mid = float((mean - low)/ 2)
        high_mid = float((high - mean) / 2)
        print("{} -- low: {} low_mid: {} mean: {} high_mid: {} high: {}".format(header, low, low_mid, mean, high_mid, high))
        return [(low, low_mid), (low_mid, high_mid), (high_mid, high)]


    def __str__(self):
        return "So far you've got {} neighborhoods".format(len(self.neighborhoods))