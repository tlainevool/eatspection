import boto3

from data.data_error import DataError
from data.restaurant_storage import RestaurantStorage
from model.restaurant import Restaurant
from util.string_util import capitalize_all

with open('la-health-file.tsv', 'r') as in_file:
    dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    storage = RestaurantStorage(dynamodb)
    for line in in_file:
        data = line.split('\t')
        name = capitalize_all(data[0])
        inspect_date = data[1]
        score = data[2]
        address = capitalize_all(data[4])
        city = capitalize_all(data[5])
        state = 'CA'
        zip_code = data[6]
        print("Uploading " + name)
        restaurant = Restaurant(name, inspect_date, score, address, city, state, zip_code)
        try:
            storage.insert(restaurant)
        except DataError as err:
            print("Unexpected Error:", err)
