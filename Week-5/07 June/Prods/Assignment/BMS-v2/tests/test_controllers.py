import pytest
from controllers.bank_controller import BankController
from controllers.transaction_controller import TransactionController
from db.database import get_db_connection, initialize_db
from exceptions.custom_exceptions import InsufficientFundsError


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
        cursor.execute("DELETE FROM accounts")
        cursor.execute("DELETE FROM transactions")
        connection.commit()
    yield


@pytest.mark.success
def test_create_account_controller(setup_database):
    try:
        BankController.create_account("1002", "Jane Doe", "IFSC002",
                                      "Branch2", "State2", "District2", "Country2",
                                      "savings", 5000.0)
        account = BankController.get_account_details("1002")
        assert account is not None
        assert account["account_number"] == "1002"
        assert account["balance"] == 5000.0
        print("test_create_account_controller passed")
    except AssertionError as e:
        print("test_create_account_controller failed")
        raise e


@pytest.mark.success
def test_debit_controller(setup_database):
    try:
        BankController.create_account("1001", "John Doe", "IFSC001",
                                      "Main Branch", "State1", "District1", "Country1",
                                      "savings", 10000.0)
        TransactionController.debit("1001", 2000.0)
        account = BankController.get_account_details("1001")
        assert account["balance"] == 8000.0
        print("test_debit_controller passed")
    except AssertionError as e:
        print("test_debit_controller failed")
        raise e


@pytest.mark.failure
def test_debit_insufficient_funds_controller(setup_database):
    BankController.create_account("1001", "John Doe", "IFSC001",
                                  "Main Branch", "State1", "District1", "Country1",
                                  "savings", 10000.0)
    with pytest.raises(InsufficientFundsError):
        TransactionController.debit("1001", 12000.0)
    print("test_debit_insufficient_funds_controller passed")


@pytest.mark.success
def test_credit_controller(setup_database):
    try:
        BankController.create_account("1001", "John Doe", "IFSC001",
                                      "Main Branch", "State1", "District1", "Country1",
                                      "savings", 10000.0)
        TransactionController.credit("1001", 2000.0)
        account = BankController.get_account_details("1001")
        assert account["balance"] == 12000.0
        print("test_credit_controller passed")
    except AssertionError as e:
        print("test_credit_controller failed")
        raise e


@pytest.mark.success
def test_transfer_controller(setup_database):
    try:
        BankController.create_account("1001", "John Doe", "IFSC001",
                                      "Main Branch", "State1", "District1", "Country1",
                                      "savings", 10000.0)
        BankController.create_account("1003", "Jake Doe", "IFSC003",
                                      "Branch3", "State3", "District3", "Country3",
                                      "savings", 5000.0)
        TransactionController.transfer("1001", "1003", 2000.0)
        sender = BankController.get_account_details("1001")
        receiver = BankController.get_account_details("1003")
        assert sender["balance"] == 8000.0
        assert receiver["balance"] == 7000.0
        print("test_transfer_controller passed")
    except AssertionError as e:
        print("test_transfer_controller failed")
        raise e


@pytest.mark.success
def test_view_transactions_controller(setup_database):
    try:
        BankController.create_account("1001", "John Doe", "IFSC001",
                                      "Main Branch", "State1", "District1", "Country1",
                                      "savings", 10000.0)
        TransactionController.credit("1001", 1000.0)
        TransactionController.debit("1001", 500.0)
        transactions = BankController.view_transactions("1001")
        assert len(transactions) == 2
        print("test_view_transactions_controller passed")
    except AssertionError as e:
        print("test_view_transactions_controller failed")
        raise e
