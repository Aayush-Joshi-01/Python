def highest_paid_employee(employees):
    return max(employees, key=lambda x: employees[x]['salary'])


def lowest_paid_employee(employees):
    return min(employees, key=lambda x: employees[x]['salary'])


def count_salaries_in_range(employees, low, high):
    return sum(1 for e in employees if low <= employees[e]['salary'] <= high)


def sort_by_date_ascending(employees):
    return sorted(employees, key=lambda x: employees[x]['date_of_joining'])


def sort_by_date_descending(employees):
    return sorted(employees, key=lambda x: employees[x]['date_of_joining'], reverse=True)


if __name__ == '__main__':
    employees = {
        1: {'id': 1, 'salary': 50000, 'date_of_joining': '2021-01-01'},
        2: {'id': 2, 'salary': 60000, 'date_of_joining': '2021-02-01'},
        3: {'id': 3, 'salary': 70000, 'date_of_joining': '2021-03-01'},
        4: {'id': 4, 'salary': 80000, 'date_of_joining': '2021-04-01'},
        5: {'id': 5, 'salary': 90000, 'date_of_joining': '2021-05-01'},
    }
    print("Highest paid employee:", highest_paid_employee(employees))
    print("Lowest paid employee:", lowest_paid_employee(employees))
    print("Number of employees with salaries between 60000 and 80000:", count_salaries_in_range(employees, 60000, 80000))
    print("Employees sorted by date of joining (ascending):", sort_by_date_ascending(employees))
    print("Employees sorted by date of joining (descending):", sort_by_date_descending(employees))