# You're developing a program to manage inventory levels in a warehouse.
# Write a Python function to find the items that need restocking based on their current quantities and minimum threshold.

def find_items_to_restock(items, min_threshold):
    items_to_restock = []
    for item in items:
        if item['quantity'] < min_threshold:
            items_to_restock.append(item)
    return items_to_restock


if __name__ == '__main__':
    items = [
        {'name': 'item1', 'quantity': 15},
        {'name': 'item2', 'quantity': 5},
        {'name': 'item3', 'quantity': 20},
        {'name': 'item4', 'quantity': 8},
        {'name': 'item5', 'quantity': 12}
    ]

    min_threshold = 10

    items_to_restock = find_items_to_restock(items, min_threshold)
    for item in items_to_restock:
        print(item)
