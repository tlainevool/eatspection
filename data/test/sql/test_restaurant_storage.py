import unittest

import sqlite3

from data.db_creation.sql.restaurant_table_creator import RestaurantTableCreator
from data.sql.restaurant_storage import RestaurantStorage
from model.restaurant import Restaurant


class TestRestaurantStorage(unittest.TestCase):
    def test_insert(self):
        conn = sqlite3.connect(':memory:')

        creator = RestaurantTableCreator(conn)
        creator.create_tables()
        storage = RestaurantStorage(conn)
        restaurant = Restaurant(
            'test_123',
            "Joe's Crabshack",
            city="Los Angeles",
            state='CA')
        storage.insert(restaurant)

        actual = storage.get_by_id(restaurant.rid)
        self.assertEqual(actual.rid, restaurant.rid)
        self.assertEqual(actual.name, restaurant.name)
        self.assertEqual(actual.address, restaurant.address)
        self.assertEqual(actual.city, restaurant.city)
        self.assertEqual(actual.state, restaurant.state)
        self.assertEqual(actual.zip_code, restaurant.zip_code)
        self.assertEqual(actual.latitude, restaurant.latitude)
        self.assertEqual(actual.longitude, restaurant.longitude)




if __name__ == '__main__':
    unittest.main()
