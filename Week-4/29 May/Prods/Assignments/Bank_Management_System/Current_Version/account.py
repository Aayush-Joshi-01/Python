import json
from typing import Dict

from exceptions import InvalidInitialBalanceError, InsufficientFundsError


class Account:
    """
    Represents a bank account.

    Attributes:
        account_number (str): The account number.
        name (str): The account holder's name.
        ifsc_code (str): The IFSC code of the branch.
        branch_name (str): The name of the branch.
        state (str): The state where the branch is located.
        district (str): The district where the branch is located.
        country (str): The country where the branch is located.
        account_type (str): The type of account (savings or zero_balance_savings).
        balance (float): The current balance of the account.

    Methods:
        credit(amount: float): Credits the account with the given amount.
        debit(amount: float): Debits the account with the given amount.
    """

    accounts_file = "accounts.json"
    accounts: Dict[str, 'Account'] = {}

    def __init__(self, account_number: str, name: str, ifsc_code: str, branch_name: str, state: str, district: str,
                 country: str, account_type: str, balance: float = 0):
        """
        Initializes an Account object.

        Args:
            account_number (str): The account number.
            name (str): The account holder's name.
            ifsc_code (str): The IFSC code of the branch.
            branch_name (str): The name of the branch.
            state (str): The state where the branch is located.
            district (str): The district where the branch is located.
            country (str): The country where the branch is located.
            account_type (str): The type of account (savings or zero_balance_savings).
            balance (float, optional): The initial balance of the account. Defaults to 0.

        Raises:
            InvalidInitialBalanceError: If the initial balance is less than the minimum required for the account type.
        """
        self.account_number = account_number
        self.name = name
        self.ifsc_code = ifsc_code
        self.branch_name = branch_name
        self.state = state
        self.district = district
        self.country = country
        self.account_type = account_type
        self.balance = balance
        self._validate_initial_balance()

    def _validate_initial_balance(self) -> None:
        """
        Validates the initial balance of the account.

        Raises:
            InvalidInitialBalanceError: If the initial balance is less than the minimum required for the account type.
        """
        if self.account_type == 'savings' and self.balance < 5000:
            raise InvalidInitialBalanceError("Savings accounts must have a minimum balance of 5000.")
        if self.account_type == 'zero_balance_savings' and self.balance < 2000:
            raise InvalidInitialBalanceError(
                "Zero balance savings accounts must have a minimum initial balance of 2000.")
        if self.account_type == 'zero_balance_savings' and self.balance >= 2000:
            self.balance -= 2000

    def credit(self, amount: float) -> None:
        """
        Credits the account with the given amount.

        Args:
            amount (float): The amount to credit.
        """
        self.balance += amount

    def debit(self, amount: float) -> None:
        """
        Debits the account with the given amount.

        Args:
            amount (float): The amount to debit.

        Raises:
            InsufficientFundsError: If the account balance is less than the amount to debit.
        """
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount

    def __str__(self) -> str:
        """
        Returns a string representation of the account.

        Returns:
            str: A string representation of the account.
        """
        return f"Account({self.account_number}, {self.name}, {self.balance}, {self.account_type})"

    @classmethod
    def save_accounts(cls) -> None:
        """
        Saves the accounts to the accounts file.
        """
        with open(cls.accounts_file, 'w') as f:
            accounts_data = {acc_number: acc.__dict__ for acc_number, acc in cls.accounts.items()}
            json.dump(accounts_data, f)
