from variable import Variable
from constant import Constant
from context import Context
from subtract import Subtract


def test1():
    # a - 2
    # 6 - 2
    # = 4
    context1 = Context()
    context1.set_variable('a', 6)
    expression = Subtract(Variable('a'), Constant(2))
    result = expression.interpret(context1)
    assert result == 4


def test2():
    # a - b
    # 10 - 2
    # = 8
    context1 = Context()
    context1.set_variable('a', 10)
    context1.set_variable('b', 2)
    expression = Subtract(Variable('a'), Variable('b'))
    result = expression.interpret(context1)
    assert result == 8


def test3():
    # 23 - 5 - a - b
    # 23 - 5 - 3 - 7
    # = 8
    context1 = Context()
    context1.set_variable('a', 3)
    context1.set_variable('b', 7)
    expression = Subtract(Constant(23), Constant(5))
    result = expression.interpret(context1)
    expression = Subtract(Constant(result), Variable('a'))
    result = expression.interpret(context1)
    expression = Subtract(Constant(result), Variable('b'))
    result = expression.interpret(context1)
    assert result == 8
