import json
from typing import Dict


class Account:
    accounts_file = "accounts.json"
    accounts: Dict[str, 'Account'] = {}

    def __init__(self, account_number: str, name: str, ifsc_code: str, branch_name: str, state: str, district: str,
                 country: str, account_type: str, balance: float = 0):
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
        if self.account_type == 'savings' and self.balance < 5000:
            raise InvalidInitialBalanceError("Savings accounts must have a minimum balance of 5000.")
        if self.account_type == 'zero_balance_savings' and self.balance < 2000:
            raise InvalidInitialBalanceError(
                "Zero balance savings accounts must have a minimum initial balance of 2000.")

    def credit(self, amount: float) -> None:
        self.balance += amount

    def debit(self, amount: float) -> None:
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount

    def __str__(self) -> str:
        return f"Account({self.account_number}, {self.name}, {self.balance}, {self.account_type})"

    @classmethod
    def load_accounts(cls) -> None:
        try:
            with open(cls.accounts_file, 'r') as f:
                accounts_data = json.load(f)
                cls.accounts = {acc_number: cls(**data) for acc_number, data in accounts_data.items()}
        except FileNotFoundError:
            cls.accounts = {}

    @classmethod
    def save_accounts(cls) -> None:
        with open(cls.accounts_file, 'w') as f:
            accounts_data = {acc_number: acc.__dict__ for acc_number, acc in cls.accounts.items()}
            json.dump(accounts_data, f)
