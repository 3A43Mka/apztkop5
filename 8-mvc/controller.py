class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_all_users(self):
        return self.model.get_all_users()

    def get_user_by_id(self, id):
        return self.model.get_user_by_id(id)

    def add_user(self, new_user):
        return self.model.add_user(new_user)

    def update_user(self, updated_user):
        return self.model.update_user(updated_user)

    def delete_user(self, id):
        return self.model.delete_user(id)

    def delete_all_users(self):
        all_users = list(self.model.get_all_users()).copy()
        for user in all_users:
            self.model.delete_user(user['id'])

    def handle_updating_user(self):
        self.view.print_message('Please specify user id:')
        user_id = input('id: ')
        user = self.model.get_user_by_id(int(user_id))
        if user is None:
            self.view.print_message('There is no such user.')
            return
        self.view.print_message('You are editing this user:')
        self.view.print_users([user])
        self.view.print_message('Enter new username:')
        new_username = input()
        self.view.print_message('Enter new email:')
        new_email = input()
        updated_user = {'id': user['id'], 'username': new_username, 'email': new_email}
        result = self.model.update_user(updated_user)
        if result is not None:
            self.view.print_message('User has been updated')

    def handle_input(self):
        while True:
            self.view.print_message('1. Show all users\n2. Update user by id\n6. Exit')
            command = input('\nInsert a command ')

            if command == '1':
                self.view.print_users(self.model.get_all_users())

            if command == '2':
                self.handle_updating_user()

            if command == '6':
                break
