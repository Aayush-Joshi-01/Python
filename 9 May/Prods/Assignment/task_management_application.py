class TaskManager:
    """Task manager class"""

    def __init__(self):
        self.tasks = []

    def add_task(self, task_title: str, status: str) -> None:
        """Add a new task"""
        self.tasks.append({"id": len(self.tasks) + 1, "title": task_title.lower(), "status": status.lower()})

    def remove_task(self, task_id: int) -> None:
        """Remove a task by ID"""
        self.tasks = [task for task in self.tasks if task["id"] != task_id]

    def update_task_status(self, task_id: int, status: str) -> None:
        """Update a task's status"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = status.lower()
                break

    def show_tasks(self) -> None:
        """Show all tasks"""
        print("-------------------------------------------------------------------")
        for task in self.tasks:
            print(f"| {task['id']}, {task['title']}, {task['status']} |")
        print("-------------------------------------------------------------------")
        continue_var = int(input("To Continue press 1:  "))
        if continue_var:
            pass

    def find_task(self, task_id: int) -> None:
        """Find a task by ID"""
        for task in self.tasks:
            if task["id"] == task_id:
                print(f"| {task['id']}, {task['title']}, {task['status']} |")
                break

    def find_task_substring(self, task_string: str) -> None:
        """Find tasks containing a substring"""
        for task in self.tasks:
            if task_string in task["title"]:
                print(f"| {task['id']}, {task['title']}, {task['status']} |")

    def find_task_status(self, status: str) -> None:
        """Find tasks by status"""
        for task in self.tasks:
            if task["status"] == status.lower():
                print(f"| {task['id']}, {task['title']}, {task['status']} |")


class Login:
    """Login class"""
    def sign_in(self) -> bool:
        """Sign in with username and password"""
        username, password = self.get_user_pass()
        return username == "admin" and password == "123456"

    @staticmethod
    def get_user_pass() -> tuple:
        """Get username and password from user"""
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return username, password


class ServiceManager:
    """Service manager class"""

    def __init__(self):
        self.task_manager = TaskManager()
        self.login = Login()

    @staticmethod
    def print_services() -> None:
        """Print available services"""
        print("--------------------------------------------")
        print("1: Add Task")
        print("2: Update Task Status")
        print("3: Remove Task")
        print("4: Show Task")
        print("5: Find Task with Id")
        print("6: Find Task using Substring")
        print("7: Find Task with Status")
        print("8: Quit")
        print("--------------------------------------------")

    @staticmethod
    def get_service_number() -> int:
        """Get service number from user"""
        while True:
            try:
                service_number = int(input("Enter the Service you want to use: "))
                if 1 <= service_number <= 8:
                    return service_number
                else:
                    print("Invalid service number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def service_calls(self, service_number: int) -> bool:
        """Handle service calls"""
        if service_number == 1:
            task_title = input("Enter the Task: ")
            status = self.get_status()
            self.task_manager.add_task(task_title, status)
            return True
        elif service_number == 2:
            self.task_manager.show_tasks()
            task_id = int(input("Enter the Task ID: "))
            status = self.get_status()
            self.task_manager.update_task_status(task_id, status)
            return True
        elif service_number == 3:
            self.task_manager.show_tasks()
            id = int(input("Enter the ID you want to remove: "))
            self.task_manager.remove_task(id)
            return True
        elif service_number == 4:
            self.task_manager.show_tasks()
            return True
        elif service_number == 5:
            task_id = int(input("Enter the Task ID: "))
            self.task_manager.find_task(task_id)
            return True
        elif service_number == 6:
            task_string = input("Enter the Task Substring: ")
            self.task_manager.find_task_substring(task_string)
            return True
        elif service_number == 7:
            status = self.get_status()
            self.task_manager.find_task_status(status)
            return True
        elif service_number == 8:
            return False

    @staticmethod
    def get_status() -> str:
        """Get task status from user"""
        while True:
            task_status_string = input("Enter the Task Status  1: done / 2: in progress: ")
            if task_status_string in ["1", "done"]:
                return "done"
            elif task_status_string in ["2", "in progress"]:
                return "in progress"
            else:
                print("Invalid status. Please try again.")

    def service_manager(self) -> None:
        repeat = True
        """Service manager loop"""
        if self.login.sign_in():
            while repeat:
                print("Welcome to the Task Manager")
                print("Please choose a service")
                self.print_services()
                service_number = self.get_service_number()
                repeat = self.service_calls(service_number)
        else:
            print("You are not authorized to use this service")
            print("Try again ")
            self.service_manager()


if __name__ == '__main__':
    service_manager = ServiceManager()
    service_manager.service_manager()
