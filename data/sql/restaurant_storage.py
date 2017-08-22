from logging import getLogger

from model.restaurant import Restaurant

TABLE_NAME = 'restaurants'


class RestaurantStorage:
    logger = getLogger('eatspection.data.sql.restaurant_stoarge')

    def __init__(self, connection):
        self.connection = connection

    def insert(self, restaurant):
        self.connection.execute('''
        INSERT INTO restaurants 
        (rid, 
        name, 
        city, 
        state, 
        address, 
        zip_code, 
        latitude, 
        longitude)
        VALUES (
        ?, ?, ?, ?, ?, ?, ? ,?
        )

        ''', (restaurant.rid,
              restaurant.name,
              restaurant.city,
              restaurant.state,
              restaurant.address,
              restaurant.zip_code,
              restaurant.latitude,
              restaurant.longitude))
        self.connection.commit()

    def get_by_id(self, rid):
        cursor = self.connection.execute(
            'SELECT * FROM restaurants WHERE rid = ?', (rid,))
        if cursor.arraysize != 1:
            raise ValueError("Restaurant with Rid: " + rid + " does not exist")
        row = cursor.__next__()
        restaurant = Restaurant(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        return restaurant
