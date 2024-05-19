# You're developing a task management application.
# How would you use a list in Python to allow users to add, remove, and view tasks?

def add_task(tasks, task):
    tasks.append(task)

def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    else:
        print("Invalid task index.")

def view_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

if __name__ == '__main__':
    tasks = []
    while True:
        user_input = input("Enter 'add', 'remove', 'view', or 'quit': ")
        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'add':
            new_task = input("Enter a new task: ")
            add_task(tasks, new_task)
        elif user_input.lower() == 'remove':
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index - 1)
        elif user_input.lower() == 'view':
            view_tasks(tasks)
        else:
            print("Invalid command.")
