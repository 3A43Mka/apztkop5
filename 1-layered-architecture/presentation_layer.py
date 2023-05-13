class PresentationLayer:

    @staticmethod
    def print_items(items):
        print("\n============ITEMS============")
        print("ID | Name | Price | Quantity")
        for item in items:
            print(f'{item["id"]} - {item["name"]} - {item["price"]} - {item["quantity"]}')
        print("=============================\n")

    @staticmethod
    def print_item(item):
        print(f'{item["id"]} - {item["name"]} - {item["price"]} - {item["quantity"]}')
