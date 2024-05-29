import pickle


def count_rec():
    count = 0
    try:
        with open('Assets/student.dat', 'rb') as file:
            while True:
                try:
                    student = pickle.load(file)
                    if student['Percentage'] > 75:
                        print(student)
                        count += 1
                except EOFError:
                    break
    except FileNotFoundError:
        print('File not found')
    print(f'Number of students with percentage above 75: {count}')


count_rec()
