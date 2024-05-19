def search_products(products, search_criteria):
    matching_products = []
    for product in products:
        for key, value in search_criteria.items():
            if key == 'price_range':
                if product['price'] >= value[0] and product['price'] <= value[1]:
                    matching_products.append(product)
                    break
            else:
                if product[key] == value:
                    matching_products.append(product)
                    break
    return sorted(matching_products, key=lambda x: x['price'])


if __name__ == '__main__':
    products = [
        {'product_id': 1001, 'name': 'Laptop', 'category': 'Electronics', 'price': 800},
        {'product_id': 1002, 'name': 'Smartphone', 'category': 'Electronics', 'price': 600},
        {'product_id': 1003, 'name': 'Shirt', 'category': 'Clothing', 'price': 30},
        {'product_id': 1004, 'name': 'Pants', 'category': 'Clothing', 'price': 40},
        {'product_id': 1005, 'name': 'Book', 'category': 'Books', 'price': 15},
        {'product_id': 1006, 'name': 'Headphones', 'category': 'Electronics', 'price': 100},
    ]
    search_criteria = {
        'name': 'Laptop',
        'category': 'Electronics',
        'price_range': [500, 1000],
    }
    matching_products = search_products(products, search_criteria)
    print(f"Matching products:")
    for product in matching_products:
        print(f"Product ID: {product['product_id']}, Name: {product['name']}, Category: {product['category']}, Price: {product['price']}")
