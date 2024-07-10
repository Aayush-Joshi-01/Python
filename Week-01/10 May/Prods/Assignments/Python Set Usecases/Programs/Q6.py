def find_frequent_products(transactions):
    unique_products = set()
    for transaction in transactions:
        unique_products.update(transaction)
    return unique_products


if __name__ == '__main__':
    transactions = [
        ["product1", "product2", "product3"],
        ["product2", "product3", "product4"],
        ["product1", "product3", "product4"],
        ["product1", "product2", "product4"],
        ["product2", "product3", "product4"],
    ]
    frequent_products = find_frequent_products(transactions)
    print(frequent_products)
