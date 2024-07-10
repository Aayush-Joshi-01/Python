# Check eligibility for driving based on age and possession of a driver's license.
#
#     Args:
#     - age: The age of the person (in years)
#     - has_license: A boolean indicating whether the person has a driver's license
#
#     Returns:
#     - A string indicating whether the person is eligible to drive
def get_license():
    status = input("Do you have a driver license y or n: ")
    if status.lower() in ['y', 'yes']:
        return True
    else:
        return False


def get_age():
    age = int(input("Enter your age: "))
    return age


def eligiblity(age, has_license):
    if age >= 18 and has_license:
        return "Eligible to drive"
    else:
        return "Not eligible to drive"


if __name__ == '__main__':
    print(eligiblity(get_age(), get_license()))
