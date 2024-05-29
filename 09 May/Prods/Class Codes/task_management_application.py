class task_manager:
    task_id =[]
    task_list = []
    task_status = []
    def add_task(self, id, task, status):
        self.task_id.append(id)
        self.task_list.append(task.lower())
        self.task_status.append(status.lower())
    def remove_task(self, id):
        index = self.task_id.remove(id)
        self.task_list.remove(index)
        self.task_status.remove(index)
    def update_task_status(self, id, status):
        index = self.task_id.index(id)
        self.task_status[index] = status
    def show_tasks(self):
        for id in range(len(self.task_id)):
            print(f"| {self.task_id[id]}, {self.task_list[id]}, {self.task_status[id]} |")
    def find_task(self, task_id):
        index = self.task_id.index(task_id)
        print(f"| {self.task_id[index]}, {self.task_list[index]}, {self.task_status[index]} |")
    def find_task_substring(self, task_string):
        for task in range(len(self.task_list)):
            if task_string in self.task_list[task]:
                print(f"| {self.task_id[task]}, {self.task_list[task]}, {self.task_status[task]} |")
    def find_task_status(self, status):
        for task in range(len(self.task_status)):
            if status in self.task_status[task]:
                print(f"| {self.task_id[task]}, {self.task_list[task]}, {self.task_status[task]} |")

class services:

    def print_services(self):
        print("1: Add Task ")
        print("2: Update Task Status ")
        print("3: Remove Task ")
        print("4: Show Task ")
        print("5: Find Task with Id ")
        print("6: Update Task Substring ")
        print("7: Find Task with Status ")
    def get_services(self):
        service_number = int(input("Enter the Service you want to use: "))
        return service_number
    def get_substring(self):
        task_substring = input("Enter the Task Substring: ")
        return task_substring
    def get_id(self):
        id = input("Enter the Id: ")
        return int(id)
    def get_status(self):
        task_status_string = input("Enter the Task Status  1: done / 2: in progress: ")
        if task_status_string.lower() in ["done", "1"]:
            task_status = "done"
        elif task_status_string.lower() == ["in progress", "2"]:
            task_status = "in progress"
        return task_status
    def service_calls(self, service_number):
        id = 0
        task_object = task_manager()
        if service_number == 1:
            task_title = input("Enter the Task: ")
            task_object.add_task(id+1, task_title, self.get_status())
        elif service_number == 2:
            task_object.show_task()
            task_object.update_task_status(self.get_id(), self.get_status())
        elif service_number == 3:
            task_object.show_task()
            task_object.remove_task(self.get_id())
        elif service_number == 4:
            task_object.show_tasks()
        elif service_number == 5:
            task_object.find_task(self.get_id())
        elif service_number == 6:
            task_object.find_task_substring(self.get_substring())
        elif service_number == 7:
            task_object.find_task_status(self.get_status())
    def service_manager(self):
        repeat = True
        login_obj = login()
        if login_obj.sign_in():
            while repeat:
                print("Welcome to the Task Manager")
                print("Please choose a service")
                self.print_services()
                service_number = self.get_services()
                self.service_calls(service_number)
        else:
            print("You are not authorized to use this service")
            print("Try again ")
            self.service_manager()

class login:
    def sign_in(self):
        username, password = self.get_user_pass()
        if username == "admin" and password == "123456":
            return True
        else:
            return False
    def get_user_pass(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return username, password

if __name__ == '__main__':
    service_object = services()
    service_object.service_manager()

