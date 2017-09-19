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

    def get_all_by_id(self, rid):
        inspections = []
        cursor = self.connection.execute(
            'SELECT * FROM inspections WHERE rid = ?', (rid,))
        rows = cursor.fetchall()
        for row in rows:
            inspections.append(Inspection(row[0], row[1], row[2]))
        return inspections

    def get_latest_by_id(self, rid):
        inspections = []
        cursor = self.connection.execute(
            'SELECT rid, MAX(Date), score '
            'FROM inspections WHERE '
            'rid = ? '
            'GROUP BY rid',
            (rid,))
        rows = cursor.fetchall()
        if len(rows) != 1:
            raise ValueError("Inspection with RID " + rid + " not found")
        return Inspection(rows[0][0], rows[0][1], rows[0][2])

