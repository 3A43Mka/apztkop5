from context import Context
from variable import Variable
from constant import Constant
from add import Add
from subtract import Subtract


def main():
    context1 = Context()

    # 5 + 8 + 10 - 2
    # a + b + 10 - c
    # = 21

    context1.set_variable('a', 5)
    context1.set_variable('b', 8)
    context1.set_variable('c', 2)

    expression = Add(Variable('a'), Variable('b'))
    result = expression.interpret(context1)

    expression = Add(Constant(result), Constant(10))
    result = expression.interpret(context1)

    expression = Subtract(Constant(result), Variable('c'))
    result = expression.interpret(context1)
    print(result)


if __name__ == '__main__':
    main()
