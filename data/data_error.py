class DataError(Exception):
    def __init__(self, message):
        self.message = message


class InsertError(DataError):
    def __init__(self, message):
        DataError.__init__(self, message)
