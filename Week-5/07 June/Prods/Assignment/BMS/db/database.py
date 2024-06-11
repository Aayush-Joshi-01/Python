import pymysql
from pymysql.cursors import DictCursor


def get_db_connection():
    """
    Establishes and returns a connection to the MySQL database.

    :return: Connection object to the MySQL database.
    """
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='bank_management',
        cursorclass=DictCursor
    )
    return connection


def initialize_db():
    """
    Initializes the database by creating the necessary tables if they do not exist.
    """
    connection = get_db_connection()
    try:

        with connection.cursor() as cursor:

            # Create bank_management database
            cursor.execute("""
                        CREATE DATABASE IF NOT EXISTS bank_management
                        """)
            connection.select_db('bank_management')

            # Create accounts table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_management.accounts (
                account_number VARCHAR(20) PRIMARY KEY,
                name VARCHAR(255),
                ifsc_code VARCHAR(20),
                branch_name VARCHAR(255),
                state VARCHAR(255),
                district VARCHAR(255),
                country VARCHAR(255),
                account_type ENUM('savings', 'zero_balance_savings'),
                balance FLOAT
            )
            """)

            # Create transactions table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_management.transactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                account_number VARCHAR(20),
                type ENUM('deposit', 'credit', 'transfer'),
                amount FLOAT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                target_account VARCHAR(20),
                FOREIGN KEY (account_number) REFERENCES accounts(account_number)
            )
            """)

            # Create logs table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_management.logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                action VARCHAR(255),
                account_number VARCHAR(20),
                amount FLOAT,
                target_account VARCHAR(20),
                error TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

        connection.commit()
    finally:
        connection.close()


if __name__ == '__main__':
    # Call this function once to initialize the database
    initialize_db()
