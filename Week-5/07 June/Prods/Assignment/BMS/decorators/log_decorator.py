from functools import wraps
from db.database import get_db_connection
import pymysql


def log_action(func):
    """
    Decorator to log actions performed on bank accounts.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        account_number = args[0]  # Assuming the first argument is always the account number
        try:
            result = func(*args, **kwargs)
            action = func.__name__
            amount = kwargs.get('amount', 0)
            target_account = kwargs.get('to_account') or kwargs.get('target_account')

            log_to_db(action, account_number, amount, target_account)

            return result
        except Exception as e:
            log_to_db(func.__name__, account_number, 0, None, error=str(e))
            print(f"Error logging action: {e}")
            raise e

    return wrapper


def log_to_db(action: str, account_number: str, amount: float, target_account: str = None, error: str = None) -> None:
    """
    Function to log actions into the db.
    """
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO logs (action, account_number, amount, target_account, error)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (action, account_number, amount, target_account, error))
        connection.commit()
    finally:
        connection.close()
