def search_by_name(name, products):
    return [product for product in products if name.lower() in product['name'].lower()]


def search_by_category(category, products):
    return [product for product in products if category.lower() == product['category'].lower()]


def search_by_price_range(min_price, max_price, products):
    return [product for product in products if min_price <= product['price'] <= max_price]


if __name__ == '__main__':
    products = [
        {'id': 1001, 'name': 'Laptop', 'category': 'Electronics', 'price': 800},
        {'id': 1002, 'name': 'Smartphone', 'category': 'Electronics', 'price': 600},
        {'id': 1003, 'name': 'Shirt', 'category': 'Clothing', 'price': 30},
        {'id': 1004, 'name': 'Pants', 'category': 'Clothing', 'price': 40},
        {'id': 1005, 'name': 'Book', 'category': 'Books', 'price': 15},
        {'id': 1006, 'name': 'Headphones', 'category': 'Electronics', 'price': 100},
    ]
    name_search = input("Enter the name of the product to search: ")
    name_results = search_by_name(name_search, products)
    print(f"Search results for '{name_search}':")
    for product in name_results:
        print(product)
    category_search = input("Enter the category of the product to search: ")
    category_results = search_by_category(category_search, products)
    print(f"\nSearch results for category '{category_search}':")
    for product in category_results:
        print(product)
    min_price = int(input("Enter the minimum price: "))
    max_price = int(input("Enter the maximum price: "))
    price_range_results = search_by_price_range(min_price, max_price, products)
    print(f"\nSearch results for price range ${min_price} - ${max_price}:")
    for product in price_range_results:
        print(product)
