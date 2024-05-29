import pickle as pick

emp = {'name': 'aayush', 'number': '9910132767'}
with open('data.txt', 'wb') as file:
    pick.dump(emp, file)
with open('data.txt', 'rb') as file:
    emp_d = pick.load(file)
    print(emp_d)

emp = {'name': 'aayush', 'age': 22}
emp_str = pick.dumps(emp)
print(emp_str)
emp_obj = pick.loads(emp_str)
print(emp_obj)
