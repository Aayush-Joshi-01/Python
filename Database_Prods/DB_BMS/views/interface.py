from Database_Prods.DB_BMS.decorators.login_decorator import login_banking_system
from Database_Prods.DB_BMS.decorators.generate_logs import logger_v
from Database_Prods.DB_BMS.routes.url import route


@login_banking_system
@logger_v
def main() -> None:
    try:
        while True:
            print(
                "1: Create Account\n2: Deposit\n3: Debit\n4: Credit\n5: Get Account Details\n6: Transfer\n7: View "
                "Transactions\n8: Get Logs\n9: Exit")
            choice: str = input("Enter choice: ")

            if choice == "1":
                account_number: str = input("Enter new account number: ")
                name: str = input("Enter name: ")
                ifsc_code: str = input("Enter IFSC code: ")
                branch_name: str = input("Enter branch name: ")
                state: str = input("Enter state: ")
                district: str = input("Enter district: ")
                country: str = input("Enter country: ")
                account_type: str = input("Enter account type (savings/zero_balance_savings): ")
                initial_balance: float = float(input("Enter initial balance: "))
                try:
                    route("create_account", account_number, name, ifsc_code, branch_name, state, district,
                          country, account_type, initial_balance)
                except Exception as e:
                    print(e)

            elif choice == "2":
                account_number: str = input("Enter account number: ")
                amount: float = float(input("Enter amount: "))
                try:
                    route("deposit", account_number, amount)
                except Exception as e:
                    print(e)

            elif choice == "3":
                account_number: str = input("Enter account number: ")
                amount: float = float(input("Enter amount: "))
                try:
                    route("debit", account_number, amount)
                except Exception as e:
                    print(e)

            elif choice == "4":
                account_number: str = input("Enter account number: ")
                amount: float = float(input("Enter amount: "))
                try:
                    route("credit", account_number, amount)
                except Exception as e:
                    print(e)

            elif choice == "5":
                account_number: str = input("Enter account number: ")
                try:
                    print(route("get_account_details", account_number))
                except Exception as e:
                    print(e)

            elif choice == "6":
                from_account: str = input("Enter from account number: ")
                to_account: str = input("Enter to account number: ")
                amount: float = float(input("Enter amount: "))
                try:
                    route("transfer", from_account, to_account, amount)
                except Exception as e:
                    print(e)

            elif choice == "7":
                account_number: str = input("Enter account number: ")
                try:
                    transactions = route("view_transactions", account_number)
                    for transaction in transactions:
                        print(transaction)

                except Exception as e:
                    print(e)

            elif choice == "8":
                logs = route("get_logs",)
                for log in logs:
                    print(log)

            elif choice == "9":
                print("Exiting...")
                break

            else:
                print("404 Error : Not Found")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
