from ..exceptions.custom_exceptions import AccountNotFoundError, InsufficientFundsError
from ..models.transaction import Transaction
from ..decorators.generate_logs import logger_v


class TransactionController:
    @staticmethod
    def deposit(account_number: str, amount: float) -> None:
        """
        Deposits the specified amount into the account.

        :param account_number: The account number.
        :param amount: The amount to deposit.
        """
        try:
            Transaction.deposit(account_number, amount)
        except AccountNotFoundError as e:
            print(e)
            raise e

    @staticmethod
    def debit(account_number: str, amount: float) -> None:
        """
        Debits the specified amount from the account.

        :param account_number: The account number.
        :param amount: The amount to debit.
        """
        try:
            Transaction.debit(account_number, amount)
        except (AccountNotFoundError, InsufficientFundsError) as e:
            print(e)
            raise e

    @staticmethod
    def credit(account_number: str, amount: float) -> None:
        """
        Credits the specified amount into the account.

        :param account_number: The account number.
        :param amount: The amount to credit.
        """
        try:
            Transaction.credit(account_number, amount)
        except AccountNotFoundError as e:
            print(e)
            raise e

    @staticmethod
    def transfer(from_account: str, to_account: str, amount: float) -> None:
        """
        Transfers the specified amount from one account to another.

        :param from_account: The account number to transfer from.
        :param to_account: The account number to transfer to.
        :param amount: The amount to transfer.
        """
        try:
            Transaction.transfer(from_account, to_account, amount)
        except (AccountNotFoundError, InsufficientFundsError) as e:
            print(e)
            raise e
