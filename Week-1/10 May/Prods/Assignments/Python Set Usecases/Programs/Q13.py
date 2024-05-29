def find_out_of_stock_products(warehouse_product_stock):
    out_of_stock_products = set()
    for warehouse in warehouse_product_stock:
        out_of_stock_products.update(product for product in warehouse_product_stock[warehouse] if
                                     product not in warehouse_product_stock[warehouse] or
                                     warehouse_product_stock[warehouse][product] <= 0)
    return out_of_stock_products


if __name__ == '__main__':
    warehouse_product_stock = {
        "warehouse1": {
            "product1": 10,
            "product2": 5,
            "product3": 0,
            "product4": 15,
        },
        "warehouse2": {
            "product1": 0,
            "product2": 8,
            "product3": 12,
            "product4": 0,
        },
        "warehouse3": {
            "product1": 12,
            "product2": 0,
            "product3": 8,
            "product4": 10,
        },
    }
    out_of_stock_products = find_out_of_stock_products(warehouse_product_stock)
    print(out_of_stock_products)
