def calculate_total_revenue(sales_data):
    total_revenue = 0
    for sale in sales_data:
        total_revenue += sale['price'] * sale['quantity_sold']
    return total_revenue


def get_best_selling_product(sales_data):
    best_selling_product = None
    max_quantity_sold = 0
    for sale in sales_data:
        if sale['quantity_sold'] > max_quantity_sold:
            max_quantity_sold = sale['quantity_sold']
            best_selling_product = sale
    return best_selling_product


def calculate_total_profit_margin(sales_data):
    total_profit_margin = 0
    for sale in sales_data:
        profit_margin = (sale['price'] - sale['cost_price']) * sale['quantity_sold']
        total_profit_margin += profit_margin
    return total_profit_margin


if __name__ == '__main__':
    sales_data = [
        {'product_id': 1001, 'product_name': 'Laptop', 'quantity_sold': 10, 'price': 800, 'cost_price': 600},
        {'product_id': 1002, 'product_name': 'Smartphone', 'quantity_sold': 20, 'price': 600, 'cost_price': 400},
        {'product_id': 1003, 'product_name': 'Shirt', 'quantity_sold': 30, 'price': 30, 'cost_price': 15},
        {'product_id': 1004, 'product_name': 'Pants', 'quantity_sold': 40, 'price': 40, 'cost_price': 20},
        {'product_id': 1005, 'product_name': 'Book', 'quantity_sold': 50, 'price': 15, 'cost_price': 10},
        {'product_id': 1006, 'product_name': 'Headphones', 'quantity_sold': 15, 'price': 100, 'cost_price': 80},
    ]
    total_revenue = calculate_total_revenue(sales_data)
    print(f"Total revenue generated from sales: {total_revenue}")
    best_selling_product = get_best_selling_product(sales_data)
    print(f"Best-selling product: {best_selling_product['product_name']} (ID: {best_selling_product['product_id']})")
    total_profit_margin = calculate_total_profit_margin(sales_data)
    print(f"Total profit margin: {total_profit_margin}")