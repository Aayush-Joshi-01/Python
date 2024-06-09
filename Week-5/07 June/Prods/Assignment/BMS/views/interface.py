from routes.url import route


def main() -> None:
    while True:
        print(
            "1: Create Account\n2: Deposit\n3: Debit\n4: Credit\n5: Get Account Details\n6: Transfer\n7: View "
            "Transactions\n8: Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            account_number = input("Enter new account number: ")
            name = input("Enter name: ")
            ifsc_code = input("Enter IFSC code: ")
            branch_name = input("Enter branch name: ")
            state = input("Enter state: ")
            district = input("Enter district: ")
            country = input("Enter country: ")
            account_type = input("Enter account type (savings/zero_balance_savings): ")
            initial_balance = float(input("Enter initial balance: "))
            try:
                route("create_account", account_number, name, ifsc_code, branch_name, state, district, country,
                      account_type, initial_balance)
            except Exception as e:
                print(e)

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount: "))
            try:
                route("deposit", account_number, amount)
            except Exception as e:
                print(e)

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount: "))
            try:
                route("debit", account_number, amount)
            except Exception as e:
                print(e)

        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount: "))
            try:
                route("credit", account_number, amount)
            except Exception as e:
                print(e)

        elif choice == "5":
            account_number = input("Enter account number: ")
            try:
                route("get_account_details", account_number)
            except Exception as e:
                print(e)

        elif choice == "6":
            from_account = input("Enter from account number: ")
            to_account = input("Enter to account number: ")
            amount = float(input("Enter amount: "))
            try:
                route("transfer", from_account, to_account, amount)
            except Exception as e:
                print(e)

        elif choice == "7":
            account_number = input("Enter account number: ")
            try:
                route("view_transactions", account_number)
            except Exception as e:
                print(e)

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
