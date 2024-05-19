def print_order_details(order):
    print(f"Order ID: {order['id']}")
    print(f"Customer ID: {order['customer_id']}")
    print(f"Items:")
    for item in order['items']:
        print(f"- Product ID: {item['product_id']}, Quantity: {item['quantity']}, Price: {item['price']}")
    print(f"Total Amount: {order['total_amount']}")


if __name__ == '__main__':
    order = {
        'id': 1001,
        'customer_id': 2001,
        'items': [
            {'product_id': 3001, 'quantity': 2, 'price': 50},
            {'product_id': 3002, 'quantity': 1, 'price': 100},
            {'product_id': 3003, 'quantity': 3, 'price': 20}
        ],
        'total_amount': 190
    }
    print_order_details(order)