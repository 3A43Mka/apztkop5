from master import Master


def test_1():
    master1 = Master()
    master1.process([{'name': 'Task1', 'steps': 1}])
    results = master1.get_results()
    assert results == ['Result for the task "Task1".']


def test_2():
    master1 = Master()
    master1.process([{'name': 'Task1', 'steps': 1},
                     {'name': 'Task2', 'steps': 3}])
    results = master1.get_results()
    assert results == ['Result for the task "Task1".', 'Result for the task "Task2".']


def test_3():
    master1 = Master()
    master1.process([{'name': 'Task1', 'steps': 1},
                     {'name': 'Task2', 'steps': 3}])
    logs = master1.get_logs()
    assert logs == ['Doing task "Task1", 0 steps left.',
                    'Doing task "Task2", 2 steps left.',
                    'Result for the task "Task1".',
                    'Doing task "Task2", 1 steps left.',
                    'Doing task "Task2", 0 steps left.',
                    'Result for the task "Task2".']
