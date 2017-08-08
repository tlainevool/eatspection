#!flask/bin/python
import boto3
from flask import Flask

from data.restaurant_storage import RestaurantStorage

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
storage = RestaurantStorage(dynamodb)


@app.route('/eatspection/api/v1.0/restaurants/<string:restaurant_id>', methods=['GET'])
def get_restaurants_by_id(restaurant_id):
    return storage.get_by_id(restaurant_id)

if __name__ == '__main__':
    app.run(debug=True)
