import pytest

from ..controllers.bank_controller import BankController
from ..controllers.transaction_controller import TransactionController
from ..db.database import initialize_db, get_db_connection
from ..exceptions.custom_exceptions import InsufficientFundsError, AccountNotFoundError


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
def test_create_account_controller(setup_database):
    BankController.create_account("1002", "Jane Doe", "IFSC002",
                                  "Branch2", "State2", "District2", "Country2",
                                  "savings", 9000.0)
    account = BankController.get_account_details("1002")
    assert account is not None
    assert account.account_number == "1002"
    assert account.balance == 9000.0


@pytest.mark.success
def test_debit_controller(setup_database):
    BankController.create_account("1001", "John Doe", "IFSC001",
                                  "Main Branch", "State1", "District1", "Country1",
                                  "savings", 10000.0)
    TransactionController.debit("1001", 2000.0)
    account = BankController.get_account_details("1001")
    assert account.balance == 8000.0


@pytest.mark.failure
def test_debit_insufficient_funds_controller(setup_database):
    BankController.create_account("1003", "John Doe", "IFSC001",
                                  "Main Branch", "State1", "District1", "Country1",
                                  "savings", 10000.0)
    with pytest.raises(InsufficientFundsError):
        TransactionController.debit("1003", 12000.0)


@pytest.mark.success
def test_credit_controller(setup_database):
    BankController.create_account("1004", "John Doe", "IFSC001",
                                  "Main Branch", "State1", "District1", "Country1",
                                  "savings", 10000.0)
    TransactionController.credit("1004", 2000.0)
    account = BankController.get_account_details("1004")
    assert account.balance == 8000.0


@pytest.mark.success
def test_transfer_controller(setup_database):
    BankController.create_account("1007", "John Doe", "IFSC001",
                                  "Main Branch", "State1", "District1", "Country1",
                                  "savings", 10000.0)
    BankController.create_account("1008", "Jake Doe", "IFSC003",
                                  "Branch3", "State3", "District3", "Country3",
                                  "savings", 7000.0)
    BankController.transfer("1007", "1008", 2000.0)
    sender = BankController.get_account_details("1007")
    receiver = BankController.get_account_details("1008")
    assert sender.balance == 8000.0
    assert receiver.balance == 9000.0


@pytest.mark.failure
def test_transfer_insufficient_funds_controller(setup_database):
    BankController.create_account("1009", "John Doe", "IFSC001",
                                  "Main Branch", "State1", "District1", "Country1",
                                  "savings", 10000.0)
    BankController.create_account("1010", "Jake Doe", "IFSC003",
                                  "Branch3", "State3", "District3", "Country3",
                                  "savings", 9000.0)
    with pytest.raises(InsufficientFundsError):
        BankController.transfer("1009", "1010", 15000.0)


@pytest.mark.failure
def test_transfer_account_not_found_controller(setup_database):
    BankController.create_account("1011", "John Doe", "IFSC001",
                                  "Main Branch", "State1", "District1", "Country1",
                                  "savings", 10000.0)
    with pytest.raises(AccountNotFoundError):
        BankController.transfer("1011", "101010", 2000.0)


@pytest.mark.success
def test_view_transactions_controller(setup_database):
    BankController.create_account("1012", "John Doe", "IFSC001",
                                  "Main Branch", "State1", "District1", "Country1",
                                  "savings", 10000.0)
    BankController.deposit("1012", 1000.0)
    BankController.debit("1012", 500.0)
    transactions = BankController.view_transactions("1012")
    assert len(transactions) == 3
    assert transactions[0]['type'] == 'debit'
    assert transactions[0]['amount'] == 500.0


@pytest.mark.failure
def test_view_transactions_account_not_found_controller(setup_database):
    with pytest.raises(AccountNotFoundError):
        BankController.view_transactions("5")
