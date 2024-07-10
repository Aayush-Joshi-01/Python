import pandas as pd
import numpy as np
import csv

dtype = np.dtype([
    ('pclass', int),  # Passenger class
    ('survived', int),  # Survival (0 = No, 1 = Yes)
    ('name', 'U50'),  # Passenger name
    ('sex', 'U10'),  # Passenger sex
    ('age', float),  # Passenger age
    ('sibsp', int),  # Number of siblings/spouses aboard
    ('parch', int),  # Number of parents/children aboard
    ('ticket', 'U20'),  # Ticket number
    ('fare', float),  # Passenger fare
    ('cabin', 'U20'),  # Cabin number
    ('embarked', 'U1'),  # Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)
    ('boat', 'U10'),  # Lifeboat (if survived)
    ('body', float),  # Body number (if did not survive and body was recovered)
    ('home_dest', 'U50')  # Home/Destination
])


def data_structuring():
    data = []

    # Open the CSV file for reading
    #
    #
    # Insert your own relative path from Titanic_CSV
    #
    #
    with open('Week-9/05 July/Prods/Assignment/Project_Titanic_Analysis/Titanic_CSV/titanic3.csv', 'r') as file:
        read = csv.reader(file)

        # Skip the header row
        next(read)

        # Iterate over each row in the CSV
        for row in read:
            try:
                # Clean each column in the row, replace empty values with '0'
                cleaned_row = [col if col else '0' for col in row]

                # Convert the cleaned row into a tuple and append to data list
                data.append(tuple(cleaned_row))

            except ValueError as e:
                # If there's an error converting values, print an error message
                print(f"Error processing row: {row}, Error: {e}")

    # Convert the list of tuples into a structured numpy array using defined dtype
    structured_data = np.array(data, dtype=dtype)
    return structured_data


if __name__ == '__main__':
    print(data_structuring())
