from transactions import Transactions


class Bank:
    """
            A class that provides a static interface to the `Transactions` class for managing bank accounts.

            Args:
                None
            """

    @staticmethod
    def create_account(account_number: str, name: str, ifsc_code: str, branch_name: str, state: str, district: str,
                       country: str, account_type: str, initial_balance: float = 0) -> None:
        """
                Creates a new bank account.

                Args:
                    account_number (str): The account number.
                    name (str): The account holder's name.
                    ifsc_code (str): The IFSC code of the branch.
                    branch_name (str): The name of the branch.
                    state (str): The state where the branch is located.
                    district (str): The district where the branch is located.
                    country (str): The country where the branch is located.
                    account_type (str): The type of account (savings or zero_balance_savings).
                    initial_balance (float): The initial balance of the account.
                """

        Transactions.create_account(account_number, name, ifsc_code, branch_name, state, district, country, account_type,
                                    initial_balance)

    @staticmethod
    def deposit(account_number: str, amount: float) -> None:
        """
                Deposits money into an existing bank account.

                Args:
                    account_number (str): The account number.
                    amount (float): The amount to deposit.
                """
        Transactions.deposit(account_number, amount)

    @staticmethod
    def credit(account_number: str, amount: float) -> None:
        """
                Credits money into an existing bank account.

                Args:
                    account_number (str): The account number.
                    amount (float): The amount to credit.
                """
        Transactions.credit(account_number, amount)

    @staticmethod
    def statement(account_number: str) -> None:
        """
                Generates a statement for an existing bank account.

                Args:
                    account_number (str): The account number.
                """
        Transactions.statement(account_number)

    @staticmethod
    def transfer(from_account: str, to_account: str, amount: float) -> None:
        """
                Transfers money from one bank account to another.

                Args:
                    from_account (str): The account number to transfer from.
                    to_account (str): The account number to transfer to.
                    amount (float): The amount to transfer.
                """
        Transactions.transfer(from_account, to_account, amount)

    @staticmethod
    def view_transactions(account_number: str) -> None:
        """
                Views the transactions of an existing bank account.

                Args:
                    account_number (str): The account number.
                """
        Transactions.view_transactions(account_number)
