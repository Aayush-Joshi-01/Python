import pickle


def add_employee_record():
    with open('Assets/employee.dat', 'ab') as file:
        employee = {}
        employee['empcode'] = input('Enter employee code: ')
        employee['name'] = input('Enter name: ')
        employee['salary'] = float(input('Enter salary: '))
        pickle.dump(employee, file)


def display_high_salary_employees():
    try:
        with open('Assets/employee.dat', 'rb') as file:
            while True:
                try:
                    employee = pickle.load(file)
                    if employee['salary'] > 30000:
                        print(employee)
                except EOFError:
                    break
    except FileNotFoundError:
        print('File not found')


add_employee_record()
display_high_salary_employees()
