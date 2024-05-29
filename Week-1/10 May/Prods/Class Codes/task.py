# insert employee details with number of details
# emp id name and salary
# count total salary
# highest paid employee
# lowest paid employee
# make list then make tuple inside that list
EMP_LIST = []


def get_input(id: int) -> tuple[str, str, int]:
    emp_name = input("Enter the employee name: ")
    emp_salary = int(input("Enter the salary in whole numbers: "))
    return str(id), emp_name, emp_salary


def insert_employees(number_of_employees: int) -> None:
    for id in range(1, number_of_employees + 1):
        EMP_LIST.append(get_input(id))


def sum_of_salaries() -> int:
    sum = 0
    for emp in EMP_LIST:
        sum += emp[2]
    return sum


def get_salaries() -> list[int]:
    sal = []
    for emp in EMP_LIST:
        sal.append(emp[2])
    return sal


def get_highest_and_lowest_salaries() -> tuple[int, int]:
    sal = get_salaries()
    return max(sal), min(sal)


if __name__ == '__main__':
    number_of_employees = int(input("Enter the number of employees you want to enter: "))
    insert_employees(number_of_employees)
    print(EMP_LIST)
    print(f"The sum of salaries is : {sum_of_salaries()}")
    highest, lowest = get_highest_and_lowest_salaries()
    print(f"Highest is {highest}, and lowest is  {lowest}")
