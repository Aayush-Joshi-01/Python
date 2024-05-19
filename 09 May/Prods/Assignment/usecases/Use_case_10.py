# You're designing a scheduling application for a busy office.
# Write a Python function to merge and sort two lists of appointments, ensuring the appointments are arranged chronologically.

import datetime

def merge_sort_appointments(appointments1, appointments2):
    merged_appointments = appointments1 + appointments2
    merged_appointments.sort(key=lambda x: x['start_time'])
    return merged_appointments

if __name__ == '__main__':
    appointments1 = [
        {'name': 'Meeting with John', 'start_time': datetime.datetime(2023, 3, 15, 10, 0),
         'end_time': datetime.datetime(2023, 3, 15, 11, 0)},
        {'name': 'Lunch with Sarah', 'start_time': datetime.datetime(2023, 3, 15, 12, 0),
         'end_time': datetime.datetime(2023, 3, 15, 13, 0)}
    ]

    appointments2 = [
        {'name': 'Call with Jane', 'start_time': datetime.datetime(2023, 3, 15, 9, 0),
         'end_time': datetime.datetime(2023, 3, 15, 9, 30)},
        {'name': 'Meeting with Bob', 'start_time': datetime.datetime(2023, 3, 15, 14, 0),
         'end_time': datetime.datetime(2023, 3, 15, 15, 0)}
    ]

    merged_appointments = merge_sort_appointments(appointments1, appointments2)
    for merged_appointment in merged_appointments:
        print(f"Merged appointments: {merged_appointment}")
