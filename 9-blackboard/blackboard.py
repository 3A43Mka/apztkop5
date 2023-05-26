class Blackboard:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_data(self):
        return self.data

    def display_data(self):
        for d in self.data:
            print(f'- {d}')
