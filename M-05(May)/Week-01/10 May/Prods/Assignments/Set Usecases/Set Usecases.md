# Consider a project for managing employee attendance in a company. Sets can be used in various aspects of this project:

## Employee IDs:

Sets can store unique employee IDs to keep track of employees who have attended work. This ensures that each employee is
counted only once, regardless of how many times they attend.

```
present_employees = {101, 102, 105, 107, 110}  # Employee IDs of those present
```

## Employee Attendance Tracking:

Sets can be used to efficiently check whether a particular employee is present or absent on a given day.

```
present_employees = {101, 102, 105, 107, 110}  # Employee IDs of those present
absent_employees = {103, 106, 108, 109}  # Employee IDs of those absent
```

## Employee Check-ins:

Sets can store employee IDs to keep track of unique check-ins made by employees throughout the day. This ensures that
duplicate check-ins are not counted.

```
check_ins = {101, 102, 103, 105, 107, 109}  # Employee IDs of those who checked in
```

## Employee Check-out:

Sets can also be used to store employee IDs to keep track of unique check-outs made by employees. This helps in
calculating the total hours worked by each employee accurately.

```
check_outs = {101, 102, 105, 107}  # Employee IDs of those who checked out
```

## Employee Shift Scheduling:

Sets can represent the set of employees scheduled to work during a particular shift. This ensures that each employee is
scheduled only once for a shift.

```
morning_shift = {101, 102, 105, 110}  # Employee IDs scheduled for the morning shift
evening_shift = {103, 106, 107, 109}  # Employee IDs scheduled for the evening shift
```

```commandline
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

```

---

## Sets can be used in various aspects of this project:

---

### Member IDs:

Sets can store unique member IDs to efficiently manage membership records and quickly check for membership validity.

```
member_ids = {101, 102, 103, 104, ...}
```

### Membership Plans:

Sets can represent different membership plans offered by the gym. Each set might contain the features included in a
particular plan.

```
basic_membership = {"Gym Access", "Cardio Equipment", "Locker Room Access"}
premium_membership = {"Gym Access", "Cardio Equipment", "Strength Training Equipment", "Group Classes", "Locker Room Access", "Towel Service"}
```

### Class Attendance:

Sets can track attendance for group classes. Each set might contain the member IDs of attendees for a specific class
session.

```
pilates_class_attendance = {101, 103, 105, ...}
yoga_class_attendance = {102, 104, 106, ...}
```

### Membership Renewals:

Sets can store member IDs for those who have renewed their memberships for the upcoming month.

```
membership_renewals = {101, 102, 105, ...}
```

### Locker Assignments:

Sets can represent locker assignments. Each set might contain locker numbers assigned to members.

```
locker_assignments = {"A101", "B203", "C305", ...}
```

```commandline
class Membership:
    def __init__(self):
        self.member_ids = set()
        self.member_plans = {
            "basic_membership": {"Gym Access", "Cardio Equipment", "Locker Room Access"},
            "premium_membership": {
                "Gym Access",
                "Cardio Equipment",
                "Strength Training Equipment",
                "Group Classes",
                "Locker Room Access",
                "Towel Service",
            },
        }
        self.class_attendance = {}
        self.membership_renewals = set()
        self.locker_assignments = set()

    def add_member(self, member_id: int) -> None:
        if member_id in self.member_ids:
            print("Member ID already exists.")
            return
        self.member_ids.add(member_id)

    def remove_member(self, member_id: int) -> None:
        if member_id not in self.member_ids:
            print("Member ID does not exist.")
            return
        self.member_ids.remove(member_id)
        if member_id in self.class_attendance:
            del self.class_attendance[member_id]
        if member_id in self.membership_renewals:
            self.membership_renewals.remove(member_id)
        if member_id in self.locker_assignments:
            self.locker_assignments.remove(member_id)

    def assign_plan(self, member_id: int, plan_name: str) -> None:
        if member_id not in self.member_ids:
            print("Member ID does not exist.")
            return
        if plan_name not in self.member_plans:
            print("Invalid membership plan.")
            return

    def update_attendance(self, class_name: str, member_ids: list) -> None:
        if class_name not in self.class_attendance:
            self.class_attendance[class_name] = set()
        for member_id in member_ids:
            if member_id not in self.member_ids:
                print("Member ID does not exist.")
                return
        self.class_attendance[class_name].update(member_ids)

    def renew_membership(self, member_id: int) -> None:
        if member_id not in self.member_ids:
            print("Member ID does not exist.")
            return
        self.membership_renewals.add(member_id)

    def assign_locker(self, member_id: int, locker_number: int) -> None:
        if member_id not in self.member_ids:
            print("Member ID does not exist.")
            return
        if locker_number in self.locker_assignments:
            print("Locker is already assigned.")
            return
        self.locker_assignments.add((member_id, locker_number))

    def view_members(self) -> None:
        print("Member IDs:", self.member_ids)

    def view_plans(self) -> None:
        print("Membership Plans:")
        for plan_name, features in self.member_plans.items():
            print(f"{plan_name}: {', '.join(features)}")

    def view_attendance(self) -> None:
        print("Class Attendance:")
        for class_name, member_ids in self.class_attendance.items():
            print(f"{class_name}: {', '.join(map(str, member_ids))}")

    def view_renewals(self) -> None:
        print("Membership Renewals:", self.membership_renewals)

    def view_lockers(self) -> None:
        print("Locker Assignments:")
        for member_id, locker_number in self.locker_assignments:
            print(f"Member ID {member_id}: Locker {locker_number}")

    def display_members_menu(self) -> None:
        while True:
            print("\n1. Add Member")
            print("2. Remove Member")
            print("3. View Members")
            print("4. Back")

            option = int(input("Enter your option: "))
            if option == 1:
                member_id = int(input("Enter member ID: "))
                self.add_member(member_id)
            elif option == 2:
                member_id = int(input("Enter member ID: "))
                self.remove_member(member_id)
            elif option == 3:
                self.view_members()
            elif option == 4:
                break
            else:
                print("Invalid option.")

    def display_plans_menu(self) -> None:
        while True:
            print("\n1. Assign Membership Plan")
            print("2. View Membership Plans")
            print("3. Back")

            option = int(input("Enter your option: "))
            if option == 1:
                member_id = int(input("Enter member ID: "))
                plan_name = input("Enter membership plan: ")
                self.assign_plan(member_id, plan_name)
            elif option == 2:
                self.view_plans()
            elif option == 3:
                break
            else:
                print("Invalid option.")

    def display_attendance_menu(self) -> None:
        while True:
            print("\n1. Update Class Attendance")
            print("2. View Class Attendance")
            print("3. Back")

            option = int(input("Enter your option: "))
            if option == 1:
                class_name = input("Enter class name: ")
                member_ids = list(map(int, input("Enter member IDs (space separated): ").split()))
                self.update_attendance(class_name, member_ids)
            elif option == 2:
                self.view_attendance()
            elif option == 3:
                break
            else:
                print("Invalid option.")

    def display_renewals_menu(self) -> None:
        while True:
            print("\n1. Renew Membership")
            print("2. View Membership Renewals")
            print("3. Back")

            option = int(input("Enter your option: "))
            if option == 1:
                member_id = int(input("Enter member ID: "))
                self.renew_membership(member_id)
            elif option == 2:
                self.view_renewals()
            elif option == 3:
                break
            else:
                print("Invalid option.")

    def display_lockers_menu(self) -> None:
        while True:
            print("\n1. Assign Locker")
            print("2. View Locker Assignments")
            print("3. Back")

            option = int(input("Enter your option: "))
            if option == 1:
                member_id = int(input("Enter member ID: "))
                locker_number = int(input("Enter locker number: "))
                self.assign_locker(member_id, locker_number)
            elif option == 2:
                self.view_lockers()
            elif option == 3:
                break
            else:
                print("Invalid option.")

    def display_menu(self) -> None:
        while True:
            print("\n1. Members")
            print("2. Membership Plans")
            print("3. Class Attendance")
            print("4. Membership Renewals")
            print("5. Locker Assignments")
            print("6. Exit")

            option = int(input("Enter your option: "))
            if option == 1:
                self.display_members_menu()
            elif option == 2:
                self.display_plans_menu()
            elif option == 3:
                self.display_attendance_menu()
            elif option == 4:
                self.display_renewals_menu()
            elif option == 5:
                self.display_lockers_menu()
            elif option == 6:
                break
            else:
                print("Invalid option.")


if __name__ == "__main__":
    member = Membership()
    member.display_menu()

```
