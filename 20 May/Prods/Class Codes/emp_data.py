def arrange_emp_acc_to_doj(emp: list) -> list:
    return sorted(emp, key=lambda d: d["DOJ"])


if __name__ == '__main__':
    emp = [{"name": "aayush", "DOJ": 2024}, {"name": "vikrant", "DOJ": 2023},
           {"name": "prankur", "DOJ": 2021}, {"name": "aaditya", "DOJ": 2025}]
    print(arrange_emp_acc_to_doj(emp))
