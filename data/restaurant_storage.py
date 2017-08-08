import json

from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from logging import getLogger

from data.data_error import InsertError, DataError
from data.decimal_encoder import DecimalEncoder

TABLE_NAME = 'restaurants'


class RestaurantStorage:
    logger = getLogger('eatspection.data.restaurant_storage')

    def __init__(self, resource):
        self.resource = resource

    def insert(self, restaurant):
        table = self.resource.Table(TABLE_NAME)

        try:
            table.put_item(
                Item={
                    'id': restaurant.id,
                    'name': restaurant.name,
                    'inspect_date': restaurant.inspect_date,
                    'score': restaurant.score,
                    'address': restaurant.address,
                    'city': restaurant.city,
                    'state': restaurant.state,
                    'zip_code': restaurant.zip_code
                }
            )
        except Exception as err:
            raise InsertError(err)
        else:
            self.logger.info("PutItem succeeded for id:" + restaurant.id)

    def get_by_id(self, rid):
        table = self.resource.Table(TABLE_NAME)

        try:
            response = table.get_item(
                Key={
                    'id': rid
                }
            )
        except ClientError as e:
            message = e.response['Error']['Message']
            self.logger.info(message)
            raise DataError(message)
        else:
            if 'Item' not in response:
                return None
            item = response['Item']
            self.logger.debug("GetItem succeeded:")
            return json.dumps(item, indent=4, cls=DecimalEncoder)

    def get_by_zip(self, zip_code):
        table = self.resource.Table(TABLE_NAME)

        try:
            response = table.query(
                KeyConditionExpression=Key('zip_code').eq(zip_code)
            )
        except ClientError as e:
            message = e.response['Error']['Message']
            self.logger.info(message)
            raise DataError(message)
        else:
            item = response['Item']
            return json.dumps(item, indent=4, cls=DecimalEncoder)
