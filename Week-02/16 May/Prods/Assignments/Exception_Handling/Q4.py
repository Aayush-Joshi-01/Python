class AccountNotFoundException(Exception):
    pass


class InsufficientBalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceException(f"Account {self.account_number} has insufficient balance.")
        self.balance -= amount

    def __str__(self):
        return f"Account {self.account_number}, Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def find_account(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundException(f"Account {account_number} not found.")
        return self.accounts[account_number]

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"Transferred {amount} from Account {from_account_number} to Account {to_account_number}.")


def main():
    bank = Bank()

    # Adding accounts to the bank
    bank.add_account(BankAccount('123', 500))
    bank.add_account(BankAccount('456', 300))
    bank.add_account(BankAccount('789', 1000))

    print("Initial Account Balances:")
    for account in bank.accounts.values():
        print(account)

    try:
        bank.transfer('123', '456', 200)
        bank.transfer('456', '789', 50)
        bank.transfer('123', '999', 100)
    except AccountNotFoundException as e:
        print(e)
    except InsufficientBalanceException as e:
        print(e)

    print("\nFinal Account Balances:")
    for account in bank.accounts.values():
        print(account)


if __name__ == "__main__":
    main()
