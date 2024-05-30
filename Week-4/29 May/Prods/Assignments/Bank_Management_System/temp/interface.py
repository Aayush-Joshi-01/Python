import sys

from Bank_Utility.bank import Bank


class BankingSystem:
    """
            A banking system that allows users to create accounts, deposit/credit money,
            view statements, transfer money, and view transactions.
            """

    def __init__(self):
        self.bank = Bank()

    def main(self) -> None:
        """
        The main function that runs the banking system.
        """
        while True:
            print("1: Create Account\n2: Deposit\n3: Credit\n4: Statement\n5: Transfer\n6: View Transactions\n7: Exit")
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
                    self.bank.create_account(account_number, name, ifsc_code, branch_name, state, district, country,
                                             account_type, initial_balance)
                except Exception as e:
                    print(e)

            elif choice == "2":
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount: "))
                try:
                    self.bank.deposit(account_number, amount)
                except Exception as e:
                    print(e)

            elif choice == "3":
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount: "))
                try:
                    self.bank.credit(account_number, amount)
                except Exception as e:
                    print(e)

            elif choice == "4":
                account_number = input("Enter account number: ")
                try:
                    self.bank.statement(account_number)
                except Exception as e:
                    print(e)

            elif choice == "5":
                from_account = input("Enter from account number: ")
                to_account = input("Enter to account number: ")
                amount = float(input("Enter amount: "))
                try:
                    self.bank.transfer(from_account, to_account, amount)
                except Exception as e:
                    print(e)

            elif choice == "6":
                account_number = input("Enter account number: ")
                try:
                    self.bank.view_transactions(account_number)
                except Exception as e:
                    print(e)

            elif choice == "7":
                print("Exiting...")
                sys.exit(0)

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.main()
