import json

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

