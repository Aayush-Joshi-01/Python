# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

def get_inputs():
    salary = int(input("Enter your salary: "))
    start_year = int(input("Enter your year when you started: "))
    current_year = int(input("Enter your current year: "))
    get_service_bonus(salary, find_service_duration(start_year, current_year))

def find_service_duration(start_date, current_date):
    service_duration = current_date - start_date
    return service_duration

def get_service_bonus(salary, service_duration):
    if service_duration > 5:
        bonus = salary * 0.05
        print(f"Your bonus amount is: {bonus}")
    else:
        print("You are not eligible for bonus")

if __name__ == '__main__':
    print("Welcome to the Company Portal check your eligiblity of your account bonus: ")
    get_inputs()