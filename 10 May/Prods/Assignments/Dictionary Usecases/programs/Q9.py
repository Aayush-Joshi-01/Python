def get_total_orders_by_customer(orders):
    order_count = {}
    for order in orders:
        customer_id = order['customer_id']
        if customer_id not in order_count:
            order_count[customer_id] = 0
        order_count[customer_id] += 1
    return order_count

if __name__ == '__main__':
    orders = [
        {'customer_id': 1001, 'order_id': 1001, 'total_amount': 50},
        {'customer_id': 1002, 'order_id': 1002, 'total_amount': 100},
        {'customer_id': 1001, 'order_id': 1003, 'total_amount': 75},
        {'customer_id': 1003, 'order_id': 1004, 'total_amount': 25},
        {'customer_id': 1002, 'order_id': 1005, 'total_amount': 200},
        {'customer_id': 1001, 'order_id': 1006, 'total_amount': 100},
    ]
    total_orders_by_customer = get_total_orders_by_customer(orders)
    print(f"Total number of orders placed by each customer:")
    for customer_id, order_count in total_orders_by_customer.items():
        print(f"Customer ID {customer_id}: {order_count} orders")