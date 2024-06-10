# You're tasked with creating a program to Calculator the average grade of students.
# How would you use a list in Python to store grades and compute the average?

def add_grades(grades, new_grades):
    grades.extend(new_grades)


def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


if __name__ == '__main__':
    grades = []
    while True:
        user_input = input("Enter 'add', 'Calculator', or 'quit': ")
        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'add':
            new_grades = list(map(int, input("Enter new grades (comma-separated): ").split(',')))
            add_grades(grades, new_grades)
        elif user_input.lower() == 'Calculator':
            average = calculate_average(grades)
            print(f"The average grade is: {average}")
        else:
            print("Invalid command.")
