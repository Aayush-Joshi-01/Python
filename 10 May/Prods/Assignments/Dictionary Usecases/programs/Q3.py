def add_employee(employee_id, name, department, salary, employee_database):
    if employee_id not in employee_database:
        employee_database[employee_id] = {'name': name, 'department': department, 'salary': salary}
        print(f"Employee with ID {employee_id} added to the system.")
    else:
        print(f"Employee with ID {employee_id} already exists in the system.")


if __name__ == '__main__':
    employee_database = {}
    add_employee(1001, 'aayush', 'CSE', 50000, employee_database)
    add_employee(1002, 'aaditya', 'Mech', 60000, employee_database)
    add_employee(1003, 'ishaan', 'IT', 70000, employee_database)
    add_employee(1004, 'prankur', 'Commerce', 80000, employee_database)
    add_employee(1001, 'arnav', 'Arts', 90000, employee_database)
    print(employee_database)