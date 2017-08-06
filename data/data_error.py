class DataError(Exception):
    pass


class InsertError(DataError):
    def __init__(self, message):
        self.message = message
