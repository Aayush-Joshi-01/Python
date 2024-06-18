from ..decorators.generate_logs import log_nested_calls
from ..exceptions.custom_exceptions import InsufficientFundsError, AccountNotFoundError, \
    AccountAlreadyExistsError, InvalidInitialBalanceError
from ..models.account import Account
from ..models.log import Log
from ..models.transaction import Transaction


class BankController:
    @staticmethod
    @log_nested_calls
    def create_account(account_number: str, name: str, ifsc_code: str, branch_name: str, state: str,
                       district: str, country: str, account_type: str, initial_balance: float) -> None:
        """
        Creates a new account with the provided details.

        :param account_number: The account number.
        :param name: The name of the account holder.
        :param ifsc_code: The IFSC code of the bank branch.
        :param branch_name: The name of the bank branch.
        :param state: The state where the bank branch is located.
        :param district: The district where the bank branch is located.
        :param country: The country where the bank branch is located.
        :param account_type: The type of account (e.g., savings, zero_balance_savings).
        :param initial_balance: The initial balance to be deposited.
        """
        try:
            Account.create_account(account_number, name, ifsc_code, branch_name, state, district, country,
                                   account_type, initial_balance)
            Log.log_action('create_account', account_number, initial_balance)
        except (AccountAlreadyExistsError, InvalidInitialBalanceError) as e:
            print(e)
            raise e

    @staticmethod
    @log_nested_calls
    def get_account_details(account_number: str) -> Account:
        """
        Retrieves the account details for the specified account number.

        :param account_number: The account number.
        :return: Account object containing account details.
        """
        try:
            return Account.load_account(account_number)
        except AccountNotFoundError as e:
            print(e)
            raise e

    @staticmethod
    @log_nested_calls
    def deposit(account_number: str, amount: float) -> None:
        """
        Deposits the specified amount into the account.

        :param account_number: The account number.
        :param amount: The amount to deposit.
        """
        try:
            Transaction.deposit(account_number, amount)
            Log.log_action('deposit', account_number, amount)
        except AccountNotFoundError as e:
            print(e)
            raise e

    @staticmethod
    @log_nested_calls
    def debit(account_number: str, amount: float) -> None:
        """
        Debits the specified amount from the account.

        :param account_number: The account number.
        :param amount: The amount to debit.
        """
        try:
            Transaction.debit(account_number, amount)
            Log.log_action('debit', account_number, amount)
        except AccountNotFoundError as e:
            print(e)
            raise e

    @staticmethod
    @log_nested_calls
    def credit(account_number: str, amount: float) -> None:
        """
        Credits the specified amount into the account.

        :param account_number: The account number.
        :param amount: The amount to credit.
        """
        try:
            Transaction.credit(account_number, amount)
            Log.log_action('credit', account_number, amount)
        except AccountNotFoundError as e:
            print(e)
            raise e

    @staticmethod
    @log_nested_calls
    def transfer(from_account: str, to_account: str, amount: float) -> None:
        """
        Transfers amount from one account to another.

        :param from_account: The account number to transfer from.
        :param to_account: The account number to transfer to.
        :param amount: The amount to transfer.
        """
        if not Account.exists(from_account):
            raise AccountNotFoundError
        if not Account.exists(to_account):
            raise AccountNotFoundError

        try:
            Transaction.transfer(from_account, to_account, amount)
            Log.log_action('transfer', from_account, amount, target_account=to_account)
        except InsufficientFundsError as e:
            print(e)
            raise e

    @staticmethod
    @log_nested_calls
    def view_transactions(account_number: str):
        """
        View all transactions for the specified account number.

        :param account_number: The account number.
        """
        try:
            return Log.fetch_logs(account_number)
        except AccountNotFoundError as e:
            raise e
