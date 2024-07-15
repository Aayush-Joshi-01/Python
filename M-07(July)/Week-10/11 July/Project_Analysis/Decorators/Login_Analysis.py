import pymysql
from pymysql.cursors import DictCursor
from typing import Callable, Any


def create_db():
    """
    Creates the database if it does not exist.
    """
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root'
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                        CREATE DATABASE IF NOT EXISTS analysis_login
                        """)
        connection.commit()
    finally:
        connection.close()

def get_db_connection():
    """
    Establishes and returns a connection to the MySQL database.

    :return: Connection object to the MySQL database.
    """
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='analysis_login',
        cursorclass=DictCursor
    )
    return connection


def initialize_db():
    """
    Initializes the database by creating the necessary tables if they do not exist.
    """
    create_db()  # Create the database first
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Create accounts table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS analysis_login.login_accounts (
                username VARCHAR(20) PRIMARY KEY,
                password VARCHAR(255),
                role ENUM('DBA', 'BDA', 'DS', 'DE', 'DA')
            )
            """)
        connection.commit()
    finally:
        connection.close()


def analysis_login_system(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that checks if the user is logged in before calling the decorated function.

    Args:
        func: The function to decorate.

    Returns: the main function to execute the code
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        choice = input("Do you want to sign-in or signup or exit: ")
        while True:
            if choice.strip().lower() in ['signin', 'sign-in']:
                username = input("Enter the username: ")
                password = input("Enter the password: ")
                connection = get_db_connection()
                try:
                    with connection.cursor() as cursor:
                        cursor.execute("SELECT * FROM analysis_login.login_accounts WHERE username = %s AND password = %s", (username.strip(), password))
                        user = cursor.fetchone()
                        if user:
                            print("You are logged-in")
                            return func(*args, **kwargs)
                        else:
                            print("Invalid username or password. Please try again.")
                finally:
                    connection.close()
            elif choice.strip().lower() in ['signup', 'sign-up']:
                username = input("Enter the username: ")
                password = input("Enter the password: ")
                print("""Roles are (
                DBA: Database Administrator, 
                BDA: Business Development Analyst, 
                DS: Data Scientist, 
                DE: Data Engineer, 
                DA: Data Analyst
                )""")
                role = input("Enter the role (DBA, BDA, DS, DE, DA): ")
                if role in ['DBA', 'BDA', 'DS', 'DE', 'DA']:
                    pass
                else:
                    print("Invalid role. Please enter a valid role. Enter only the ID (Like BDA)")
                    continue
                connection = get_db_connection()
                try:
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO login_accounts (username, password, role) VALUES (%s, %s, %s)", (username.strip(), password, role.strip()))
                        connection.commit()
                        print("Account created successfully!")
                finally:
                    connection.close()
                    choice = input("Do you want to sign-in or signup: ")
                    continue
            elif choice.strip().lower() == 'exit':
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please enter 'signin' or 'signup' or 'exit.")
                choice = input("Do you want to sign-in or signup: ")
                continue
        
            # returns the wrapped function as not logged-in us

    return wrapper

if __name__ == '__main__':
    # Call this function once to initialize the database
    initialize_db()