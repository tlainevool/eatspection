from data.uploads.la.la_data_upload import LaDataUpload
from model.restaurant import Restaurant
from util.string_util import capitalize_all


class manually_downloaded_la_data_upload(LaDataUpload):
    """Deprecated: This was made before I discovered the LIVES format I can use"""

    def upload(self):
        with open('LOS_ANGELES_COUNTY_RESTAURANT_AND_MARKET_VIOLATIONS-2017-07-20.csv', 'r') as in_file:
            reader = csv.DictReader(in_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
            restaurants = dict()
            for data in reader:
                restaurant, rid = self.create_restaurant_from_data(data)
                if rid in restaurants:
                    if restaurants[rid].inspect_date < restaurant.inspect_date:
                        restaurants[rid] = restaurant
                else:
                    restaurants[rid] = restaurant

            print("Number of restaurant:", len(restaurants))
            restaurants = restaurants.values()
            self.save_to_db(restaurants)

    def create_restaurant_from_data(self, data):
        name = capitalize_all(data["NAME"])
        inspect_date = self.mdy_to_date(data["ACTIVITY DATE"])
        score = data["SCORE"]
        address = capitalize_all(data["SITE ADDRESS"])
        city = capitalize_all(data["SITE CITY"])
        state = data["SITE STATE"]
        zip_code = data["SITE ZIP"]
        rid = 'laca_' + data["RECORD ID"]
        restaurant = Restaurant(rid, name, inspect_date, score, address, city, state, zip_code)
        return restaurant, rid


if __name__ == '__main__':
    la_data = LaDataUpload()
    la_data.upload()