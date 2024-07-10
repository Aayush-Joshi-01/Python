from functools import wraps

from transactions import Transactions


def save_accounts_decorator(func):
    """
    A decorator that saves the accounts after calling the decorated function.

    Args:
        func: The function to decorate.

    Returns:
        A wrapped function that saves the accounts after calling the decorated function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        Transactions.save_accounts()
        return result

    return wrapper


def log_transaction_decorator(transaction_type):
    """
    A decorator that logs a transaction after calling the decorated function.

    Args:
        transaction_type: The type of transaction to log.

    Returns:
        A decorator function that logs the transaction after calling the decorated function.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            account_number = args[0]
            amount = args[1]
            target_account = kwargs.get('target_account')
            Transactions.log_transaction(transaction_type, account_number, amount, target_account)
            return result

        return wrapper

    return decorator
