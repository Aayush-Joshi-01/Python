import numpy as np
import matplotlib.pyplot as plt
import csv
from typing import Dict


class Demographic_Controller:

    @staticmethod
    def passenger_count_by_class(arr: np.ndarray) -> Dict[int, int]:
        class_counts = np.bincount(arr['pclass'])
        passenger_count_by_class: Dict[int, int] = {}
        for pclass in np.unique(arr['pclass']):
            passenger_count_by_class[int(pclass)] = int(class_counts[pclass])
        return passenger_count_by_class

    @staticmethod
    def gender_distribution(self, arr: np.ndarray) -> Dict[str, int]:
        gender_counts = dict(zip(*np.unique(arr['sex'], return_counts=True)))
        return gender_counts

    @staticmethod
    def age_distribution(self, arr: np.ndarray) -> None:
        plt.hist(arr['age'], bins=20, edgecolor='black')
        plt.xlabel('Age')
        plt.title('Age Distribution of Passengers')
        plt.show()

    @staticmethod
    def embarkation_port_analysis(self, arr: np.ndarray) -> Dict[str, int]:
        embarkation_port_counts = dict(zip(*np.unique(arr['embarked'], return_counts=True)))
        return embarkation_port_counts


def data_structuring():
        dtype = np.dtype([
        ('pclass', int),
        ('survived', int),
        ('name', 'U50'),
        ('sex', 'U10'),
        ('age', float),
        ('sibsp', int),
        ('parch', int),
        ('ticket', 'U20'),
        ('fare', float),
        ('cabin', 'U20'),
        ('embarked', 'U1'),
        ('boat', 'U10'),
        ('body', float),
        ('home_dest', 'U50')
        ])
        data = []
        with open('Week-9/05 July/Prods/Assignment/Project_Titanic_Analysis/Titanic_CSV/titanic3.csv', 'r') as file:
            read = csv.reader(file)
            next(read)
            for row in read:
                try:
                    cleaned_row = [col if col else '0' for col in row]
                    data.append(tuple(cleaned_row))
                except ValueError as e:
                    print(f"Error processing row: {row}, Error: {e}")
        structured_data = np.array(data, dtype=dtype)
        return structured_data


if __name__ == '__main__':
    data = data_structuring()
    controller = Demographic_Controller()

    print("Passenger count by class:", controller.passenger_count_by_class(data))
    print("Gender distribution:", controller.gender_distribution(data))
    controller.age_distribution(data)
    print("Embarkation port analysis:", controller.embarkation_port_analysis(data))