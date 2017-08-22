from logging import getLogger

logger = getLogger('eatspection.data.creation')

class BaseTableCreator:
    def __init__(self, table_name):
        self.table_name = table_name

    def drop_table(self):
        logger.info("Drop table:" + self.table_name + "...")
        table = self.db_resource.Table(self.table_name)
        table.delete()
        table.meta.client.get_waiter('table_not_exists').wait(TableName=self.table_name)
        logger.info(self.table_name + " dropped.")
