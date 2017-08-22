import json

from botocore.exceptions import ClientError
from logging import getLogger

from data.data_error import InsertError, DataError
from data.decimal_encoder import DecimalEncoder

TABLE_NAME = 'inspections'


class DynamoDBInspectionStorage:
    logger = getLogger('eatspection.data.inspection_storage')

    def __init__(self, resource):
        self.table = resource.Table(TABLE_NAME)

    def insert(self, inspection):

        try:
            self.table.put_item(
                Item={
                    'id': inspection.rid,
                    'date': inspection.date,
                    'score': inspection.score
                }
            )
        except Exception as err:
            raise InsertError(err)
        else:
            self.logger.info("PutItem succeeded for id:" + inspection.rid)

    def get_by_id(self, rid):

        try:
            response = self.table.get_item(
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
