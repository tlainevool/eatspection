from logging import getLogger

from data.restaurant_storage import TABLE_NAME

logger = getLogger('eatspection.data.creation')


class RestaurantTableCreator:
    def __init__(self, db_resource):
        self.db_resource = db_resource

    def create_table(self):
        logger.info("Create table:" + TABLE_NAME + "...")
        table = self.db_resource.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        table.meta.client.get_waiter('table_exists').wait(TableName=TABLE_NAME)
        logger.info(TABLE_NAME + " created.")
