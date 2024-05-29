import json
from datetime import datetime
from functools import wraps
from account import Account
from bank import Bank


def save_accounts_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(Account.accounts_file, 'w') as f:
            accounts_data = {acc_number: acc.__dict__ for acc_number, acc in Account.accounts.items()}
            json.dump(accounts_data, f)
        return result

    return wrapper


def log_transaction_decorator(transaction_type):
    def decorator(func):
        @wraps(func)
        def wrapper(account_number, *args, **kwargs):
            result = func(account_number, *args, **kwargs)
            transactions = Bank.load_transactions()
            if account_number not in transactions:
                transactions[account_number] = []
            transaction_details = {
                "transaction_type": transaction_type,
                "amount": args[0],
                "date": str(datetime.now()),
                "target_account": kwargs.get('target_account')
            }
            transactions[account_number].append(transaction_details)
            with open(Bank.transactions_file, 'w') as f:
                json.dump(transactions, f)
            return result

        return wrapper

    return decorator
