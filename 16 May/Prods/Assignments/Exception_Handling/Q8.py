class ItemNotFoundException(Exception):
    pass


class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def update_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity} unit(s)"


class GroceryStoreInventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, name, quantity):
        if name in self.inventory:
            self.inventory[name].quantity += quantity
        else:
            self.inventory[name] = InventoryItem(name, quantity)

    def update_item(self, name, quantity):
        if name not in self.inventory:
            raise ItemNotFoundException(f"Item '{name}' not found in inventory.")
        self.inventory[name].update_quantity(quantity)

    def remove_item(self, name):
        if name not in self.inventory:
            raise ItemNotFoundException(f"Item '{name}' not found in inventory.")
        del self.inventory[name]

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for item in self.inventory.values():
                print(item)

    def search_item(self, name):
        if name in self.inventory:
            return self.inventory[name]
        else:
            raise ItemNotFoundException(f"Item '{name}' not found in inventory.")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("The number must be non-negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")


def main():
    inventory = GroceryStoreInventory()

    while True:
        print("\nGrocery Store Inventory Management System:")
        print("1. Add Item")
        print("2. Update Item Quantity")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. Search for an Item")
        print("6. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            name = input("Enter the name of the item to add: ")
            quantity = get_positive_integer("Enter the quantity: ")
            inventory.add_item(name, quantity)
            print(f"Added {quantity} unit(s) of '{name}' to inventory.")
        elif choice == '2':
            name = input("Enter the name of the item to update: ")
            quantity = get_positive_integer("Enter the new quantity: ")
            try:
                inventory.update_item(name, quantity)
                print(f"Updated '{name}' to {quantity} unit(s) in inventory.")
            except ItemNotFoundException as e:
                print(e)
        elif choice == '3':
            name = input("Enter the name of the item to remove: ")
            try:
                inventory.remove_item(name)
                print(f"Removed '{name}' from inventory.")
            except ItemNotFoundException as e:
                print(e)
        elif choice == '4':
            print("Current Inventory:")
            inventory.view_inventory()
        elif choice == '5':
            name = input("Enter the name of the item to search for: ")
            try:
                item = inventory.search_item(name)
                print(f"Found: {item}")
            except ItemNotFoundException as e:
                print(e)
        elif choice == '6':
            print("Exiting the inventory management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
