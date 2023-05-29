from expression import Expression


class Add(Expression):
    def __init__(self, left_expression, right_expression):
        self.left_expression = left_expression
        self.right_expression = right_expression

    def interpret(self, context):
        left_value = self.left_expression.interpret(context)
        right_value = self.right_expression.interpret(context)
        return left_value + right_value
