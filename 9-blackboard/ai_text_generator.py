import random


class AITextGenerator:
    def __init__(self):
        # mocking some result data
        self.possible_data = ['Hello', 'Here are the results', 'Sun aperture is high today', 'Some disturbing data',
                              'The hateful 11', 'Want. More. Coffee.']

    def execute(self, arguments):
        return random.choice(self.possible_data)
