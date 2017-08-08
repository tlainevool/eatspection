import csv
import datetime

import boto3

from data.data_error import DataError
from data.restaurant_storage import RestaurantStorage
from model.restaurant import Restaurant
from util.string_util import capitalize_all

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
storage = RestaurantStorage(dynamodb)


def todate(string):
    date = datetime.datetime.strptime(string, '%m/%d/%Y').date()
    return str(date.year) + '-' + '%02d' % date.month + '-' + '%02d' % date.day


with open('LOS_ANGELES_COUNTY_RESTAURANT_AND_MARKET_VIOLATIONS-2017-07-20.csv', 'r') as in_file:
    reader = csv.DictReader(in_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    restaurants = dict()
    for data in reader:
        name = capitalize_all(data["NAME"])
        inspect_date = todate(data["ACTIVITY DATE"])
        score = data["SCORE"]
        address = capitalize_all(data["SITE ZIP"])
        city = capitalize_all(data["SITE CITY"])
        state = data["SITE STATE"]
        zip_code = data["SITE ZIP"]
        rid = 'laca_' + data["RECORD ID"]
        restaurant = Restaurant(rid, name, inspect_date, score, address, city, state, zip_code)
        if rid in restaurants:
            if restaurants[rid].inspect_date < restaurant.inspect_date:
                restaurants[rid] = restaurant
        else:
            restaurants[rid] = restaurant

    print("Number of restaurant:", len(restaurants))
    for restaurant in restaurants.values():
        try:
            storage.insert(restaurant)
        except DataError as err:
            print("Unexpected Error:", err)
