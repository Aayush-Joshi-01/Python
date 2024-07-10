class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, item):
        self.menu_items[item.name] = item

    def display_menu(self):
        print("Menu:")
        for item in self.menu_items.values():
            print(f"{item.name}: ${item.price:.2f}")


class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name]['quantity'] += quantity
        else:
            self.items[item.name] = {'item': item, 'quantity': quantity}

    def calculate_total(self):
        total = sum(item_info['item'].price * item_info['quantity'] for item_info in self.items.values())
        return total


def main():
    menu = Menu()
    menu.add_item(MenuItem("Burger", 5.99))
    menu.add_item(MenuItem("Pizza", 8.99))
    menu.add_item(MenuItem("Salad", 3.99))
    menu.add_item(MenuItem("Drink", 1.99))

    order = Order()

    while True:
        print("\nRestaurant Order Handling System:")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Order")
        print("4. Calculate Total")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            menu.display_menu()
        elif choice == '2':
            item_name = input("Enter the name of the item to order: ")
            quantity = int(input("Enter the quantity: "))
            item = menu.menu_items.get(item_name)
            if item:
                order.add_item(item, quantity)
                print(f"Added {quantity} of '{item_name}' to your order.")
            else:
                print(f"Sorry, '{item_name}' is not on the menu.")
        elif choice == '3':
            if order.items:
                print("Your Order:")
                for item_info in order.items.values():
                    item = item_info['item']
                    quantity = item_info['quantity']
                    print(f"{item.name}: ${item.price:.2f} x {quantity}")
            else:
                print("Your order is empty.")
        elif choice == '4':
            if order.items:
                total = order.calculate_total()
                print(f"Total bill amount: ${total:.2f}")
            else:
                print("Your order is empty.")
        elif choice == '5':
            print("Exiting the restaurant order handling system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
