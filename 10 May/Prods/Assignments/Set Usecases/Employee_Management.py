global choice


class EmployeeAttendanceSystem:
    def __init__(self):
        self.present_employees = set()
        self.absent_employees = set()
        self.check_ins = set()
        self.check_outs = set()
        self.morning_shift = set()
        self.evening_shift = set()

    @staticmethod
    def display_menu() -> None:
        print("Employee Attendance Management System: ")
        print("\nChoose the service from below")
        print("--------------------------------------------------------")
        print("1. Attendance Management")
        print("2. Check-In and Check-Out Management")
        print("3. Shift Management")
        print("4. Quit")
        print("--------------------------------------------------------")

    @staticmethod
    def attendance_menu() -> None:
        print("\nAttendance Menu\n")
        print("1. Mark Employee Present")
        print("2. Mark Employee Absent")
        print("3. View Present Employee ID")
        print("4. View Absent Employee ID")
        print("5. Exit to Main Menu")

    @staticmethod
    def check_in_check_out_menu() -> None:
        print("\nCheck-In and Check-Out Menu\n")
        print("1. Record Employee Check-In")
        print("2. Record Employee Check-Out")
        print("3. View Checked-In Employee")
        print("4. View Checked-Out Employee")
        print("5. Exit to Main Menu")

    @staticmethod
    def shifts_menu() -> None:
        print("\nShifts Menu\n")
        print("1. Schedule an Employee for Morning Shift")
        print("2. Schedule an employee for Evening Shift")
        print("3. View the Morning Shift Employees")
        print("4. View the Evening Shift Employees")
        print("5. Exit to Main Menu")

    def attendance_system(self) -> None:
        global choice
        while True:
            self.attendance_menu()
            try:
                choice = int(input("Enter the sub service you want to use: "))
            except ValueError:
                print("\nEnter a Valid Choice\n")
                self.attendance_system()
            if choice == 1:
                self.mark_employee_present()
            elif choice == 2:
                self.mark_employee_absent()
            elif choice == 3:
                self.view_present_employees()
            elif choice == 4:
                self.view_absent_employees()
            elif choice == 5:
                print("Returning to the Main Menu.....\n\n")
                break
            else:
                print("Enter a valid Choice")

    def check_in_and_out_system(self) -> None:
        global choice
        while True:
            self.check_in_check_out_menu()
            try:
                choice = int(input("Enter the sub service you want to use: "))
            except ValueError:
                print("\nEnter a Valid Choice\n")
                self.check_in_and_out_system()
            if choice == 1:
                self.record_check_in()
            elif choice == 2:
                self.record_check_out()
            elif choice == 3:
                self.view_check_ins()
            elif choice == 4:
                self.view_check_outs()
            elif choice == 5:
                print("Returning to the Main Menu.....\n\n")
                break
            else:
                print("Enter a valid Choice")

    def shifts_system(self) -> None:
        global choice
        while True:
            self.shifts_menu()
            try:
                choice = int(input("Enter the sub service you want to use: "))
            except ValueError:
                print("\nEnter a Valid Choice\n")
                self.shifts_system()
            if choice == 1:
                self.schedule_morning_shift()
            elif choice == 2:
                self.schedule_evening_shift()
            elif choice == 3:
                self.view_morning_shift()
            elif choice == 4:
                self.view_evening_shift()
            elif choice == 5:
                print("Returning to the Main Menu.....\n\n")
                break
            else:
                print("Enter a valid Choice")

    def mark_employee_present(self) -> None:
        employee_id = int(input("Enter employee ID: "))
        self.present_employees.add(employee_id)
        print(f"Employee {employee_id} marked as present.")

    def mark_employee_absent(self) -> None:
        employee_id = int(input("Enter employee ID: "))
        self.absent_employees.add(employee_id)
        print(f"Employee {employee_id} marked as absent.")

    def record_check_in(self) -> None:
        employee_id = int(input("Enter employee ID: "))
        self.check_ins.add(employee_id)
        print(f"Employee {employee_id} checked in.")

    def record_check_out(self) -> None:
        employee_id = int(input("Enter employee ID: "))
        self.check_outs.add(employee_id)
        print(f"Employee {employee_id} checked out.")

    def schedule_morning_shift(self) -> None:
        employee_id = int(input("Enter employee ID: "))
        self.morning_shift.add(employee_id)
        print(f"Employee {employee_id} scheduled for morning shift.")

    def schedule_evening_shift(self) -> None:
        employee_id = int(input("Enter employee ID: "))
        self.evening_shift.add(employee_id)
        print(f"Employee {employee_id} scheduled for evening shift.")

    def view_present_employees(self) -> None:
        print("Present Employees:")
        if len(self.present_employees):
            for employee_id in self.present_employees:
                print(employee_id)
        else:
            print("There are no Present Employees")

    def view_absent_employees(self) -> None:
        print("Absent Employees:")
        if len(self.absent_employees):
            for employee_id in self.absent_employees:
                print(employee_id)
        else:
            print("There are not Absent Employees")

    def view_check_ins(self) -> None:
        print("Employee Check-Ins:")
        if len(self.check_ins):
            for employee_id in self.check_ins:
                print(employee_id)
        else:
            print("There are no Check-Ins")

    def view_check_outs(self) -> None:
        print("Employee Check-Outs:")
        if len(self.check_outs):
            for employee_id in self.check_outs:
                print(employee_id)
        else:
            print("There are no Check-Outs")

    def view_morning_shift(self) -> None:
        print("Morning Shift Schedule:")
        if len(self.morning_shift):
            for employee_id in self.morning_shift:
                print(employee_id)
        else:
            print("There are no Employees in Morning Shift")

    def view_evening_shift(self) -> None:
        print("Evening Shift Schedule:")
        if len(self.evening_shift):
            for employee_id in self.evening_shift:
                print(employee_id)
        else:
            print("There are no Employees in Evening Shift")

    def run(self) -> None:
        global choice
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("\nEnter a Valid Choice\n")
                self.run()
            if choice == 1:
                self.attendance_system()
            elif choice == 2:
                self.check_in_and_out_system()
            elif choice == 3:
                self.shifts_system()
            elif choice == 4:
                print("Quiting the System....")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    attendance_system = EmployeeAttendanceSystem()
    attendance_system.run()
