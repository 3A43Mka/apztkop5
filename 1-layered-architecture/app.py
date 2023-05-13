from business_layer import BusinessLayer
from presentation_layer import PresentationLayer


class App:
    def __init__(self):
        self.business_layer = BusinessLayer()
        self.presentation_layer = PresentationLayer()
        self.is_running = True
        self.menu_choice = 1

    def run_app(self):
        while self.is_running:
            self.display_menu()
            self.ask_menu_choice()

    @staticmethod
    def display_menu():
        print("\nItems Stock App")
        print("1. Show all items")
        print("2. Add new item")
        print("3. Update item")
        print("4. Delete item")
        print("7. Exit")

    def ask_menu_choice(self):
        self.menu_choice = input("Your menu choice...\n")
        if self.menu_choice == "1":
            self.show_all_items()
        elif self.menu_choice == "2":
            self.add_new_item()
        elif self.menu_choice == "3":
            self.update_item()
        elif self.menu_choice == "4":
            self.delete_item()
        elif self.menu_choice == "7":
            self.is_running = False

    def show_all_items(self):
        all_items = self.business_layer.get_all_items_from_stock()
        self.presentation_layer.print_items(all_items)

    def add_new_item(self):
        print("Please describe new item:")
        name = input("Item name: ")
        price = input("Item price: ")
        quantity = input("Item quantity: ")
        new_item = {"id": 0, "name": name, "price": int(price), "quantity": int(quantity)}
        created_item = self.business_layer.add_item_to_stock(new_item)
        print("\nCreated new item in stock:")
        self.presentation_layer.print_item(created_item)

    def update_item(self):
        id = input("Please enter id of the item you want to update:\n")
        got_item = self.business_layer.get_item_by_id(int(id))
        if got_item is None:
            print("There is no such item")
            return
        print("Editing item:")
        self.presentation_layer.print_item(got_item)
        new_name = input("Please enter new name:\n")
        new_price = input("Please enter new price:\n")
        new_quantity = input("Please enter new quantity:\n")
        updated_item = {"id": got_item["id"], "name": new_name, "price": int(new_price), "quantity": int(new_quantity)}
        result = self.business_layer.update_item_in_stock(updated_item)
        print("\nThe item has been updated:")
        self.presentation_layer.print_item(result)

    def delete_item(self):
        id = input("Please enter id of the item you want to delete:\n")
        got_item = self.business_layer.get_item_by_id(int(id))
        if got_item is None:
            print("There is no such item")
            return
        print("Deleting item...")
        deleted_item = self.business_layer.remove_item_from_stock(int(id))
        print("Successfully deleted item:")
        self.presentation_layer.print_item(deleted_item)
