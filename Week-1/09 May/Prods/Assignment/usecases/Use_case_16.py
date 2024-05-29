# You're building a program to manage employee shifts at a retail store.
# Write a Python function to determine the total number of hours worked by each employee given a list of shifts.

def total_hours_worked(shifts):
    total_hours = {}
    for shift in shifts:
        employee_id, hours = shift
        if employee_id not in total_hours:
            total_hours[employee_id] = 0
        total_hours[employee_id] += hours
    return total_hours


if __name__ == '__main__':
    shifts = [(1, 8), (2, 6), (1, 4), (3, 7), (2, 3)]

    total_hours = total_hours_worked(shifts)
    print(total_hours)
