class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("The amount must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")


def main():
    print("Welcome to the Simple Banking System!")
    initial_balance = 0.0

    while True:
        try:
            initial_balance = float(input("Please enter your initial balance: "))
            if initial_balance < 0:
                raise ValueError("Initial balance cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    account = BankAccount(initial_balance)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            amount = get_positive_number("Enter the amount to deposit: ")
            try:
                new_balance = account.deposit(amount)
                print(f"Successfully deposited. New balance: {new_balance:.2f}")
            except ValueError as e:
                print(e)
        elif choice == '2':
            amount = get_positive_number("Enter the amount to withdraw: ")
            try:
                new_balance = account.withdraw(amount)
                print(f"Successfully withdrawn. New balance: {new_balance:.2f}")
            except ValueError as e:
                print(e)
        elif choice == '3':
            current_balance = account.check_balance()
            print(f"Your current balance is: {current_balance:.2f}")
        elif choice == '4':
            print("Exiting the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
