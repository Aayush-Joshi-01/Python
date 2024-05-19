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
