from expression import Expression


class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value
