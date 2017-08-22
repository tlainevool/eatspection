from collections import defaultdict


class Table:

    def put_item(self, Item):
        self.inserts = []
        self.inserts.append(Item)


class TestDynamoDBResource:
    tables = defaultdict(Table)

    def Table(self, name):
        table = self.tables[name]
        return table

    def get_inserts(self, table_name):
        return self.tables[table_name].inserts
