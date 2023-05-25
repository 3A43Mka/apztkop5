from blackboard import Blackboard


def test1():
    blackboard1 = Blackboard()
    blackboard1.add_data('Hello')
    blackboard1.add_data('This is data')
    blackboard1.add_data(1)
    assert blackboard1.get_data() == ['Hello', 'This is data', 1]


def test2():
    blackboard1 = Blackboard()
    blackboard1.add_data(544)
    blackboard1.add_data(4)
    blackboard1.add_data('HI')
    assert blackboard1.get_data() == [544, 4, 'HI']


def test3():
    blackboard1 = Blackboard()
    blackboard1.add_data('Some data')
    assert blackboard1.get_data() == ['Some data']
