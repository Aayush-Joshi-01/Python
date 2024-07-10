# Calculate the ticket price based on age and student status.
#
#     Args:
#     - age: The age of the person
#     - is_student: Boolean indicating whether the person is a student (True/False)
#
#     Returns:
#     - The ticket price based on the age and student status.
def get_age_of_person():
    age_of_person = int(input("Enter the age of the person: "))
    return age_of_person


def get_person_status():
    status = input("Enter if you are a student y or n ?: ")
    if status.lower() in ['y', 'yes']:
        return True
    else:
        return False


def get_ticket_price(age_of_person, is_student):
    ticket_price = 0
    return ticket_price


if __name__ == '__main__':
    print(f"The price of the ticket is : {get_ticket_price(get_age_of_person(), get_person_status())}")
