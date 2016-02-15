class Neighborhood:

    def __init__(self, headers, row):
      self.dict = {}
      for i, h in enumerate(headers):
        try:
            self.dict[h] = float(row[i])
        except:
            self.dict[h] = row[i]
