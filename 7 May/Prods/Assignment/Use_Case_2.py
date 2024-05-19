# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.
def get_quantity():
    purchased_amount = int(input("Enter the total amount: "))
    return get_discount(purchased_amount)

def get_discount(purchased_amount):
    if purchased_amount > 1000:
        return final_cost(purchased_amount, 10)
    else:
        return final_cost(purchased_amount, 0)

def final_cost(purchased_amount, discount):
    return purchased_amount * (100 - discount)//100


if __name__ == '__main__':
    print(get_quantity())