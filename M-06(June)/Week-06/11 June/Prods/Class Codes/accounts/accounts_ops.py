accounts = {}


def create_account(account_number, name, balance, account_type):
    accounts[account_number] = {'name': name, 'balance': balance, 'account_type': account_type}
    print("Account created")


def update_account(account_number, name, balance, account_type):
    accounts[account_number] = {'name': name, 'balance': balance, 'account_type': account_type}
    print(f"Account {account_number} updated")


def deposit(account_number, amount):
    accounts[account_number]['balance'] += amount


def withdraw(account_number, amount):
    accounts[account_number]['balance'] -= amount


def create_account_ops():
    account_number = input("Enter account number: ")
    name = input("Enter name: ")
    balance = input("Enter balance: ")
    account_type = input("Enter account type: ")
    create_account(account_number, name, balance, account_type)


def update_account_ops(account_number):
    name = input("Enter name: ")
    balance = input("Enter balance: ")
    account_type = input("Enter account type: ")
    accounts[account_number] = {'name': name, 'balance': balance, 'account_type': account_type}


def deposit_ops(account_number):
    amount = input("Enter amount: ")
    deposit(account_number, amount)


def withdraw_ops(account_number):
    amount = input("Enter amount: ")
    withdraw(account_number, amount)


def main():
    while True:
        print("1. Create account")
        print("2. Update account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            create_account_ops()
        elif choice == "2":
            account_number = input("Enter account number: ")
            update_account_ops(account_number)
        elif choice == "3":
            account_number = input("Enter account number: ")
            deposit_ops(account_number)
        elif choice == "4":
            account_number = input("Enter account number: ")
            withdraw_ops(account_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
