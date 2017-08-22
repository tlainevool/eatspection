from logging import getLogger

import sqlite3

from data.db_creation.sql.inspection_table_creator import InspectionTableCreator
from data.db_creation.sql.restaurant_table_creator import RestaurantTableCreator

logger = getLogger('eatspection.data.creation')


def create_tables():
    conn = sqlite3.connect(':memory:')

    restaurants = RestaurantTableCreator(conn)
    restaurants.create_tables()

    inspections = InspectionTableCreator(conn)
    inspections.create_tables()

    return conn
