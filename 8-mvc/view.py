class View:
    def __init__(self):
        pass

    def print_message(self, msg):
        print(msg)

    def print_users(self, users):
        for user in users:
            print(f'[{user["id"]}] {user["username"]} {user["email"]}')
