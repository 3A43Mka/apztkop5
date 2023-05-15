class Pipeline:
    def __init__(self):
        self.filters = list()

    def add(self, filter):
        self.filters.extend(filter)

    def execute(self, message):
        print("Executing pipeline...")
        for message_filter in self.filters:
            message_filter(message)

