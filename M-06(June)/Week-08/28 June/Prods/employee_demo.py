EMPLOYEE = []

def input_emp_data():
    emp_data = {}
    emp_data['id'] = input("Enter employee ID: ")
    emp_data['name'] = input("Enter employee name: ")
    emp_data['department'] = input("Enter employee department: ")
    emp_data['salary'] = float(input("Enter employee salary: "))
    return emp_data

def sort_by_salary():
    sorted_emp_data = sorted(EMPLOYEE, key=lambda x: x['salary'], reverse=True)
    return sorted_emp_data

if __name__ == '__main__':
    number_of_employees = int(input("Enter the number of employees: "))
    for i in range(int(number_of_employees)):
        EMPLOYEE.append(input_emp_data())
    
    print(sort_by_salary())
