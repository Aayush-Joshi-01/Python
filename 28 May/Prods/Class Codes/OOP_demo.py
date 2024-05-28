import random


class SBI:
    """
    Class for a Bank
        Methods include:
        - deposit
        - withdraw
        - check_balance
    """

    def __init__(self, name: str, balance: float, account_type) -> None:
        self._account_number = random.randint(500000, 1000000)
        self._name = name
        self._balance = balance

    def __str__(self) -> str:
        return f"Account of acc. no. {self._account_number} is now opened"

    def __repr__(self) -> str:
        return f"Account of {self._name} is opened and has {self._balance} as initial balance"

    def withdraw(self) -> None:
        amount = float(input("Enter amount to withdraw: "))
        if amount > self._balance:
            print("Insufficient balance!")
        else:
            self._balance -= amount
            print(f"Amount withdrawn: {amount}")

    def deposit(self) -> None:
        amount = float(input("Enter amount to deposit: "))
        self._balance += amount

    def view_balance(self) -> None:
        print(f"Account balance: {self._balance}")


if __name__ == "__main__":
    bank_obj = SBI("Aayush", 5000.0, "savings")
    print(bank_obj.__doc__)
    print(str(bank_obj))
    print(repr(bank_obj))
    while True:
        print("1. Withdraw")
        print("2. Deposit")
        print("3. View balance")
        print("4. Exit")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            bank_obj.withdraw()
        elif choice == 2:
            bank_obj.deposit()
        elif choice == 3:
            bank_obj.view_balance()
        else:
            break
