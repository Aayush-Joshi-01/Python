def add_task(project_name, task_name, assignee, task_management):
    if project_name not in task_management:
        task_management[project_name] = {'start_date': None, 'end_date': None, 'tasks': {}}
    task_management[project_name]['tasks'][task_name] = {'assignee': assignee, 'status': 'Pending'}


def update_task_status(project_name, task_name, status, task_management):
    if project_name in task_management and task_name in task_management[project_name]['tasks']:
        task_management[project_name]['tasks'][task_name]['status'] = status


def mark_task_complete(project_name, task_name, task_management):
    update_task_status(project_name, task_name, 'Completed', task_management)


if __name__ == '__main__':
    task_management = {
        'Project A': {'start_date': '2024-01-01', 'end_date': '2024-06-30',
                      'tasks': {'Task 1': {'assignee': 'aayush', 'status': 'Completed'},
                                'Task 2': {'assignee': 'prankur', 'status': 'In Progress'},
                                'Task 3': {'assignee': 'aaditya', 'status': 'Pending'}}},
        'Project B': {'start_date': '2024-02-15', 'end_date': '2024-08-31',
                      'tasks': {'Task 1': {'assignee': 'aayush', 'status': 'In Progress'},
                                'Task 2': {'assignee': 'palak', 'status': 'Pending'},
                                'Task 3': {'assignee': 'ishaan', 'status': 'Completed'}}}
    }
    add_task('Project A', 'Task 4', 'kaustaubh', task_management)
    update_task_status('Project A', 'Task 2', 'Completed', task_management)
    mark_task_complete('Project B', 'Task 1', task_management)
    print(task_management)
