def update_inventory(product_id, quantity, inventory):
    if product_id in inventory:
        inventory[product_id]['quantity'] += quantity
        print(f"{quantity} units of product with ID {product_id} added to the inventory.")
    else:
        print(f"Product with ID {product_id} not found in the inventory.")


def add_product(product_id, name, quantity, inventory):
    if product_id not in inventory:
        inventory[product_id] = {'name': name, 'quantity': quantity}
        print(f"Product with ID {product_id} added to the inventory.")
    else:
        print(f"Product with ID {product_id} already exists in the inventory.")


if __name__ == '__main__':
    inventory = {
        1001: {'name': 'I Phone 13', 'quantity': 50},
        1002: {'name': 'I Pad Air', 'quantity': 75},
        1003: {'name': 'Apple Watch Ultra', 'quantity': 100}
    }
    update_inventory(1001, 25, inventory)
    update_inventory(1004, 10, inventory)
    add_product(1005, 'Macbook Air', 20, inventory)
    add_product(1001, 'Macbook Pro', 30, inventory)
    print(inventory)
