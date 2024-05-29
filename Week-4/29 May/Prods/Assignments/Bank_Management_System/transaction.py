import json


class Transaction:
    transactions_file = "transactions.json"

    @staticmethod
    def load_transactions():
        try:
            with open(Transaction.transactions_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    @staticmethod
    def view_transactions(account_number):
        transactions = Transaction.load_transactions()
        if account_number in transactions:
            return transactions[account_number]
        else:
            raise Exception("No transactions found for this account")
