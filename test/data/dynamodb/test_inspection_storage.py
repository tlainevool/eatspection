import unittest

from data.dynamodb.inspection_storage import DynamoDBInspectionStorage
from model.inspection import Inspection
from test.data.test_resource import TestDynamoDBResource


class TestDynamoDBInspectionStorage(unittest.TestCase):
    def test_insert(self):
        resource = TestDynamoDBResource()
        storage = DynamoDBInspectionStorage(resource)
        inspection = Inspection(
            'test_123',
            "20170816",
            99)
        storage.insert(inspection)
        actual = resource.get_inserts('inspections')
        first = actual[0]
        self.assertEqual(first['id'], inspection.rid)
        self.assertEqual(first['date'], inspection.date)


if __name__ == '__main__':
    unittest.main()
