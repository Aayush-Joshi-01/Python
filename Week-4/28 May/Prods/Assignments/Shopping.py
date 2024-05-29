class Item:
    """
    This is Custom defined Data Type 'Item'
    with 2 Instance Attribute name and price we can add this for future prospects.
    """

    def __init__(self, name: str, price: float):
        if not name:
            raise ValueError("Item name cannot be empty.")
        if price < 0:
            raise ValueError("Item price cannot be negative.")
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item(name={self.name}, price={self.price:.2f})"


class ShoppingCart:
    """
    This is the shopping cart storing all the items to be saved in the cart for item management
    the functions involved are :
        def add_item(self, item: Item) -> None
        def remove_item(self, item: Item) -> None
        def get_total(self) -> tuple[int | float, int]
        def __str__(self) -> str
        def __len__(self) -> int
        we have using len() as well in this

    Here _items is a protected member
    """
    DISCOUNT_THRESHOLD_1 = 10000
    DISCOUNT_RATE_1 = 0.10
    DISCOUNT_THRESHOLD_2 = 30000
    DISCOUNT_RATE_2 = 0.15

    def __init__(self):
        self._items = []

    def add_item(self, item: Item) -> None:
        if not isinstance(item, Item):
            raise TypeError("Only Item instances can be added to the cart.")
        quantity = input("Enter the quantity: ")
        for _ in range(int(quantity)):
            self._items.append(item)
        print(f"Added {item} to the cart.")

    def remove_item(self, item: Item) -> None:
        if item in self._items:
            self._items.remove(item)
            print(f"Removed {item} from the cart.")
        else:
            raise ValueError(f"Item {item} not found in the cart.")

    def get_total(self) -> tuple[int | float, int]:
        total = sum(item.price for item in self._items)
        discount = 0
        if total > self.DISCOUNT_THRESHOLD_2:
            discount = total * self.DISCOUNT_RATE_2
        elif total > self.DISCOUNT_THRESHOLD_1:
            discount = total * self.DISCOUNT_RATE_1
        final_total = total - discount
        return final_total, discount

    def clear_list(self):
        self._items = []

    def __str__(self) -> str:
        item_list = "\n".join(str(item) for item in self._items)
        total, discount = self.get_total()
        return (f"ShoppingCart contains:\n{item_list}\n"
                f"Total (before discount): {total + discount:.2f}\n"
                f"Discount: {discount:.2f}\n"
                f"Total (after discount): {total:.2f}")

    def __len__(self) -> int:
        return len(self._items)


class Menu:
    """
    This the menu class for menu-driven program with menu management methods
    functions involve are:
        display_menu()
        run()
        add_item()
        remove_item()
        view_cart()
        checkout()
    """

    def __init__(self):
        self.cart = ShoppingCart()

    @staticmethod
    def display_menu() -> None:
        print("Shopping Cart Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

    def run(self) -> None:
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.remove_item()
            elif choice == '3':
                self.view_cart()
            elif choice == '4':
                self.checkout()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

    def add_item(self) -> None:
        name = input("Enter item name: ")
        try:
            price = float(input("Enter item price: "))
            item = Item(name, price)
            self.cart.add_item(item)
        except ValueError as e:
            print(f"Error: {e}")

    def remove_item(self) -> None:
        self.view_cart()
        name = input("Enter item name to remove: ")
        validate = input("Are you sure you want to remove the item [y/n]: ")
        if validate in ['y', 'yes']:
            items_to_remove = [item for item in self.cart._items if item.name == name]
            if not items_to_remove:
                print(f"Item '{name}' not found in the cart.")
                return
            item = items_to_remove[0]
            try:
                self.cart.remove_item(item)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Removal cancelled.")

    def view_cart(self) -> None:
        print(self.cart)

    def checkout(self) -> None:
        total, discount = self.cart.get_total()
        print(f"Total cost (before discount): {total + discount:.2f}")
        print(f"Discount applied: {discount:.2f}")
        print(f"Total cost (after discount): {total:.2f}")
        print("Thank you for shopping!")
        self.cart.clear_list()


if __name__ == '__main__':
    menu = Menu()
    menu.run()
