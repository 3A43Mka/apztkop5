from model import Model
from controller import Controller
from view import View


def test1():
    view1 = View()
    model1 = Model()
    controller1 = Controller(model1, view1)
    controller1.add_user({'username': 'testuser', 'email': 'someemail@gmail.com'})
    controller1.add_user({'username': 'testuser2', 'email': 'someemail2@gmail.com'})
    controller1.delete_all_users()
    all_users = controller1.get_all_users()
    assert all_users == []


def test2():
    view1 = View()
    model1 = Model()
    controller1 = Controller(model1, view1)
    controller1.add_user({'username': 'testuser', 'email': 'someemail@gmail.com'})
    controller1.add_user({'username': 'testuser2', 'email': 'someemail2@gmail.com'})
    users = controller1.get_all_users()
    assert users == [{'email': 'someemail@gmail.com', 'id': 1, 'username': 'testuser'},
                     {'email': 'someemail2@gmail.com', 'id': 2, 'username': 'testuser2'}]


def test3():
    view1 = View()
    model1 = Model()
    controller1 = Controller(model1, view1)
    controller1.add_user({'username': 'testuser', 'email': 'someemail@gmail.com'})
    controller1.add_user({'username': 'testuser2', 'email': 'someemail2@gmail.com'})
    controller1.delete_user(2)
    users = controller1.get_all_users()
    assert users == [{'email': 'someemail@gmail.com', 'id': 1, 'username': 'testuser'}]
