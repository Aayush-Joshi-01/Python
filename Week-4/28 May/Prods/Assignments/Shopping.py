import json
from typing import List, Tuple


class Item:
    """
    This is a custom defined Data Type 'Item'
    with 2 instance attributes name and price.
    """

    def __init__(self, name: str, price: float):
        """
        Initializes an Item instance.

        :param name: The name of the item.
        :param price: The price of the item.
        :raises ValueError: If name is empty or price is negative.
        """
        if not name:
            raise ValueError("Item name cannot be empty.")
        if price < 0:
            raise ValueError("Item price cannot be negative.")
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Returns a string representation of the Item instance.

        :return: String representation of the item.
        """
        return f"Item(name={self.name}, price={self.price:.2f})"


class ShoppingCart:
    """
    This is the shopping cart storing all the items to be saved in the cart for item management.
    """
    DISCOUNT_THRESHOLD_1 = 10000
    DISCOUNT_RATE_1 = 0.10
    DISCOUNT_THRESHOLD_2 = 30000
    DISCOUNT_RATE_2 = 0.15

    def __init__(self):
        """
        Initializes a ShoppingCart instance with an empty list of items.
        """
        self._items: List[Item] = []

    def add_item(self, item: Item) -> None:
        """
        Adds an item to the shopping cart.

        :param item: The item to add.
        :raises TypeError: If the item is not an instance of Item.
        """
        if not isinstance(item, Item):
            raise TypeError("Only Item instances can be added to the cart.")
        quantity = input("Enter the quantity: ")
        for _ in range(int(quantity)):
            self._items.append(item)
        print(f"Added {item} to the cart.")

    def remove_item(self, item: Item) -> None:
        """
        Removes an item from the shopping cart.

        :param item: The item to remove.
        :raises ValueError: If the item is not found in the cart.
        """
        if item in self._items:
            self._items.remove(item)
            print(f"Removed {item} from the cart.")
        else:
            raise ValueError(f"Item {item} not found in the cart.")

    def get_total(self) -> Tuple[float, float]:
        """
        Calculates the total price and the discount applied to the shopping cart.

        :return: A tuple containing the final total price and the discount.
        """
        total = sum(item.price for item in self._items)
        discount = 0
        if total > self.DISCOUNT_THRESHOLD_2:
            discount = total * self.DISCOUNT_RATE_2
        elif total > self.DISCOUNT_THRESHOLD_1:
            discount = total * self.DISCOUNT_RATE_1
        final_total = total - discount
        return final_total, discount

    def clear_list(self) -> None:
        """
        Clears all items from the shopping cart.
        """
        self._items = []

    def __str__(self) -> str:
        """
        Returns a string representation of the shopping cart.

        :return: String representation of the shopping cart.
        """
        item_list = "\n".join(str(item) for item in self._items)
        total, discount = self.get_total()
        return (f"ShoppingCart contains:\n{item_list}\n"
                f"Total (before discount): {total + discount:.2f}\n"
                f"Discount: {discount:.2f}\n"
                f"Total (after discount): {total:.2f}")

    def __len__(self) -> int:
        """
        Returns the number of items in the shopping cart.

        :return: Number of items in the cart.
        """
        return len(self._items)


class Mart:
    """
    This class represents the mart with prebuilt data loaded from a JSON file.
    """

    def __init__(self, filename: str = "shopping_mart.json"):
        """
        Initializes a Mart instance and loads products from a JSON file.

        :param filename: The name of the JSON file containing the mart data.
        """
        self.filename = filename
        self.products = self.load_products()

    def load_products(self) -> List[dict]:
        """
        Loads products from a JSON file.

        :return: A list of products.
        :raises FileNotFoundError: If the JSON file is not found.
        :raises json.JSONDecodeError: If there is an error decoding the JSON file.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {self.filename}.")
            return []

    def display_products(self) -> None:
        """
        Displays the products available in the mart.
        """
        if not self.products:
            print("No products available in the mart.")
        else:
            print("Available products in the mart:")
            for product in self.products:
                print(f"Name: {product['name']}, Price: {product['price']:.2f}")


class Menu:
    """
    This is the menu class for a menu-driven program with menu management methods.
    """

    def __init__(self):
        """
        Initializes a Menu instance with a shopping cart and a mart.
        """
        self.cart = ShoppingCart()
        self.mart = Mart()

    @staticmethod
    def display_menu() -> None:
        """
        Displays the shopping cart menu options.
        """
        print("Shopping Cart Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

    def run(self) -> None:
        """
        Runs the menu-driven program.
        """
        self.mart.display_products()
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

            if input("Would you like to view the mart again? (yes/no): ").lower() in ['yes', 'y']:
                self.mart.display_products()

    def add_item(self) -> None:
        """
        Adds an item to the shopping cart based on user input.
        """
        name = input("Enter item name: ")
        try:
            price = float(input("Enter item price: "))
            item = Item(name, price)
            self.cart.add_item(item)
        except ValueError as e:
            print(f"Error: {e}")

    def remove_item(self) -> None:
        """
        Removes an item from the shopping cart based on user input.
        """
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
        """
        Displays the current items in the shopping cart.
        """
        print(self.cart)

    def checkout(self) -> None:
        """
        Displays the total cost, discount applied, and clears the cart.
        """
        total, discount = self.cart.get_total()
        print(f"Total cost (before discount): {total + discount:.2f}")
        print(f"Discount applied: {discount:.2f}")
        print(f"Total cost (after discount): {total:.2f}")
        print("Thank you for shopping!")
        self.cart.clear_list()


if __name__ == '__main__':
    menu = Menu()
    menu.run()
