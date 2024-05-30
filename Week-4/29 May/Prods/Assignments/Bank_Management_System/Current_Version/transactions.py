import json
from datetime import datetime
from typing import Optional

from account import Account
from exceptions import AccountNotFoundError, AccountAlreadyExistsError


class Transactions:
    """
        Handles transactions and account operations.

        Attributes:
            transactions_file (str): The file where transactions are stored.
        """
    transactions_file = "transactions.json"

    @staticmethod
    def load_transactions() -> dict:
        """
                Loads transactions from the transactions file.

                Returns:
                    dict: A dictionary of transactions.
                """
        try:
            with open(Transactions.transactions_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_transactions(transactions: dict) -> None:
        """
               Saves transactions to the transactions file.

               Args:
                   transactions (dict): A dictionary of transactions.
               """
        with open(Transactions.transactions_file, 'w') as f:
            json.dump(transactions, f)

    @staticmethod
    def log_transaction(transaction_type: str, account_number: str, amount: float,
                        target_account: Optional[str] = None) -> None:
        """
                Logs a transaction.

                Args:
                    transaction_type (str): The type of transaction.
                    account_number (str): The account number.
                    amount (float): The amount of the transaction.
                    target_account (Optional[str], optional): The target account number for transfer transactions. Defaults to None.
                """
        transactions = Transactions.load_transactions()
        if account_number not in transactions:
            transactions[account_number] = []
        transaction_details = {
            "transaction_type": transaction_type,
            "amount": amount,
            "date": str(datetime.now()),
            "target_account": target_account
        }
        transactions[account_number].append(transaction_details)
        Transactions.save_transactions(transactions)

    @staticmethod
    def create_account(account_number: str, name: str, ifsc_code: str, branch_name: str, state: str, district: str,
                       country: str, account_type: str, initial_balance: float = 0) -> Account:
        """
                Creates a new account.

                Args:
                    account_number (str): The account number.
                    name (str): The account holder's name.
                    ifsc_code (str): The IFSC code of the branch.
                    branch_name (str): The name of the branch.
                    state (str): The state where the branch is located.
                    district (str): The district where the branch is located.
                    country (str): The country where the branch is located.
                    account_type (str): The type of account.
                    initial_balance (float, optional): The initial balance of the account. Defaults to 0.

                Returns:
                    Account: The created account.

                Raises:
                    AccountAlreadyExistsError: If an account with the same account number already exists.
                """
        if account_number in Account.accounts:
            raise AccountAlreadyExistsError("Account already exists")
        new_account = Account(account_number, name, ifsc_code, branch_name, state, district, country, account_type,
                              initial_balance)
        Account.accounts[account_number] = new_account
        print(f"Account {account_number} created with initial balance {initial_balance}")
        Account.save_accounts()
        Transactions.log_transaction("create_account", account_number, initial_balance)
        return new_account

    @staticmethod
    def get_account(account_number: str) -> Account:
        """
                Gets an account by its account number.

                Args:
                    account_number (str): The account number.

                Returns:
                    Account: The account.

                Raises:
                    AccountNotFoundError: If the account is not found.
                """
        if account_number not in Account.accounts:
            raise AccountNotFoundError("Account not found")
        return Account.accounts[account_number]

    @staticmethod
    def deposit(account_number: str, amount: float) -> None:
        """
                Deposits money into an account.

                Args:
                    account_number (str): The account number.
                    amount (float): The amount to deposit.
                """
        account = Transactions.get_account(account_number)
        account.credit(amount)
        Account.save_accounts()
        Transactions.log_transaction("deposit", account_number, amount)
        print(f"Deposited {amount} to {account}")

    @staticmethod
    def credit(account_number: str, amount: float) -> None:
        """
                Credits money into an account.

                Args:
                    account_number (str): The account number.
                    amount (float): The amount to credit.
                """
        account = Transactions.get_account(account_number)
        account.credit(amount)
        Account.save_accounts()
        Transactions.log_transaction("credit", account_number, amount)
        print(f"Credited {amount} to {account}")

    @staticmethod
    def statement(account_number: str) -> None:
        """
                Prints the account statement.

                Args:
                    account_number (str): The account number.
                """
        account = Transactions.get_account(account_number)
        print(account)

    @staticmethod
    def transfer(from_account: str, to_account: str, amount: float) -> None:
        """
                Transfers money from one account to another.

                Args:
                    from_account (str): The account number of the sender.
                    to_account (str): The account number of the receiver.
                    amount (float): The amount to transfer.
                """
        from_acc = Transactions.get_account(from_account)
        to_acc = Transactions.get_account(to_account)
        from_acc.debit(amount)
        to_acc.credit(amount)
        Account.save_accounts()
        Transactions.log_transaction("transfer_out", from_account, amount, target_account=to_account)
        Transactions.log_transaction("transfer_in", to_account, amount, target_account=from_account)
        print(f"Transferred {amount} from {from_acc} to {to_acc}")

    @staticmethod
    def view_transactions(account_number: str) -> None:
        """
                Views the transactions of an account.

                Args:
                    account_number (str): The account number.
                """
        transactions = Transactions.load_transactions()
        if account_number in transactions:
            for transaction in transactions[account_number]:
                print(transaction)
        else:
            print("No transactions found for this account.")
