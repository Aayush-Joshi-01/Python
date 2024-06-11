import pytest

from db.database import get_db_connection, initialize_db
from exceptions.custom_exceptions import InsufficientFundsError
from models.account import Account
from models.transaction import Transaction


@pytest.fixture(scope="module")
def setup_database():
    initialize_db()
    yield
    connection = get_db_connection()
    connection.close()


@pytest.fixture(autouse=True)
def setup_teardown():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM transactions")
        cursor.execute("DELETE FROM accounts")
        cursor.execute("DELETE FROM logs")
        connection.commit()
    yield


@pytest.mark.success
def test_create_account(setup_database):
    try:
        account = Account("1002", "Jane Doe", "IFSC002", "Branch2",
                          "State2", "District2", "Country2", "savings",
                          10000.0)
        account.create_account("1002", "Jane Doe", "IFSC002", "Branch2",
                               "State2", "District2", "Country2", "savings",
                               10000.0)
        assert account is not None
        assert account.account_number == "1002"
        assert account.balance == 10000.0
        print("test_create_account passed")
    except AssertionError as e:
        print("test_create_account failed")
        raise e


@pytest.mark.success
def test_get_account(setup_database):
    try:
        Account.create_account("1001", "John Doe", "IFSC001", "Main Branch",
                               "State1", "District1", "Country1",
                               "savings", 10000.0)
        fetched_account = Account.load_account("1001")
        assert fetched_account is not None
        assert fetched_account.name == "John Doe"
        print("test_get_account passed")
    except AssertionError as e:
        print("test_get_account failed")
        raise e
