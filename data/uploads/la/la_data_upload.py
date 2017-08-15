import datetime

import boto3

from data.data_error import DataError
from data.restaurant_storage import RestaurantStorage


class LaDataUpload:
    def __init__(self):
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
        self.storage = RestaurantStorage(dynamodb)

    @staticmethod
    def mdy_to_date(string):
        date = datetime.datetime.strptime(string, '%m/%d/%Y').date()
        return str(date.year) + '-' + '%02d' % date.month + '-' + '%02d' % date.day

    def save_to_db(self, restaurants):
        for restaurant in restaurants:
            try:
                self.storage.insert(restaurant)
            except DataError as err:
                print("Unexpected Error:", err)
