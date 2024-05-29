from account import Account


class Bank:
    accounts = {}

    def __init__(self) -> None:
        pass

    @staticmethod
    def add_account(account_number):
        if account_number in Bank.accounts:
            raise Exception(f"Account {account_number} already exists.")
        Bank.accounts[account_number] = Account(account_number)
        return Bank.accounts[account_number]

    @staticmethod
    def find_account(account_number):
        if account_number not in Bank.accounts:
            raise Exception(f"Account {account_number} not found.")
        return Bank.accounts[account_number]

    @staticmethod
    def deposit(account_number, amount):
        account = Bank.find_account(account_number)
        account.credit(amount)
        print(f"Deposited {amount} into account {account_number}.")

    @staticmethod
    def withdraw(account_number, amount):
        account = Bank.find_account(account_number)
        account.debit(amount)
        print(f"Withdrawn {amount} from account {account_number}.")

    @staticmethod
    def statement(account_number):
        account = Bank.find_account(account_number)
        print(f"Statement for account {account}:")
