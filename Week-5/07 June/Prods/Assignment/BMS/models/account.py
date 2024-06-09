from db.database import get_db_connection
from exceptions.custom_exceptions import AccountAlreadyExistsError, AccountNotFoundError, InvalidInitialBalanceError


class Account:
    def __init__(self, account_number: str, name: str, ifsc_code: str, branch_name: str, state: str,
                 district: str, country: str, account_type: str, balance: float):
        self.account_number = account_number
        self.name = name
        self.ifsc_code = ifsc_code
        self.branch_name = branch_name
        self.state = state
        self.district = district
        self.country = country
        self.account_type = account_type
        self.balance = balance

    @staticmethod
    def create_account(account_number: str, name: str, ifsc_code: str, branch_name: str, state: str,
                       district: str, country: str, account_type: str, initial_balance: float) -> None:
        if account_type == 'zero_balance_savings' and initial_balance < 2000:
            raise InvalidInitialBalanceError("Initial balance must be at least 2000 for zero balance savings accounts.")
        elif account_type == 'savings' and initial_balance < 5000:
            raise InvalidInitialBalanceError("Initial balance must be at least 5000 for savings accounts.")

        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                # Check if account already exists
                cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
                if cursor.fetchone():
                    raise AccountAlreadyExistsError(account_number)

                # Create account
                cursor.execute("""
                INSERT INTO accounts (account_number, name, ifsc_code, branch_name, state, district, country, account_type, balance)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                account_number, name, ifsc_code, branch_name, state, district, country, account_type, initial_balance))

            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def load_account(account_number: str) -> 'Account':
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
                account_data = cursor.fetchone()
                if not account_data:
                    raise AccountNotFoundError(account_number)

                return Account(
                    account_number=account_data['account_number'],
                    name=account_data['name'],
                    ifsc_code=account_data['ifsc_code'],
                    branch_name=account_data['branch_name'],
                    state=account_data['state'],
                    district=account_data['district'],
                    country=account_data['country'],
                    account_type=account_data['account_type'],
                    balance=account_data['balance']
                )
        finally:
            connection.close()

    def save(self) -> None:
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                UPDATE accounts
                SET name = %s, ifsc_code = %s, branch_name = %s, state = %s, district = %s, country = %s,
                    account_type = %s, balance = %s
                WHERE account_number = %s
                """, (self.name, self.ifsc_code, self.branch_name, self.state, self.district, self.country,
                      self.account_type, self.balance, self.account_number))

            connection.commit()
        finally:
            connection.close()
