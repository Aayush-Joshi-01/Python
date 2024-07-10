def calculate_total_amount(order):
    total_amount = 0
    for item in order['items']:
        total_amount += item['price'] * item['quantity'] * (1 - item['discount'])
    return total_amount


def calculate_total_discount(order):
    total_discount = 0
    for item in order['items']:
        total_discount += item['price'] * item['quantity'] * item['discount']
    return total_discount


if __name__ == '__main__':
    order = {
        'order_id': 1001,
        'customer_name': 'John Doe',
        'items': [
            {'product_id': 1001, 'name': 'Laptop', 'price': 800, 'quantity': 1, 'discount': 0.1},
            {'product_id': 1002, 'name': 'Smartphone', 'price': 600, 'quantity': 2, 'discount': 0.05},
            {'product_id': 1003, 'name': 'Shirt', 'price': 30, 'quantity': 3, 'discount': 0},
        ],
    }
    total_amount = calculate_total_amount(order)
    print(f"Total amount of order #{order['order_id']} is: ${total_amount:.2f}")
    total_discount = calculate_total_discount(order)
    print(f"Total discount applied to order #{order['order_id']} is: ${total_discount:.2f}")
    print(f"Detailed view of order #{order['order_id']} for {order['customer_name']}:\n")
    for item in order['items']:
        print(f"Product ID: {item['product_id']}, "
              f"Name: {item['name']}, "
              f"Price: ${item['price']:.2f}, "
              f"Quantity: {item['quantity']}, "
              f"Discount: {item['discount']:.2f}, "
              f"Total: ${item['price'] * item['quantity'] * (1 - item['discount']):.2f}")
