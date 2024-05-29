from bank import Bank


class Transactions:
    def __init__(self) -> None:
        pass

    @staticmethod
    def transfer(from_account, to_account, amount):
        from_account = Bank.find_account(from_account)
        to_account = Bank.find_account(to_account)
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(
            f"Transferred {amount} from Account {from_account.account_number} to Account {to_account.account_number}.")
