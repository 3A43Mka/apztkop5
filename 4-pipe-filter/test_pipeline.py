from pipeline import Pipeline


def test_1():
    pipeline1 = Pipeline()
    obj = {'a': 4, 'b': 43, 'c': 67, 'd': 23}
    pipeline1.execute(obj)
    assert obj == {'a': 8, 'b': 43, 'c': 67, 'd': 0}


def test_2():
    pipeline1 = Pipeline()
    obj = {'a': 56, 'b': 8, 'c': 12, 'd': 3}
    pipeline1.execute(obj)
    assert obj == {'a': 56, 'b': 4, 'c': 36, 'd': 3}


def test_3():
    pipeline1 = Pipeline()
    obj = {'a': 12, 'b': 34, 'c': 3, 'd': 89}
    pipeline1.execute(obj)
    assert obj == {'a': 24, 'b': 17, 'c': 9, 'd': 0}
