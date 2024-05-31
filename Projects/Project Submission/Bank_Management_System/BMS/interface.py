import sys

from routes import urls
from utility.decorators import login_banking_system


class BankingSystem:
    """
            A banking system that allows users to create accounts, deposit/credit money,
            view statements, transfer money, and view transactions.
            """

    @staticmethod
    @login_banking_system
    def main() -> None:
        """
        The main function that runs the banking system.
        """
        while True:
            print("************************************************************************************************\n")
            print("Create Account - create_account/ \nDeposit - deposit/ \nCredit - credit/ \nStatement - "
                  "statement/\nTransfer - transfer/\nView Transactions - view_transactions/\nExit - 0/\n")
            print("************************************************************************************************\n")
            choice = input("Enter choice: ")
            try:
                if choice == "create_account":
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
                        urls.route("create_account", account_number, name, ifsc_code, branch_name, state,
                                   district, country, account_type, initial_balance)
                    except Exception as e:
                        print(e)

                elif choice == "deposit":
                    account_number = input("Enter account number: ")
                    amount = float(input("Enter amount: "))
                    try:
                        urls.route("deposit", account_number, amount)
                    except Exception as e:
                        print(e)

                elif choice == "credit":
                    account_number = input("Enter account number: ")
                    amount = float(input("Enter amount: "))
                    try:
                        urls.route("credit", account_number, amount)
                    except Exception as e:
                        print(e)

                elif choice == "statement":
                    account_number = input("Enter account number: ")
                    try:
                        urls.route("statement", account_number)
                    except Exception as e:
                        print(e)

                elif choice == "transfer":
                    from_account = input("Enter from account number: ")
                    to_account = input("Enter to account number: ")
                    amount = float(input("Enter amount: "))
                    try:
                        urls.route("transfer", from_account, to_account, amount)
                    except Exception as e:
                        print(e)

                elif choice == "view_transactions":
                    account_number = input("Enter account number: ")
                    try:
                        urls.route("view_transactions", account_number)
                    except Exception as e:
                        print(e)

                elif choice == "0":
                    print("Exiting...")
                    sys.exit(0)

                else:
                    urls.route(choice)
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.main()
