from model import Model


def test1():
    model1 = Model()
    model1.add_user({'username': 'testuser', 'email': 'someemail@gmail.com'})
    users = model1.get_all_users()
    assert users == [{'id': 1, 'username': 'testuser', 'email': 'someemail@gmail.com'}]


def test2():
    model1 = Model()
    model1.add_user({'username': 'testuser1', 'email': 'someemail1@gmail.com'})
    model1.add_user({'username': 'testuser2', 'email': 'someemail2@gmail.com'})
    users = model1.get_all_users()
    assert users == [{'id': 1, 'username': 'testuser1', 'email': 'someemail1@gmail.com'},
                     {'id': 2, 'username': 'testuser2', 'email': 'someemail2@gmail.com'}]


def test3():
    model1 = Model()
    model1.add_user({'username': 'testuser', 'email': 'someemail@gmail.com'})
    user = model1.get_user_by_id(1)
    assert user == {'id': 1, 'username': 'testuser', 'email': 'someemail@gmail.com'}


def test4():
    model1 = Model()
    model1.add_user({'username': 'testuser', 'email': 'someemail@gmail.com'})
    user = model1.get_user_by_id(9)
    assert user is None


def test5():
    model1 = Model()
    model1.add_user({'username': 'testuser', 'email': 'someemail@gmail.com'})
    user = model1.get_user_by_id(1)
    assert user == {'id': 1, 'username': 'testuser', 'email': 'someemail@gmail.com'}


def test6():
    model1 = Model()
    model1.add_user({'username': 'testuser', 'email': 'someemail@gmail.com'})
    update_user = {'id': 1, 'username': 'upd', 'email': 'upd@gmail.com'}
    user = model1.update_user(update_user)
    assert user == {'id': 1, 'username': 'upd', 'email': 'upd@gmail.com'}


def test7():
    model1 = Model()
    model1.add_user({'username': 'testuser', 'email': 'someemail@gmail.com'})
    model1.delete_user(1)
    check_user = model1.get_user_by_id(1)
    assert check_user is None
