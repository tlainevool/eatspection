from zipfile import ZipFile

from data.uploads.la.la_data_upload import LaDataUpload
from model.inspection import Inspection
from model.restaurant import Restaurant
from util.string_util import capitalize_all


def custom_split(s):
    not_inside_comma = True
    words = []
    start = 0
    for i, c in enumerate(s):
        if c == ',' and not_inside_comma:
            words.append(s[start:i])
            start = i + 1
        elif c == '"':
            not_inside_comma = not not_inside_comma
    words.append(s[start:])
    return words


class LivesDataUpload(LaDataUpload):
    def __init__(self, restaurant_storage, inspection_storage):
        super().__init__()
        self.restaurant_storage = restaurant_storage
        self.inspection_storage = inspection_storage

    def upload(self, file=ZipFile('LaBusinesses.zip')):
        with file as zip_file:
            restaurants = self.read_restaurants(zip_file)
            inspections = self.read_inspections(zip_file)
            # self.add_inspections(restaurants, inspections)
        for restaurant in restaurants.values():
            self.restaurant_storage.insert(restaurant)
        for inspection in inspections:
            self.inspection_storage.insert(inspection)

    def read_inspections(self, zip_file):
        with zip_file.open("inspections.csv") as inspections_file:
            inspections = []
            header_line = inspections_file.readline()
            header_mapping = self.map_headers(header_line)
            for line in inspections_file:
                line = self.split_line_from_zip(line)
                inspections.append(self.create_inspection_from_lives_data(line, header_mapping))
        return inspections

    # @staticmethod
    # def add_inspections(restaurants, inspections):
    #     for inspection in inspections:
    #         restaurant = restaurants[inspection.rid]
    #         if not restaurant.inspect_date or inspection.date > restaurant.inspect_date:
    #             restaurant.inspect_date = inspection.date
    #             restaurant.score = inspection.score

    def read_restaurants(self, zip_file):
        restaurants = dict()
        with zip_file.open("businesses.csv") as businesses:
            header_line = businesses.readline()
            header_mapping = self.map_headers(header_line)
            for line in businesses:
                line = self.split_line_from_zip(line)
                restaurant = self.create_restaurant_from_lives_data(line, header_mapping)
                restaurants[restaurant.rid] = restaurant
        return restaurants

    @staticmethod
    def create_inspection_from_lives_data(line, header_mapping):
        rid = 'laca_' + line[header_mapping['business_id']]
        score = line[header_mapping['score']]
        date = line[header_mapping['date']]
        return Inspection(rid, date, score)

    def map_headers(self, header_line):
        header = self.split_line_from_zip(header_line)
        header_mapping = dict()
        for i, name in enumerate(header):
            header_mapping[name] = i
        return header_mapping

    @staticmethod
    def split_line_from_zip(line):
        return line.decode('utf-8', errors='replace').strip().strip('"').split('","')

    @staticmethod
    def create_restaurant_from_lives_data(line, header_map):
        rid = 'laca_' + line[header_map['business_id']]
        name = capitalize_all(line[header_map['name']])
        address = capitalize_all(line[header_map['address']])
        city = capitalize_all(line[header_map["city"]])
        state = line[header_map["state"]]
        zip_code = line[header_map["postal_code"]]
        latitude = line[header_map['latitude']]
        longitude = line[header_map['longitude']]
        restaurant = Restaurant(rid,
                                name,
                                address=address,
                                city=city,
                                state=state,
                                zip_code=zip_code,
                                latitude=latitude,
                                longitude=longitude)
        return restaurant


if __name__ == '__main__':
    # conn = sqlite3.connect(':memory:')
    # data = LivesDataUpload(conn)
    # data.upload()
    pass
