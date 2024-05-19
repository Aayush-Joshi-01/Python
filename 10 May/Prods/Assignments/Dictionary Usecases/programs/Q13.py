def add_student(students, student):
    students.append(student)


def update_student(students, student_id, new_name, new_gpa):
    for student in students:
        if student['student_id'] == student_id:
            student['name'] = new_name
            student['gpa'] = new_gpa
            break


def remove_student(students, student_id):
    for i, student in enumerate(students):
        if student['student_id'] == student_id:
            del students[i]
            break


def get_student_with_highest_gpa(students):
    return max(students, key=lambda x: x['gpa'])


if __name__ == '__main__':
    students = [
        {'student_id': 1001, 'name': 'aayush', 'gpa': 3.8},
        {'student_id': 1002, 'name': 'prankur', 'gpa': 3.6},
        {'student_id': 1003, 'name': 'ishaan', 'gpa': 3.9},
        {'student_id': 1004, 'name': 'aaditya', 'gpa': 3.7},
    ]
    new_student = {'student_id': 1005, 'name': 'aaditya', 'gpa': 3.9}
    add_student(students, new_student)
    update_student(students, 1001, 'aayush (updated)', 4.0)
    remove_student(students, 1002)
    highest_gpa_student = get_student_with_highest_gpa(students)
    print(f"Student with the highest GPA is: {highest_gpa_student['name']} with GPA {highest_gpa_student['gpa']:.2f}")