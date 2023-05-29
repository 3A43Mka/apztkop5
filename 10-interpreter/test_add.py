from variable import Variable
from constant import Constant
from context import Context
from add import Add


def test1():
    # a + 2
    # 3 + 2
    # = 5
    context1 = Context()
    context1.set_variable('a', 3)
    expression = Add(Variable('a'), Constant(2))
    result = expression.interpret(context1)
    assert result == 5


def test2():
    # a + b
    # 5 + 11
    # = 16
    context1 = Context()
    context1.set_variable('a', 5)
    context1.set_variable('b', 11)
    expression = Add(Variable('a'), Variable('b'))
    result = expression.interpret(context1)
    assert result == 16


def test3():
    # 11 + 8 + a + b
    # 11 + 8 + 4 + 3
    # = 26
    context1 = Context()
    context1.set_variable('a', 4)
    context1.set_variable('b', 3)
    expression = Add(Constant(11), Constant(8))
    result = expression.interpret(context1)
    expression = Add(Constant(result), Variable('a'))
    result = expression.interpret(context1)
    expression = Add(Constant(result), Variable('b'))
    result = expression.interpret(context1)
    assert result == 26
