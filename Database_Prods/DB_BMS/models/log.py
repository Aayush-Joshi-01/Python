from typing import Any

from ..db.database import get_db_connection
from ..decorators.generate_logs import logger_v


class Log:
    def __init__(self, action: str, account_number: str, amount: float, target_account: str = None, error: str = None):
        self.action = action
        self.account_number = account_number
        self.amount = amount
        self.target_account = target_account
        self.error = error

    @staticmethod
    @logger_v
    def log_action(action: str, account_number: str = None, amount: float = None, target_account: str = None,
                   error: str = None) -> None:
        """
        Logs an action to the logs table.
        """
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                INSERT INTO logs (action, account_number, amount, target_account, error)
                VALUES (%s, %s, %s, %s, %s)
                """, (action, account_number, amount, target_account, error))
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def fetch_logs() -> tuple[tuple[Any, ...], ...]:
        """
        Fetches all logs related to a specific account number.
        """
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM logs ORDER BY timestamp DESC")
                return cursor.fetchall()
        finally:
            connection.close()
