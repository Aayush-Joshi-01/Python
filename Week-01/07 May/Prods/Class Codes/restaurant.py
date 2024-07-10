TOTAL_TABLE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
BOOKED_TABLE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
VEG_MENU = {
    'Main Course': ['Paneer Tikka Masala', 'Paneer Butter Masala', 'Mix Veg', 'Palak Paneer', 'Yellow Dal Tadka',
                    'Dal Makhani'],
    'Starters': ['Veg Lollipop', 'Crispy Corn', 'Veg Kothe', 'Paneer Tikka', '']
}
NON_VEG_MENU = {
    'Main Course': ['Chicken Tikka Masala', 'Chicken Butter Masala', 'Mix Veg', 'Palak Chicken', 'Yellow Dal Tadka',
                    'Dal Makhani'],
    'Starters': ['Non Veg Lollipop', 'Crispy Corn', 'Non Veg Kothe', 'Chicken Tikka', '']
}


class view_menu:
    def veg(self):
        print("Welcome to the veg menu")
        print(VEG_MENU)

    def non_veg(self):
        print("Welcome to the Non Veg Menu: ")
        print(NON_VEG_MENU)


def menu(status):
    view = view_menu()
    if status:
        view.non_veg()
    else:
        view.veg()


def check_veg_availability(table):
    if table in BOOKED_TABLE:
        print("table is already booked")
        print("Available Tables are: ")
        print([available_table for available_table in TOTAL_TABLE if
               available_table not in BOOKED_TABLE and available_table % 2 == 0])
        vegetarian()
    else:
        print(f"Your table is booked: {table}")
        BOOKED_TABLE.append(table)
        menu(0)
        vegetarian_non_vegetarian()


def check_non_veg_availability(table):
    if table in BOOKED_TABLE:
        print("table is already booked")
        print("Available Tables are: ")
        print([available_table for available_table in TOTAL_TABLE if
               available_table not in BOOKED_TABLE and available_table % 2 != 0])
        non_vegetarian()
    else:
        print(f"Your table is booked: {table}")
        BOOKED_TABLE.append(table)
        menu(1)
        vegetarian_non_vegetarian()


def vegetarian():
    print("vegetarian")

    table = int(input("Enter the table number you want to dine into : "))
    if table % 2 != 0:
        print("Not a vegetarian table ")
        vegetarian()
    else:
        check_veg_availability(table)


def non_vegetarian():
    print("non vegetarian")
    table = int(input("Enter the table number you want to dine into : "))
    if table % 2 == 0:
        print("wrong table")
        non_vegetarian()
    else:
        check_non_veg_availability(table)


def vegetarian_non_vegetarian():
    preference = int(input("Enter your preference for veg press 0 for non veg press 1: "))
    if preference:
        non_vegetarian()
    else:
        vegetarian()


if __name__ == '__main__':
    vegetarian_non_vegetarian()
