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


@pytest.mark.success
def test_debit(setup_database):
    try:
        account = Account("1001", "John Doe", "IFSC001", "Main Branch",
                          "State1", "District1", "Country1",
                          "savings", 10000.0)
        account.create_account("1001", "John Doe", "IFSC001", "Main Branch",
                               "State1", "District1", "Country1", "savings",
                               10000.0)
        Transaction.debit("1001", 2000.0)
        updated_account = account.load_account(account.account_number)
        assert updated_account.balance == 8000.0
        print("test_debit passed")
    except AssertionError as e:
        print("test_debit failed")
        raise e


@pytest.mark.failure
def test_debit_insufficient_funds(setup_database):
    account = Account("1001", "John Doe", "IFSC001", "Main Branch",
                      "State1", "District1", "Country1",
                      "savings", 10000.0)
    account.create_account("1001", "John Doe", "IFSC001", "Main Branch",
                           "State1", "District1", "Country1", "savings",
                           10000.0)
    with pytest.raises(InsufficientFundsError):
        Transaction.debit(account.account_number, 12000.0)
    print("test_debit_insufficient_funds passed")


@pytest.mark.success
def test_credit(setup_database):
    try:
        account = Account("1001", "John Doe", "IFSC001", "Main Branch",
                          "State1", "District1", "Country1",
                          "savings", 10000.0)
        account.create_account("1001", "John Doe", "IFSC001", "Main Branch",
                               "State1", "District1", "Country1", "savings",
                               10000.0)
        Transaction.credit(account.account_number, 2000.0)
        account = account.load_account(account.account_number)
        assert account.balance == 12000.0
        print("test_credit passed")
    except AssertionError as e:
        print("test_credit failed")
        raise e


@pytest.mark.success
def test_transfer(setup_database):
    try:
        sender = Account("1001", "John Doe", "IFSC001", "Main Branch", "State1", "District1", "Country1",
                         "savings", 10000.0)
        receiver = Account("1003", "Jake Doe", "IFSC003", "Branch3", "State3", "District3", "Country3",
                           "savings", 10000.0)
        sender.create_account("1001", "John Doe", "IFSC001", "Main Branch", "State1", "District1", "Country1",
                              "savings", 10000.0)
        receiver.create_account("1003", "Jake Doe", "IFSC003", "Branch3", "State3", "District3", "Country3",
                                "savings", 10000.0)
        sender.transfer("1003", 2000.0)
        assert sender.balance == 8000.0
        assert receiver.balance == 12000.0
        print("test_transfer passed")
    except AssertionError as e:
        print("test_transfer failed")
        raise e


@pytest.mark.success
def test_view_transactions(setup_database):
    try:
        account = Account.create("1001", "John Doe", "IFSC001", "Main Branch", "State1", "District1", "Country1",
                                 "savings", 10000.0)
        account.credit(1000.0)
        account.debit(500.0)
        transactions = Transaction.get_all(account.account_number)
        assert len(transactions) == 2
        print("test_view_transactions passed")
    except AssertionError as e:
        print("test_view_transactions failed")
        raise e
