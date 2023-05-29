from expression import Expression


class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        return context.get_variable(self.name)
