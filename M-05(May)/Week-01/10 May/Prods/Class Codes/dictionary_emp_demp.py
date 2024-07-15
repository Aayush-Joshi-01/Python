EMP_LIST = []


def get_input(id: int) -> tuple[str, str, int]:
    """Get employee details from user input"""
    emp_name = input(f"Enter the employee {id} name: ")
    emp_salary = int(input(f"Enter the salary for employee {id} in whole numbers: "))
    return str(id), emp_name, emp_salary


def insert_employees(number_of_employees: int) -> None:
    """Insert employee details into the list"""
    for id in range(1, number_of_employees + 1):
        id, name, salary = get_input(id)
        EMP_LIST.append({'id': id, 'name': name, 'salary': salary})


def sum_of_salaries() -> int:
    """Find Sum of all Salaries"""
    sum = 0
    for emp in EMP_LIST:
        sum += emp['salary']
    return sum


def get_salaries() -> list[int]:
    """Get all the Fields"""
    sal = []
    for emp in EMP_LIST:
        sal.append(emp['salary'])
    return sal


def get_highest_and_lowest_salaries() -> tuple[int, int]:
    """Get Highest and Lowest Salaries"""
    sal = get_salaries()
    return max(sal), min(sal)


def update_employee(id: str, new_name: str = None, new_salary: int = None) -> None:
    """Update an employee's details"""
    for emp in EMP_LIST:
        if emp['id'] == id:
            if new_name:
                emp['name'] = new_name
            if new_salary:
                emp['salary'] = new_salary
            break
    else:
        print(f"Employee with id {id} not found")


def update() -> None:
    """Update an employee"""
    emp_id = input("Enter the employee id to update: ")
    update_key = input("Enter what do you want to update 0 for name and 1 for salary: ")
    new_name = ''
    new_salary = ''
    if update_key:
        new_name = input("Enter the new name: ")
    else:
        new_salary = int(input("Enter the new salary:  "))
    update_employee(emp_id, new_name if new_name else None, new_salary if new_salary else None)


if __name__ == '__main__':
    number_of_employees = int(input("Enter the number of employees you want to enter: "))
    insert_employees(number_of_employees)
    print(EMP_LIST)
    print(f"The sum of salaries is : {sum_of_salaries()}")
    highest, lowest = get_highest_and_lowest_salaries()
    print(f"Highest is {highest}, and lowest is  {lowest}")
    update()
    print(EMP_LIST)
