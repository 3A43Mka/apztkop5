class Peer:
    def __init__(self, initial_data):
        self.data = initial_data
        self.connection = None

    def connect(self, other):
        if self.connection is None:
            self.connection = other
            other.connection = self

    def disconnect(self):
        if self.connection is not None:
            self.connection.connection = None
            self.connection = None

    def send_data(self, data):
        if self.connection is not None:
            self.connection.data.extend(data)

    def get_data(self):
        if self.connection is not None:
            self.data.extend(self.connection.data)
