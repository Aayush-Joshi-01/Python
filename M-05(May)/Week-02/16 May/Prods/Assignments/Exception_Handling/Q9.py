class ItemOutOfStockException(Exception):
    pass


class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item.stock < quantity:
            raise ItemOutOfStockException(f"Item '{item.name}' is out of stock. Available stock: {item.stock}")
        if item.name in self.items:
            self.items[item.name]['quantity'] += quantity
        else:
            self.items[item.name] = {'item': item, 'quantity': quantity}
        item.stock -= quantity

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your shopping cart:")
            for item_info in self.items.values():
                item = item_info['item']
                quantity = item_info['quantity']
                print(f"{item.name} - ${item.price:.2f} x {quantity} = ${item.price * quantity:.2f}")

    def checkout(self):
        if not self.items:
            print("Your cart is empty. Nothing to checkout.")
        else:
            total = sum(item_info['item'].price * item_info['quantity'] for item_info in self.items.values())
            print(f"Total amount: ${total:.2f}")
            print("Thank you for your purchase!")


def main():
    # Sample items in the store
    items = [
        Item("Laptop", 999.99, 5),
        Item("Headphones", 199.99, 10),
        Item("Coffee Maker", 49.99, 2),
        Item("Book", 14.99, 0)  # Out of stock item
    ]

    cart = ShoppingCart()

    while True:
        print("\nOnline Shopping Platform:")
        print("1. View Items")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            print("Available Items:")
            for item in items:
                print(item)
        elif choice == '2':
            item_name = input("Enter the name of the item to add to cart: ")
            quantity = int(input("Enter the quantity: "))
            item = next((item for item in items if item.name == item_name), None)
            if item:
                try:
                    cart.add_item(item, quantity)
                    print(f"Added {quantity} of '{item.name}' to your cart.")
                except ItemOutOfStockException as e:
                    print(e)
            else:
                print(f"Item '{item_name}' not found.")
        elif choice == '3':
            cart.view_cart()
        elif choice == '4':
            cart.view_cart()
            cart.checkout()
            break
        elif choice == '5':
            print("Exiting the online shopping platform. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
