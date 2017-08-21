import unittest

from data.inspection_storage import InspectionStorage
from model.inspection import Inspection
from test.data.test_resource import TestResource


class TestInspectionStorage(unittest.TestCase):
    def test_insert(self):
        resource = TestResource()
        storage = InspectionStorage(resource)
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
