# You're building a recommendation system for an e-commerce platform.
# Write a Python function to find the most frequently purchased products given a list of orders.
from collections import Counter


def most_frequent_products(orders):
    # Flatten the list of orders into a single list of products
    products = [product for order in orders for product in order]
    # Count the occurrences of each product
    product_counts = Counter(products)
    # Return the n most frequent products
    return product_counts.most_common()


if __name__ == '__main__':
    orders = [
        ['product1', 'product2', 'product3'],
        ['product2', 'product3', 'product4'],
        ['product1', 'product2', 'product3'],
        ['product1', 'product3', 'product5'],
    ]

    most_frequent = most_frequent_products(orders)
    print(most_frequent)
