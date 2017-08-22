import unittest

from data.dynamodb.restaurant_storage import DynamoDBRestaurantStorage
from model.restaurant import Restaurant
from test.data.test_resource import TestDynamoDBResource


class TestDynamoDBRestaurantStorage(unittest.TestCase):
    def test_insert(self):
        resource = TestDynamoDBResource()
        storage = DynamoDBRestaurantStorage(resource)
        restaurant = Restaurant(
            'test_123',
            "Joe's Crabshack",
            city="Los Angeles",
            state='CA')
        storage.insert(restaurant)
        actual = resource.get_inserts('restaurants')
        first = actual[0]
        self.assertEqual(first['id'], restaurant.rid)
        self.assertEqual(first['name'], restaurant.name)


if __name__ == '__main__':
    unittest.main()
