from logging import getLogger
import boto3

from data.db_creation.restaurant_table_creator import RestaurantTableCreator

logger = getLogger('eatspection.data.creation')

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

restaurants = RestaurantTableCreator(dynamodb)

restaurants.create_table()
