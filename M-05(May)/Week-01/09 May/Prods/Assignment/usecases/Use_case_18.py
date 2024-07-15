# You're designing a program to process student enrollment data.
# Write a Python function to determine the most popular course choices among students given a list of enrollments.

def most_popular_courses(enrollments):
    course_counts = {}
    for enrollment in enrollments:
        course = enrollment['course']
        if course not in course_counts:
            course_counts[course] = 0
        course_counts[course] += 1
    most_popular_course = max(course_counts, key=course_counts.get)
    return most_popular_course, course_counts[most_popular_course]


if __name__ == '__main__':
    enrollments = [
        {'student': 'A', 'course': 'Math'},
        {'student': 'B', 'course': 'Math'},
        {'student': 'C', 'course': 'Science'},
        {'student': 'D', 'course': 'Math'},
        {'student': 'E', 'course': 'Science'},
        {'student': 'F', 'course': 'Math'},
    ]

    popular_course, count = most_popular_courses(enrollments)

    print("Most popular course: ", popular_course)
    print("Number of enrollments: ", count)
