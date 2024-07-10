import datetime


def arrange_emp_acc_to_doj(emp_list: list) -> list:
    return sorted(emp_list, key=lambda date: date["DOJ"])


if __name__ == '__main__':
    emp = [
        {"name": "aayush", "DOJ": datetime.datetime(2024, 4, 8)},
        {"name": "vikrant", "DOJ": datetime.datetime(2022, 2, 8)},
        {"name": "prankur", "DOJ": datetime.datetime(2023, 12, 5)},
        {"name": "aaditya", "DOJ": datetime.datetime(2022, 1, 8)}
    ]
    for temps in emp:
        print(temps)
