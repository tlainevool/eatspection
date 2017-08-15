from logging import getLogger

from data.db_creation.base_table_creator import BaseTableCreator
from data.inspection_storage import TABLE_NAME

logger = getLogger('eatspection.data.creation')


class InspectionTableCreator(BaseTableCreator):
    def __init__(self, db_resource):
        BaseTableCreator.__init__(self, TABLE_NAME)
        self.db_resource = db_resource

    def create_table(self):
        logger.info("Create table:" + self.table_name + "...")
        table = self.db_resource.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'date',
                    'KeyType': 'RANGE'

                }

            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'date',
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
