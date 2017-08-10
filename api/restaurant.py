#!flask/bin/python
import boto3
from flask import Flask, jsonify, abort
from flask import make_response

from data.data_error import DataError
from data.restaurant_storage import RestaurantStorage

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
storage = RestaurantStorage(dynamodb)


@app.errorhandler(404)
def custom400(error):
    return make_response(jsonify({'message': error.description}), 404)


@app.errorhandler(500)
def custom500(error):
    return make_response(jsonify({'message': error.description}), 500)


@app.route('/eatspection/api/v1.0/restaurants/<string:restaurant_id>', methods=['GET'])
def get_restaurants_by_id(restaurant_id):
    try:
        restaurant = storage.get_by_id(restaurant_id)
        if not restaurant:
            abort(404, 'Restaurant with id ' + restaurant_id + ' not found.')
        return restaurant
    except DataError as de:
        abort(500, "Unknown error:" + de.message)

if __name__ == '__main__':
    app.run(debug=True)
