import numpy as np 
import pandas
from pandas import DataFrame, Series

class PandasCity:

    def __init__(self, filename):
        with open(filename, 'rU') as f:
            fields = csv.reader(f)
            for row in fields:
                data.append(row)
        self.df = DataFrame(data[1:], columns=data[0])