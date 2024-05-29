class Account:
    def __init__(self, account_number, balance=0) -> None:
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def __str__(self):
        return f"Account {self.account_number}, Balance: {self.balance}"
