def find_completed_modules(employee_training_records):
    completed_modules = set()
    num_employees = len(employee_training_records)
    for module in employee_training_records[0]:
        if all(module in employee_training_records[i] and employee_training_records[i][module] for i in range(num_employees)):
            completed_modules.add(module)
    return completed_modules


if __name__ == '__main__':
    employee_training_records = [
        {
            "module1": True,
            "module2": True,
            "module3": False,
            "module4": True,
        },
        {
            "module1": True,
            "module2": True,
            "module3": True,
            "module4": True,
        },
        {
            "module1": True,
            "module2": True,
            "module3": True,
            "module4": True,
        },
    ]
    completed_modules = find_completed_modules(employee_training_records)
    print(completed_modules)