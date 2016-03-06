class Neighborhood:

    def __init__(self, headers, row):
      self.dict = {}
      for i, h in enumerate(headers):
        try:
            self.dict[h] = float(row[i])
        # handles the case of missing values, which are very minimal
        except:
            self.dict[h] = row[i]

    def get_measurement(self, header):
        return self.dict[header]
