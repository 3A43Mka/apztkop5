from db_layer import DatabaseLayer

initial_items = [
            {"id": 1, "name": "Juice", "price": 34, "quantity": 5},
            {"id": 2, "name": "Apple", "price": 7, "quantity": 9},
        ]
db = DatabaseLayer(init_items=initial_items)


def test_get_item():
    item = db.get_item_by_id(2)
    assert item == {"id": 2, "name": "Apple", "price": 7, "quantity": 9}


def test_get_wrong_id_item():
    item = db.get_item_by_id(5)
    assert item is None


def test_add_item():
    new_item = db.add_item({"id": 0, "name": "New Item", "price": 555, "quantity": 444})
    assert new_item["id"] == 3


def test_update_item():
    db.update_item({"id": 2, "name": "Upd Apple", "price": 1, "quantity": 1})
    updated_item = db.get_item_by_id(2)
    assert updated_item == {"id": 2, "name": "Upd Apple", "price": 1, "quantity": 1}


def test_delete_item():
    db.delete_item(1)
    deleted = db.get_item_by_id(1)
    assert deleted is None
