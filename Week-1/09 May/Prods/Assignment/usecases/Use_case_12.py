# You're working on a project management tool.
# Write a Python function to calculate the total estimated duration of all tasks given a list of tasks with their respective durations.)
def calculate_total_duration(tasks):
    total_duration = 0
    for task in tasks:
        total_duration += task['duration']
    return total_duration


if __name__ == '__main__':
    tasks = [
        {'duration': 3},
        {'duration': 2},
        {'duration': 5},
        {'duration': 1},
        {'duration': 4}
    ]

    total_duration = calculate_total_duration(tasks)
    print(total_duration)
