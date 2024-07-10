import pymysql


class EmployeeDatabase:
    def __init__(self, host="localhost", user="root", password="root", database="employee_db"):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()
        self.create_database()
        self.conn.select_db(database)
        self.create_table()

    def create_database(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")
        self.conn.commit()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT,
            department VARCHAR(255)
        )
        """)
        self.conn.commit()

    def add_employee(self, name, age, department):
        self.cursor.execute("INSERT INTO employee (name, age, department) VALUES (%s, %s, %s)",
                            (name, age, department))
        self.conn.commit()

    def view_employees(self):
        self.cursor.execute("SELECT * FROM employee")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def update_employee(self, emp_id, name, age, department):
        self.cursor.execute("UPDATE employee SET name = %s, age = %s, department = %s WHERE id = %s",
                            (name, age, department, emp_id))
        self.conn.commit()

    def delete_employee(self, emp_id):
        self.cursor.execute("DELETE FROM employee WHERE id = %s", (emp_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()


def main():
    password = input("Enter your MySQL password: ")
    db = EmployeeDatabase(host="localhost", user="root", password=password, database="employee_db")

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                name = input("Enter name: ")
                age = input("Enter age: ")
                department = input("Enter department: ")
                db.add_employee(name, age, department)
            elif choice == '2':
                db.view_employees()
            elif choice == '3':
                emp_id = int(input("Enter employee ID to update: "))
                name = input("Enter new name: ")
                age = input("Enter new age: ")
                department = input("Enter new department: ")
                db.update_employee(emp_id, name, age, department)
            elif choice == '4':
                emp_id = int(input("Enter employee ID to delete: "))
                db.delete_employee(emp_id)
            elif choice == '5':
                db.close()
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
