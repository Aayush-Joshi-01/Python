# You're building a to-do list application.
# How would you use a list in Python to allow users to add, remove, and mark tasks as completed?

def add_task(tasks, task):
    tasks.append(task)

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)

def mark_task_completed(tasks, task):
    if task in tasks:
        tasks[tasks.index(task)] = f"{task} (completed)"

if __name__ == '__main__':
    tasks = []

    while True:
        user_input = input("Enter 'add', 'remove', 'mark', or 'quit': ")
        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'add':
            new_task = input("Enter new task: ")
            add_task(tasks, new_task)
        elif user_input.lower() == 'remove':
            task_to_remove = input("Enter task to remove: ")
            remove_task(tasks, task_to_remove)
        elif user_input.lower() == 'mark':
            task_to_mark = input("Enter task to mark as completed: ")
            mark_task_completed(tasks, task_to_mark)
        else:
            print("Invalid command.")
        print(f"Tasks: {tasks}")
