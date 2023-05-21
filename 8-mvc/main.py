from model import Model
from controller import Controller
from view import View


def main():
    model = Model()
    model.add_user({'username': 'johnjackson', 'email': 'john@some.com'})
    model.add_user({'username': 'jim', 'email': 'jim@some.com'})
    view = View()
    controller = Controller(model, view)
    controller.handle_input()


if __name__ == '__main__':
    main()
