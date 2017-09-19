class RestaurantTableCreator:
    def __init__(self, connection):
        self.connection = connection

    def create_tables(self):
        c = self.connection.cursor()

        # Create table
        c.execute('''CREATE TABLE restaurants
                     (rid VARCHAR(60), 
                     name VARCHAR(200), 
                     city VARCHAR(100), 
                     state VARCHAR(2), 
                     address VARCHAR(200), 
                     zip_code VARCHAR(10), 
                     latitude VARCHAR(20), 
                     longitude VARCHAR(20))''')
