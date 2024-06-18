from ..db.database import get_db_connection
from ..decorators.generate_logs import logger_v
from ..exceptions.custom_exceptions import InvalidInitialBalanceError, \
    AccountAlreadyExistsError, AccountNotFoundError


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
    @logger_v
    def create_account(account_number: str, name: str, ifsc_code: str, branch_name: str, state: str,
                       district: str, country: str, account_type: str, initial_balance: float) -> None:
        if account_type == 'zero_balance_savings' and initial_balance < 2000:
            raise InvalidInitialBalanceError("Initial balance must be at least 2000 for zero balance savings accounts.")
        elif account_type == 'savings' and initial_balance < 7000:
            raise InvalidInitialBalanceError("Initial balance must be at least 7000 for savings accounts.")
        elif account_type == 'zero_balance_savings' and initial_balance >= 2000:
            initial_balance -= 2000

        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                # Check if account already exists
                cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
                if cursor.fetchone():
                    raise AccountAlreadyExistsError(account_number)

                # create new account
                cursor.execute("""
                INSERT INTO accounts 
                (account_number, name, ifsc_code, branch_name, state, district, country, account_type, balance)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    account_number, name, ifsc_code, branch_name, state, district, country, account_type,
                    initial_balance))
                print(f"Account {account_number} created with initial balance {initial_balance}")
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    @logger_v
    def load_account(account_number: str) -> 'Account':
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
                account_data = cursor.fetchone()
                if not account_data:
                    raise AccountNotFoundError(account_number)
                # returns Account object
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

    @logger_v
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

    @staticmethod
    @logger_v
    def exists(account_number: str) -> bool:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT 1 FROM accounts WHERE account_number = %s"
        cursor.execute(query, (account_number,))
        result = cursor.fetchone()
        connection.close()
        return result is not None

    def __str__(self) -> str:
        return (f"Account(account_number={self.account_number}, name={self.name}, ifsc_code={self.ifsc_code}, "
                f"branch_name={self.branch_name}, state={self.state}, district={self.district}, "
                f"country={self.country}, account_type={self.account_type}, balance={self.balance})")
