def add_student(name, age, grade, student_records):
    new_student = {'name': name, 'age': age, 'grade': grade}
    student_records[name] = new_student


def modify_student(name, age=None, grade=None, student_records=None):
    if student_records is None:
        student_records = student_records
    if age is not None:
        student_records[name]['age'] = age
    if grade is not None:
        student_records[name]['grade'] = grade


def remove_student(name, student_records=None):
    if student_records is None:
        student_records = student_records
    del student_records[name]


if __name__ == '__main__':
    student_records = {
        'aayush': {'age': 18, 'grade': 'A'},
        'prankur': {'age': 17, 'grade': 'B'},
        'aaditya': {'age': 16, 'grade': 'A-'}
    }
    add_student('ishaan', 19, 'B+', student_records)
    modify_student('aayush', age=21, student_records=student_records)
    remove_student('aaditya', student_records)
    print(student_records)
