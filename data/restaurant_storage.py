import json

from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from data.data_error import InsertError
from data.decimal_encoder import DecimalEncoder

TABLE_NAME = 'restaurants'


class RestaurantStorage:
    def __init__(self, resource):
        self.resource = resource

    def insert(self, restaurant):
        table = self.resource.Table(TABLE_NAME)

        try:
            response = table.put_item(
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
            print("PutItem succeeded:")
            print(json.dumps(response, indent=4, cls=DecimalEncoder))

    def get_by_id(self, rid):
        table = self.resource.Table(TABLE_NAME)

        try:
            response = table.get_item(
                Key={
                    'id': rid
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            item = response['Item']
            print("GetItem succeeded:")
            return json.dumps(item, indent=4, cls=DecimalEncoder)

    def get_by_zip(self, zip_code):
        table = self.resource.Table(TABLE_NAME)

        try:
            response = table.query(
                KeyConditionExpression=Key('zip_code').eq(zip_code)
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            item = response['Item']
            print("GetItem succeeded:")
            return json.dumps(item, indent=4, cls=DecimalEncoder)
