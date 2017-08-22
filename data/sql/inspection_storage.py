import sqlite3

from logging import getLogger

from model.inspection import Inspection

TABLE_NAME = 'inspections'


class InspectionStorage:
    logger = getLogger('eatspection.data.sql.inspection_storage')

    def __init__(self, connection):
        self.connection = connection

    def insert(self, inspection):
        self.connection.execute('''
        INSERT INTO inspections 
        (rid, date, score)
        VALUES (?, ?, ?)

        ''', (inspection.rid, inspection.date, inspection.score))
        self.connection.commit()

    def get_by_id(self, rid):
        cursor = self.connection.execute(
            'SELECT * FROM inspections WHERE rid = ?', (rid,))
        if cursor.arraysize != 1:
            raise ValueError('Inspection with Rid: ' + rid + ' not found')
        row = cursor.__next__()
        inspection = Inspection(row[0], row[1], row[2])
        return inspection


