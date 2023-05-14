from master import Master
from slave import Slave


def test_1():
    master1 = Master()
    slave1 = Slave('Task1', 1)
    master1.add_slave(slave1)
    master1.process()
    results = master1.get_results()
    assert results == ['Result for the task "Task1".']


def test_2():
    master1 = Master()
    slave1 = Slave('Task1', 1)
    slave2 = Slave('Task2', 3)
    master1.add_slave(slave1)
    master1.add_slave(slave2)
    master1.process()
    results = master1.get_results()
    assert results == ['Result for the task "Task1".', 'Result for the task "Task2".']


def test_3():
    master1 = Master()
    slave1 = Slave('Task1', 1)
    slave2 = Slave('Task2', 3)
    master1.add_slave(slave1)
    master1.add_slave(slave2)
    master1.process()
    logs = master1.get_logs()
    assert logs == ['Doing task "Task1", 0 steps left.',
                    'Doing task "Task2", 2 steps left.',
                    'Result for the task "Task1".',
                    'Doing task "Task2", 1 steps left.',
                    'Doing task "Task2", 0 steps left.',
                    'Result for the task "Task2".']
