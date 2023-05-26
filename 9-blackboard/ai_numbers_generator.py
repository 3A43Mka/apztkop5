import random


class AINumbersGenerator:
    def __init__(self):
        # mocking some result data
        self.possible_data = [23, 4, 6, 4545, 45, 8697, 949, 34342, 2, 0, 324, 655]

    def execute(self, arguments):
        return random.choice(self.possible_data)
