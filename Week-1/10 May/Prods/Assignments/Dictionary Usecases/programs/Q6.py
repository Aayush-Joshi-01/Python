def deposit(customer_id, amount, customer_accounts):
    if customer_id in customer_accounts:
        customer_accounts[customer_id]['balance'] += amount
        transaction = {'type': 'deposit', 'amount': amount}
        customer_accounts[customer_id]['transaction_history'].append(transaction)
        print(f"{amount} deposited successfully into the account of customer with ID {customer_id}.")
    else:
        print(f"Customer with ID {customer_id} not found.")


def withdraw(customer_id, amount, customer_accounts):
    if customer_id in customer_accounts:
        if amount <= customer_accounts[customer_id]['balance']:
            customer_accounts[customer_id]['balance'] -= amount
            transaction = {'type': 'withdrawal', 'amount': amount}
            customer_accounts[customer_id]['transaction_history'].append(transaction)
            print(f"{amount} withdrawn successfully from the account of customer with ID {customer_id}.")
        else:
            print(f"Insufficient balance in the account of customer with ID {customer_id}.")
    else:
        print(f"Customer with ID {customer_id} not found.")


if __name__ == '__main__':
    customer_accounts = {
        1001: {'balance': 5000, 'transaction_history': []},
        1002: {'balance': 10000, 'transaction_history': []},
        1003: {'balance': 7500, 'transaction_history': []}
    }
    deposit(1001, 2000, customer_accounts)
    withdraw(1002, 500, customer_accounts)
    withdraw(1003, 10000, customer_accounts)
    print(customer_accounts)