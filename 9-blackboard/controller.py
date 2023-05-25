class Controller:
    def __init__(self, blackboard):
        self.blackboard = blackboard
        self.sources = {}

    def add_source(self, key, source):
        if key not in self.sources:
            self.sources[key] = source

    def execute_source(self, key, arguments):
        if key in self.sources:
            result = self.sources[key].execute(arguments)
            self.blackboard.add_data(result)
