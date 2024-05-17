class AppointmentNotFoundException(Exception):
    pass

class Calendar:
    def __init__(self):
        self.appointments = {}

    def schedule_appointment(self, date, time, description):
        if date not in self.appointments:
            self.appointments[date] = []
        self.appointments[date].append({'time': time, 'description': description})
        print("Appointment scheduled successfully.")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            print("Appointments:")
            for date, appointments in self.appointments.items():
                print(f"On {date}:")
                for appointment in appointments:
                    print(f"Time: {appointment['time']}, Description: {appointment['description']}")

    def cancel_appointment(self, date, time):
        if date not in self.appointments or {'time': time} not in self.appointments[date]:
            raise AppointmentNotFoundException("Appointment not scheduled.")
        self.appointments[date] = [app for app in self.appointments[date] if app['time'] != time]
        if not self.appointments[date]:
            del self.appointments[date]
        print("Appointment canceled successfully.")

def main():
    calendar = Calendar()

    while True:
        print("\nCalendar Application:")
        print("1. Schedule Appointment")
        print("2. View Appointments")
        print("3. Cancel Appointment")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD) of the appointment: ")
            time = input("Enter the time (HH:MM) of the appointment: ")
            description = input("Enter a description for the appointment: ")
            calendar.schedule_appointment(date, time, description)
        elif choice == '2':
            calendar.view_appointments()
        elif choice == '3':
            try:
                date = input("Enter the date (YYYY-MM-DD) of the appointment to cancel: ")
                time = input("Enter the time (HH:MM) of the appointment to cancel: ")
                calendar.cancel_appointment(date, time)
            except AppointmentNotFoundException as e:
                print(e)
        elif choice == '4':
            print("Exiting the calendar application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
