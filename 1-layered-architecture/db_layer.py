class DatabaseLayer:

    def __init__(self, init_items=None):
        self.items = []
        self.next_id = 0
        if init_items is None or len(init_items) == 0:
            self.set_initial_items()
        else:
            self.items = init_items
            self.next_id = (self.get_max_id_from_items(init_items) + 1)

    def set_initial_items(self):
        self.items = [
            {"id": 1, "name": "Pills", "price": 30, "quantity": 2},
            {"id": 2, "name": "Apple", "price": 7, "quantity": 9},
        ]
        self.next_id = 3

    @staticmethod
    def get_max_id_from_items(items):
        max = 0
        for item in items:
            if item["id"] > max:
                max = item["id"]
        return max

    def get_all_items(self):
        return self.items

    def add_item(self, new_item):
        new_item["id"] = self.next_id
        self.next_id += 1
        self.items.append(new_item)
        return new_item

    def update_item(self, updated_item):
        for i in range(len(self.items)):
            if self.items[i]["id"] == updated_item["id"]:
                self.items[i] = updated_item
                return updated_item
        return None

    def delete_item(self, id):
        for i in range(len(self.items)):
            if self.items[i]["id"] == id:
                returned = self.items[i]
                del self.items[i]
                return returned

    def get_item_by_id(self, id):
        for i in range(len(self.items)):
            if self.items[i]["id"] == id:
                return self.items[i]
        return None
