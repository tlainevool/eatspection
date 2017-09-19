import unittest

import sqlite3

from data.db_creation.sql.inspection_table_creator import InspectionTableCreator
from data.sql.inspection_storage import InspectionStorage
from model.inspection import Inspection


class TestSQLInspectionStorage(unittest.TestCase):
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
        inspection = Inspection(
            'test_123',
            "20170601",
            98)
        storage.insert(inspection)

        actuals = storage.get_all_by_id(inspection.rid)
        self.assertEqual(2, len(actuals))
        for inspection in actuals:
            if inspection.score == 99:
                self.assertEqual("20170816", inspection.date)
            elif inspection.score == 98:
                self.assertEqual("20170601", inspection.date)


if __name__ == '__main__':
    unittest.main()
