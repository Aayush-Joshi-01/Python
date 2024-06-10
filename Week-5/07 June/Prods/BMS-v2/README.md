# Bank Management System

## Overview

This is a simple command-line based Bank Management System implemented in Python. It follows the MVC (Model-View-Controller) architecture and uses a SQL database for data storage. The application allows you to perform various banking operations such as creating an account, depositing money, debiting money, viewing account details, transferring money, and viewing transaction logs.

## Project Structure

```
bank_management/
│
├── .venv/
│   ├── Include
│   ├── Lib/..
│   ├── Scripts/..
│   ├── pyvenv.cfg
│
├── models/
│   ├── __init__.py
│   ├── account.py
│   ├── transaction.py
│   ├── log.py
│
├── controllers/
│   ├── __init__.py
│   ├── bank_controller.py
│   ├── transaction_controller.py
│
├── views/
│   ├── __init__.py
│   ├── interface.py
│
├── decorators/
│   ├── __init__.py
│   ├── login_decorator.py
│
├── exceptions/
│   ├── __init__.py
│   ├── custom_exceptions.py
│
├── db/
│   ├── __init__.py
│   ├── database.py
│
├── routes/
│   ├── __init__.py
│   ├── url.py
│
├── views/
│   ├── __init__.py
│   ├── interface.py
│
├── requirements.txt
├── README.md
```

## Features

- **Create Account:** Create a new bank account.
- **Debit:** Withdraw money from an account.
- **Credit:** Deposit money into an account.
- **Get Account Details:** View the details of an account.
- **Transfer:** Transfer money between accounts.
- **View Transactions:** View the transaction history of an account.

## Setup

1. Install the required packages:

    ```shell
    pip install -r requirements.txt
    ```

2. Set up the database:

    - Create a MySQL database and update the connection details in `db/database.py`.

3. Run the application:

    ```shell
    cd views
    python interface.py
    ```

## Usage

1. Run the application:

    ```shell
    cd views
    python interface.py
    ```

2. Use the following username and password
   ```commandline
   username: admin
   password: 123
   ```

3. Follow the on-screen instructions to perform various banking operations.
   ```commandline
   Enter the admin Username: admin
   Enter the admin Password: 123
   1: Create Account
   2: Deposit
   3: Debit
   4: Credit
   5: Get Account Details
   6: Transfer
   7: View Transactions
   8: Exit
   Enter choice:
   ```


## Requirements

- Python 3.x
- pymysql
- Other dependencies listed in `requirements.txt`

## License

This project is licensed under the MIT License.