import unittest

import sqlite3
from zipfile import ZipFile

from data.db_creation.sql.inspection_table_creator import InspectionTableCreator
from data.db_creation.sql.restaurant_table_creator import RestaurantTableCreator
from data.sql.inspection_storage import InspectionStorage
from data.sql.restaurant_storage import RestaurantStorage
from data.uploads.la.lives_data_upload import LivesDataUpload


class TestLaLivesDataUpload(unittest.TestCase):
    def test_upload(self):
        conn = sqlite3.connect(':memory:')
        InspectionTableCreator(conn).create_tables()
        RestaurantTableCreator(conn).create_tables()

        restaurant_storage = RestaurantStorage(conn)
        inspection_storage = InspectionStorage(conn)

        data = LivesDataUpload(restaurant_storage, inspection_storage)
        data.upload(ZipFile('LaBusinesses.zip'))

        actual = restaurant_storage.get_by_id("laca_PR0000031")
        self.assertEqual(actual.rid, "laca_PR0000031")
        self.assertEqual(actual.name, "Monrovia Cinema Concession I")

        inspections = inspection_storage.get_all_by_id("laca_PR0000031")
        self.assertEqual(4, len(inspections))

        latest = inspection_storage.get_latest_by_id("laca_PR0000031")
        self.assertEqual("20170420", latest.date)
