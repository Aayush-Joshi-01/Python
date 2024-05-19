emp_name = [
    'amit',
    [
        'dept', 'IT','email', 'amit@gmail.com'
    ],
    'aarvi',
    [
        'dept', 'MECH', 'email', 'aarvi@gmail.com'
    ],
    'aayush',
    [
        'dept', 'CSE', 'email', 'aayush@gmail.com'
    ]
]

for id in range(0,6,2):
    print(f"{emp_name[id]} -> ", end=" ")
    for index in range(0,4,2):
        print(f"{emp_name[id+1][index]} : {emp_name[id+1][index+1]}", end="  ")
    print()