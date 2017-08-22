from logging import getLogger

import boto3
from data.db_creation.inspection_table_creator import InspectionTableCreator

from data.db_creation.dynamodb.restaurant_table_creator import RestaurantTableCreator

logger = getLogger('eatspection.data.creation')

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

restaurants = RestaurantTableCreator(dynamodb)
restaurants.drop_table()

inspections = InspectionTableCreator(dynamodb)
inspections.drop_table()
