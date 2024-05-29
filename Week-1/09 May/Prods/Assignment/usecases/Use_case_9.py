# You're developing a program to manage a restaurant's menu.
# Write a Python function to find the average price of menu items categorized under a specific section.

def average_price(menu, section):
    items = menu.get(section, [])
    total_price = sum(item['price'] for item in items)
    average_price = total_price / len(items) if items else 0
    return average_price


if __name__ == '__main__':
    menu = {
        'Appetizers': [
            {'name': 'Bruschetta', 'price': 7.99},
            {'name': 'Calamari', 'price': 9.99},
            {'name': 'Fried Mozzarella', 'price': 8.99}
        ],
        'Entrees': [
            {'name': 'Spaghetti Bolognese', 'price': 13.99},
            {'name': 'Grilled Chicken', 'price': 16.99},
            {'name': 'Fish and Chips', 'price': 15.99}
        ],
        'Desserts': [
            {'name': 'Tiramisu', 'price': 6.99},
            {'name': 'Cheesecake', 'price': 7.99},
            {'name': 'Ice Cream Sundae', 'price': 5.99}
        ]
    }
    average_price_appetizers = average_price(menu, 'Appetizers')
    print(f"Average price of Appetizers: {average_price_appetizers:.2f}")

    average_price_desserts = average_price(menu, 'Desserts')
    print(f"Average price of Desserts: {average_price_desserts:.2f}")
