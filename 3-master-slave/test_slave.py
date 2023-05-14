from slave import Slave


def test_1():
    slave1 = Slave('Task1', 1)
    slave1.do_task()
    assert slave1.is_complete()


def test_2():
    slave1 = Slave('Task1', 2)
    slave1.do_task()
    assert not slave1.is_complete()


def test_3():
    slave1 = Slave('Task1', 1)
    slave1.do_task()
    result = slave1.get_result()
    assert result == 'Result for the task "Task1".'


def test_4():
    num_of_steps = 4
    slave1 = Slave('Task1', num_of_steps)

    for i in range(num_of_steps):
        slave1.do_task()

    assert slave1.is_complete()

