import unittest

import sqlite3

from data.db_creation.sql.inspection_table_creator import InspectionTableCreator
from data.sql.inspection_storage import InspectionStorage
from model.inspection import Inspection


class TestDynamoDBInspectionStorage(unittest.TestCase):
    def test_insert(self):
        conn = sqlite3.connect(':memory:')

        creator = InspectionTableCreator(conn)
        creator.create_tables()
        storage = InspectionStorage(conn)
        inspection = Inspection(
            'test_123',
            "20170816",
            99)
        storage.insert(inspection)

        actual = storage.get_by_id(inspection.rid)
        self.assertEqual(actual.rid, inspection.rid)
        self.assertEqual(actual.date, inspection.date)
        self.assertEqual(actual.score, inspection.score)


if __name__ == '__main__':
    unittest.main()
