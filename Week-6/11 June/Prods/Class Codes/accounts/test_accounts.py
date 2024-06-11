import pytest
from accounts_ops import accounts, create_account, update_account, deposit, withdraw


@pytest.mark.account
def test_create_account():
    create_account("1234", "John Doe", 1000, "Savings")
    assert accounts["1234"] == {"name": "John Doe", "balance": 1000, "account_type": "Savings"}


@pytest.mark.account
def test_update_account():
    create_account("1234", "John Doe", 1000, "Savings")
    update_account("1234", "Jane Doe", 2000, "Checking")
    assert accounts["1234"] == {"name": "Jane Doe", "balance": 2000, "account_type": "Checking"}


@pytest.mark.transaction
def test_deposit():
    create_account("1234", "John Doe", 1000, "Savings")
    deposit("1234", 500)
    assert accounts["1234"]["balance"] == 1500


@pytest.mark.transaction
def test_withdraw():
    create_account("1234", "John Doe", 1000, "Savings")
    withdraw("1234", 500)
    assert accounts["1234"]["balance"] == 500


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-m", "account_creation or account_update or transaction"])
