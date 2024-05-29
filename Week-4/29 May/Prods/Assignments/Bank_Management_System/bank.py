from account import Account
from exceptions import AccountNotFoundError, InsufficientFundsError, AccountAlreadyExistsError, InvalidInitialBalanceError
from datetime import datetime
import json
from decorators import save_accounts_decorator, log_transaction_decorator
from typing import Optional

class Bank:
    transactions_file = "transactions.json"

    @staticmethod
    def load_transactions() -> dict:
        try:
            with open(Bank.transactions_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    @staticmethod
    @save_accounts_decorator
    @log_transaction_decorator("create_account")
    def create_account(account_number: str, name: str, ifsc_code: str, branch_name: str, state: str, district: str, country: str, account_type: str, initial_balance: float = 0) -> Account:
        if account_number in Account.accounts:
            raise AccountAlreadyExistsError("Account already exists")
        new_account = Account(account_number, name, ifsc_code, branch_name, state, district, country, account_type, initial_balance)
        Account.accounts[account_number] = new_account
        print(f"Account {account_number} created with initial balance {initial_balance}")
        return new_account

    @staticmethod
    def get_account(account_number: str) -> Account:
        if account_number not in Account.accounts:
            raise AccountNotFoundError("Account not found")
        return Account.accounts[account_number]

    @staticmethod
    @save_accounts_decorator
    @log_transaction_decorator("deposit")
    def deposit(account_number: str, amount: float) -> None:
        account = Bank.get_account(account_number)
        account.credit(amount)
        print(f"Deposited {amount} to {account}")

    @staticmethod
    @save_accounts_decorator
    @log_transaction_decorator("credit")
    def credit(account_number: str, amount: float) -> None:
        account = Bank.get_account(account_number)
        account.credit(amount)
        print(f"Credited {amount} to {account}")

    @staticmethod
    def statement(account_number: str) -> None:
        account = Bank.get_account(account_number)
        print(account)

    @staticmethod
    @save_accounts_decorator
    def transfer(from_account: str, to_account: str, amount: float) -> None:
        from_acc = Bank.get_account(from_account)
        to_acc = Bank.get_account(to_account)
        from_acc.debit(amount)
        to_acc.credit(amount)
        Bank.log_transaction("transfer_out", from_account, amount, target_account=to_account)
        Bank.log_transaction("transfer_in", to_account, amount, target_account=from_account)
        print(f"Transferred {amount} from {from_acc} to {to_acc}")

    @staticmethod
    def log_transaction(transaction_type: str, account_number: str, amount: float, target_account: Optional[str] = None) -> None:
        transactions = Bank.load_transactions()
        if account_number not in transactions:
            transactions[account_number] = []
        transaction_details = {
            "transaction_type": transaction_type,
            "amount": amount,
            "date": str(datetime.now()),
            "target_account": target_account
        }
        transactions[account_number].append(transaction_details)
        with open(Bank.transactions_file, 'w') as f:
            json.dump(transactions, f)
