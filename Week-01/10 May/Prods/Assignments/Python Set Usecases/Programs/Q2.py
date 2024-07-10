class Student:
    def __init__(self, name, rollno, courses):
        self.name = name
        self.rollno = rollno
        self.courses = courses


def get_unique_courses(students: list) -> set:
    unique_courses = set()
    for student in students:
        unique_courses.update(student.courses)
    return unique_courses


if __name__ == '__main__':
    students = [
        Student('aayush', 1, {'Math', 'Science', 'Astronomy'}),
        Student('prankur', 2, {'English', 'Science', 'History'}),
        Student('kaustaubh', 3, {'Math', 'English', 'Astronomy'})
    ]
    unique_courses = get_unique_courses(students)
    print(unique_courses)
