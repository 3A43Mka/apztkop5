class Model:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, id):
        for user in self.users:
            if user['id'] == id:
                return user
        return None

    def add_user(self, new_user):
        new_user['id'] = self.next_id
        self.next_id += 1
        self.users.append(new_user)
        return new_user

    def update_user(self, updated_user):
        for i in range(len(self.users)):
            if self.users[i]['id'] == updated_user['id']:
                self.users[i] = updated_user
                return self.users[i]
        return None

    def delete_user(self, id):
        for user in self.users:
            if user['id'] == id:
                self.users.remove(user)
                return user
        return None
