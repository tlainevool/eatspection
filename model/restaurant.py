class Restaurant:
    def __init__(self,
                 rid,
                 name,
                 city,
                 state,
                 address=None,
                 zip_code=None,
                 latitude=None,
                 longitude=None):
        self.rid = rid
        self.zip_code = zip_code
        self.state = state
        self.city = city
        self.address = address
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return 'Restaurant - ' \
               'rid:' + self.rid + \
               ' name:' + self.name + \
               ' address:' + self.address + ' ' + self.city + ' ' + self.state + ' ' + self.zip_code
