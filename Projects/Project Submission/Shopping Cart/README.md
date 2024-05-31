# Shopping Cart System

This is a Python-based shopping cart system that allows users to manage items in a shopping cart, view available
products in a mart, and perform checkout operations with applied discounts. The project is structured into multiple
classes to handle different functionalities such as item management, shopping cart operations, product loading from a
JSON file, and a menu-driven interface for user interaction.

## Features

- **Item Management:** Add, remove, and view items in the shopping cart.
- **Discount System:** Apply discounts based on total cart value.
- **Product Loading:** Load product data from a JSON file.
- **Menu-Driven Interface:** User-friendly interface to interact with the shopping cart system.

## Classes

- **Item:** Represents an item with a name and price.
- **ShoppingCart:** Manages the list of items in the cart, applies discounts, and calculates totals.
- **Mart:** Loads and displays products from a JSON file.
- **Menu:** Provides a menu-driven interface for the user to interact with the system.

## Installation

1. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare the product data:**
    - Create a JSON file named `shopping_mart.json` in the project directory.
    - Add product data in the following format:
      ```json
      [
        {"name": "Product1", "price": 100.0},
        {"name": "Product2", "price": 200.0},
         ...
      ]
      ```

## Usage

1. **Run the program:**
   ```bash
   python Shopping.py
   ```

2. **Follow the on-screen instructions to interact with the shopping cart system:**
    - View available products.
    - Add items to the cart by specifying the name and price.
    - Remove items from the cart.
    - View the cart contents.
    - Checkout to see the total cost and applied discounts.

## Requirements

- Python 3.7+
- Required packages are listed in the `requirements.txt` file.

## Contributing

- Fork the repository.
- Create a new branch.
- Make your changes and commit them.
- Push to the branch.
- Open a pull request.

## License

This project is licensed under the MIT License.

---