def calculate_average_score(subject, exam_results):
    total_score = 0
    num_students = 0
    for student_score in exam_results.values():
        if subject in student_score:
            total_score += student_score[subject]
            num_students += 1
    if num_students > 0:
        average_score = total_score / num_students
        return average_score
    else:
        return None


if __name__ == '__main__':
    exam_results = {
        'ishaan': {'Math': 85, 'Science': 90, 'English': 95},
        'prankur': {'Math': 75, 'Science': 80, 'English': 85},
        'aayush': {'Math': 95, 'Science': 95, 'English': 90},
        'aaditya': {'Math': 80, 'Science': 85, 'English': 90}
    }
    math_average = calculate_average_score('Math', exam_results)
    print(f"The average score of students in Math is {math_average}.")
    history_average = calculate_average_score('History', exam_results)
    print(f"The average score of students in History is {history_average}.")
    science_average = calculate_average_score('Science', exam_results)
    print(f"The average score of students in Science is {science_average}.")
