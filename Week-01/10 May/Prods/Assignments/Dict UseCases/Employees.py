import re


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        while True:
            try:
                e_id = int(input("Enter employee ID: "))
                if e_id in self.employees:
                    print("Employee ID already exists!")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        name = input("Enter employee name: ")
        while True:
            try:
                email = input("Enter employee email: ")
                if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
                    print("Invalid email address. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid email address.")

        while True:
            try:
                salary = int(input("Enter employee salary: "))
                if salary < 0:
                    print("Salary cannot be negative. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.employees[e_id] = {"name": name, "email": email, "salary": salary}
        print("Employee added successfully!")

    def display_all_employees(self):
        if not self.employees:
            print("No employees found!")
        else:
            print("------------------------------------------------------------------------------------")
            for e_id, details in self.employees.items():
                print(
                    f"Employee ID: {e_id}, Name: {details['name']}, Email: {details['email']}, Salary: {details['salary']}")
            print("------------------------------------------------------------------------------------")

    def search_by_e_id(self):
        while True:
            try:
                e_id = int(input("Enter employee ID to search: "))
                if e_id in self.employees:
                    details = self.employees[e_id]
                    print(
                        f"Employee ID: {e_id}, Name: {details['name']}, Email: {details['email']}, Salary: {details['salary']}")
                else:
                    print("Employee not found!")
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    def update_employee(self):
        while True:
            try:
                e_id = int(input("Enter employee ID to update: "))
                if e_id in self.employees:
                    break
                else:
                    print("Employee not found!")
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.employees[e_id]["name"] = input("Enter new employee name: ")
        self.employees[e_id]["email"] = input("Enter new employee email: ")
        while True:
            try:
                self.employees[e_id]["salary"] = int(input("Enter new employee salary: "))
                if self.employees[e_id]["salary"] < 0:
                    print("Salary cannot be negative. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        print("Employee updated successfully!")

    def search_by_name_substring(self):
        substring = input("Enter name substring to search: ")
        matches = []
        for e_id, details in self.employees.items():
            if substring.lower() in details["name"].lower():
                matches.append((e_id, details))
        if matches:
            print("Search Results:")
            for match in matches:
                e_id, details = match
                print(
                    f"Employee ID: {e_id}, Name: {details['name']}, Email: {details['email']}, Salary: {details['salary']}")
        else:
            print("No matches found!")

    def run(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add Employee")
            print("2. Display All Employees")
            print("3. Search Employee by ID")
            print("4. Update Employee")
            print("5. Search Employee by Name Substring")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.display_all_employees()
            elif choice == "3":
                self.search_by_e_id()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.search_by_name_substring()
            elif choice == "6":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again!")


if __name__ == "__main__":
    ems = EmployeeManagementSystem()
    ems.run()
