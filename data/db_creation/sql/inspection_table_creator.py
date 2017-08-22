class InspectionTableCreator:
    def __init__(self, connection):
        self.connection = connection

    def create_tables(self):
        c = self.connection.cursor()

        # Create table
        c.execute('''CREATE TABLE inspections
                     (rid VARCHAR(60), date VARCHAR(10), score int)''')
