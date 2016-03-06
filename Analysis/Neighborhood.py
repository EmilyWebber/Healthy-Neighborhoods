class Neighborhood:

    def __init__(self, headers, row):
      self.dictionary = {}
      for i, h in enumerate(headers):
        try:
            self.dictionary[h] = float(row[i])
        # handles the case of missing values, which are very minimal
        except:
            self.dictionary[h] = row[i]

    def get_measurement(self, header):
        '''
        Given the csv header string, return this neighborhood's measurement
        '''
        return self.dictionary[header]
