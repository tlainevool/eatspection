class Restaurant:
    def __init__(self, rid, name, inspect_date, score, address, city, state, zip_code):
        self.id = rid
        self.zip_code = zip_code
        self.state = state
        self.city = city
        self.address = address
        self.score = score
        self.inspect_date = inspect_date
        self.name = name

    def __str__(self):
        return 'Restaurant - ' \
               'id:' + self.id + \
               ' name:' + self.name + \
               ' inspect_date:' + self.inspect_date + \
               ' score:' + self.score + \
               ' address:' + self.address + ' ' + self.city + ' ' + self.state + ' ' + self.zip_code
