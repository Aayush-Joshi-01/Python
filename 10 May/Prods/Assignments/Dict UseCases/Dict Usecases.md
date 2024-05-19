# Dictionary usecase 

1:Wap to insert employee details in the form of one key and value as 
```
[e_id, name, email, salary]
```
A:display all employee details
  
B: Search by e_id , if e_id present then display employee details and if e_id not present the show message
     
“Employee Not present”.


```commandline
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
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
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
                print(f"Employee ID: {e_id}, Name: {details['name']}, Email: {details['email']}, Salary: {details['salary']}")
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
```

```commandline
Employee Management System
1. Add Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee
5. Search Employee by Name Substring
6. Exit
Enter your choice: 1
Enter employee ID: 1100673
Enter employee name: Aayush Joshi
Enter employee email: joshi.aayush@gmail.com
Enter employee salary: 14400
Employee added successfully!

Employee Management System
1. Add Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee
5. Search Employee by Name Substring
6. Exit
Enter your choice: 1
Enter employee ID: 1100777
Enter employee name: James Bond
Enter employee email: bond.james@yash.com
Enter employee salary: 777777
Employee added successfully!

Employee Management System
1. Add Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee
5. Search Employee by Name Substring
6. Exit
Enter your choice: 1
Enter employee ID: 1100123
Enter employee name: Prankur Aggarwal
Enter employee email: aggarwal.prankur@gmail.com
Enter employee salary: 14000
Employee added successfully!

Employee Management System
1. Add Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee
5. Search Employee by Name Substring
6. Exit
Enter your choice: 2
------------------------------------------------------------------------------------
Employee ID: 1100673, Name: Aayush Joshi, Email: joshi.aayush@gmail.com, Salary: 14400
Employee ID: 1100777, Name: James Bond, Email: bond.james@yash.com, Salary: 777777
Employee ID: 1100123, Name: Prankur Aggarwal, Email: aggarwal.prankur@gmail.com, Salary: 14000
------------------------------------------------------------------------------------

Employee Management System
1. Add Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee
5. Search Employee by Name Substring
6. Exit
Enter your choice: 3
Enter employee ID to search: 1100673
Employee ID: 1100673, Name: Aayush Joshi, Email: joshi.aayush@gmail.com, Salary: 14400

Employee Management System
1. Add Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee
5. Search Employee by Name Substring
6. Exit
Enter your choice: 4
Enter employee ID to update: 1100673
Enter new employee name: Aayush Joshi
Enter new employee email: joshi.aayush@yash.com
Enter new employee salary: 14400
Employee updated successfully!

Employee Management System
1. Add Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee
5. Search Employee by Name Substring
6. Exit
Enter your choice: 2
------------------------------------------------------------------------------------
Employee ID: 1100673, Name: Aayush Joshi, Email: joshi.aayush@yash.com, Salary: 14400
Employee ID: 1100777, Name: James Bond, Email: bond.james@yash.com, Salary: 777777
Employee ID: 1100123, Name: Prankur Aggarwal, Email: aggarwal.prankur@gmail.com, Salary: 14000
------------------------------------------------------------------------------------

Employee Management System
1. Add Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee
5. Search Employee by Name Substring
6. Exit
Enter your choice: 5
Enter name substring to search: joshi
Search Results:
Employee ID: 1100673, Name: Aayush Joshi, Email: joshi.aayush@yash.com, Salary: 14400

Employee Management System
1. Add Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee
5. Search Employee by Name Substring
6. Exit
Enter your choice: 5
Enter name substring to search: bond
Search Results:
Employee ID: 1100777, Name: James Bond, Email: bond.james@yash.com, Salary: 777777

Employee Management System
1. Add Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee
5. Search Employee by Name Substring
6. Exit
Enter your choice: 5
Enter name substring to search: agg
Search Results:
Employee ID: 1100123, Name: Prankur Aggarwal, Email: aggarwal.prankur@gmail.com, Salary: 14000

Employee Management System
1. Add Employee
2. Display All Employees
3. Search Employee by ID
4. Update Employee
5. Search Employee by Name Substring
6. Exit
Enter your choice: 6
Exiting the system. Goodbye!

Process finished with exit code 0
```