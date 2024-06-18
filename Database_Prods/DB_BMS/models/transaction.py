from ..db.database import get_db_connection
from ..decorators.generate_logs import logger_v
from ..exceptions.custom_exceptions import AccountNotFoundError, InsufficientFundsError


class Transaction:
    def __init__(self, account_number: str, transaction_type: str, amount: float, target_account: str = None):
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.target_account = target_account

    @staticmethod
    @logger_v
    def deposit(account_number: str, amount: float) -> None:
        """
        Deposits the specified amount into the account.

        :param account_number: The account number.
        :param amount: The amount to deposit.
        """
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s",
                               (amount, account_number))
                cursor.execute("INSERT INTO transactions (account_number, type, amount) VALUES (%s, 'deposit', %s)",
                               (account_number, amount))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    @logger_v
    def debit(account_number: str, amount: float) -> None:
        """
        Debits the specified amount from the account.

        :param account_number: The account number.
        :param amount: The amount to debit.
        """
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
                row = cursor.fetchone()
                if row is None:
                    raise AccountNotFoundError("Account not found")
                balance = row['balance']
                if balance < amount:
                    raise InsufficientFundsError("Insufficient funds")
                cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s",
                               (amount, account_number))
                cursor.execute("INSERT INTO transactions (account_number, type, amount) VALUES (%s, 'debit', %s)",
                               (account_number, float(amount)))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    @logger_v
    def credit(account_number: str, amount: float) -> None:
        """
        Credits the specified amount from the account.

        :param account_number: The account number.
        :param amount: The amount to credit.
        """
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s",
                               (amount, account_number))
                cursor.execute("INSERT INTO transactions (account_number, type, amount) VALUES (%s, 'credit', %s)",
                               (account_number, amount))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    @logger_v
    def transfer(from_account: str, to_account: str, amount: float) -> None:
        """
        Transfers the specified amount from one account to another.

        :param from_account: The account number to transfer from.
        :param to_account: The account number to transfer to.
        :param amount: The amount to transfer.
        """
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (from_account,))
                balance = cursor.fetchone()['balance']
                if balance < amount:
                    raise InsufficientFundsError("Insufficient funds")
                cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s",
                               (amount, from_account))
                cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s",
                               (amount, to_account))
                cursor.execute(
                    "INSERT INTO transactions (account_number, type, amount, target_account) VALUES (%s, 'transfer', "
                    "%s, %s)",
                    (from_account, amount, to_account))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    @logger_v
    def get_all(account_number):
        """
        Fetches all transactions related to a specific account number.

        :param account_number: The account number.
        :return: A list of transactions.

        """
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM transactions WHERE account_number = %s ORDER BY timestamp DESC",
                               (account_number,))
                return cursor.fetchall()
        finally:
            connection.close()
