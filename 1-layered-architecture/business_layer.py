from db_layer import DatabaseLayer


class BusinessLayer:
    def __init__(self):
        self.db = DatabaseLayer()

    def get_all_items_from_stock(self):
        return self.db.get_all_items()

    def get_item_by_id(self, id):
        return self.db.get_item_by_id(id)

    def add_item_to_stock(self, item):
        return self.db.add_item(item)

    def update_item_in_stock(self, new_item):
        return self.db.update_item(new_item)

    def remove_item_from_stock(self, id):
        return self.db.delete_item(id)

