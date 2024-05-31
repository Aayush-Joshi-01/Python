# Bank Management System

This is a CLI-based bank management system written in Python. It provides functionalities for creating accounts,
depositing funds, crediting funds, viewing account statements, transferring funds between accounts, and viewing
transaction histories.

## Features

- Create Account: Create a new bank account with various details such as account number, name, IFSC code, branch name,
  state, district, country, account type, and initial balance.

- Deposit: Deposit an amount into a specified account.

- Credit: Credit an amount into a specified account.

- Statement: View the statement of a specified account.

- Transfer: Transfer an amount from one account to another.

- View Transactions: View the transaction history of a specified account.

- Exit: Exit the application.

## Requirements

- Python 3.7 or higher

## Installation

Install the required packages:

```bash

    pip install -r requirements.txt

```

## Usage

Run the `interface.py` file to start the application:

```bash

python interface.py

```

## Login

```bash
# use this as the username
admin
# user the given password
123
```

## File Structure

- `account.py`: Defines the `Account` class and handles account-related operations.

- `bank.py`: Defines the `Bank` class which provides static methods for various bank operations.

- `exceptions.py`: Custom exceptions used in the application.

- `interface.py`: The main entry point for the CLI application.

- `transactions.py`: Defines the `Transaction` class and handles transaction validation.

- `urls.py`: Mimics URL routing functionality to map functions to commands.

- `decorators.py`: The main entry point for the CLI application verifies the admin login.

## Example

Upon running the application, you will see the following menu:

```

1: Create Account

2: Deposit

3: Credit

4: Statement

5: Transfer

6: View Transactions

7: Exit

Enter choice:

```

Follow the prompts to perform various banking operations.

## License

This project is licensed under the MIT License.

