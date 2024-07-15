# Write a program to Calculator the electricity bill( accept number of units user) according to the following criteria:
#
# unit:                     price:
# First 100 units.    No Charge.
# Next 100 units.     Rs 5 per unit.
# After 200 units.    Rs 10 per unit.
# If input unit is 350, Then add extra surcharge 500 Rs.
def get_units_of_electricity():
    units_of_electricity = int(input("Enter the units of electricity: "))
    return units_of_electricity


def calculate_electricity_bill():
    units_of_electricity = get_units_of_electricity()
    if units_of_electricity <= 100:
        electricity_bill = 0
    elif 100 < units_of_electricity <= 200:
        electricity_bill = (units_of_electricity - 100) * 5
    elif units_of_electricity > 200:
        electricity_bill = (units_of_electricity - 200) * 10 + 500
    return electricity_bill


if __name__ == '__main__':
    print(f"Your electricity bill is : {calculate_electricity_bill()}")
