from controller import Controller
from blackboard import Blackboard


class FakeSource1:
    def __init__(self):
        self.data = 'data from source 1'

    def execute(self, args):
        return self.data


class FakeSource2:
    def __init__(self):
        self.data = 'data from source 2'

    def execute(self, args):
        return self.data


RESOURCE_1 = 'RESOURCE_1'
RESOURCE_2 = 'RESOURCE_2'


def test1():
    blackboard1 = Blackboard()
    controller1 = Controller(blackboard1)
    resoure1 = FakeSource1()
    controller1.add_source(RESOURCE_1, resoure1)
    controller1.execute_source(RESOURCE_1, 'give me this')
    result = blackboard1.get_data()
    assert result == ['data from source 1']


def test2():
    blackboard1 = Blackboard()
    controller1 = Controller(blackboard1)
    resource1 = FakeSource1()
    resource2 = FakeSource2()
    controller1.add_source(RESOURCE_1, resource1)
    controller1.add_source(RESOURCE_2, resource2)
    controller1.execute_source(RESOURCE_1, 'give me this')
    controller1.execute_source(RESOURCE_2, 'give me that')
    result = blackboard1.get_data()
    assert result == ['data from source 1', 'data from source 2']


def test3():
    blackboard1 = Blackboard()
    controller1 = Controller(blackboard1)
    resource1 = FakeSource1()
    resource2 = FakeSource2()
    controller1.add_source(RESOURCE_1, resource1)
    controller1.add_source(RESOURCE_2, resource2)
    controller1.execute_source(RESOURCE_1, 'give me this')
    controller1.execute_source(RESOURCE_2, 'give me that')
    controller1.execute_source(RESOURCE_1, 'and then this again')
    result = blackboard1.get_data()
    assert result == ['data from source 1', 'data from source 2', 'data from source 1']
