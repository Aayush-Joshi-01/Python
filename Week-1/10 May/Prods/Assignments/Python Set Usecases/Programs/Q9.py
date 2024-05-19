def find_unique_categories_in_departments(product_data, department1, department2):
    categories_in_department1 = set()
    categories_in_department2 = set()
    for data in product_data:
        if data["department"] == department1:
            categories_in_department1.add(data["category"])
        elif data["department"] == department2:
            categories_in_department2.add(data["category"])
    return categories_in_department1 & categories_in_department2


if __name__ == '__main__':
    product_data = [
        {"category": "laptop", "department": "electronics"},
        {"category": "shirt", "department": "clothing"},
        {"category": "smart clothing", "department": "clothing"},
        {"category": "smartphone", "department": "electronics"},
        {"category": "pants", "department": "clothing"},
        {"category": "headphones", "department": "electronics"},
        {"category": "jacket", "department": "clothing"},
        {"category": "tablet", "department": "electronics"},
        {"category": "shoes", "department": "clothing"},
        {"category": "television", "department": "electronics"},
        {"category": "smart clothing", "department": "electronics"}
    ]
    unique_categories = find_unique_categories_in_departments(product_data, "electronics", "clothing")
    print(unique_categories)