import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv
from typing import Dict


class Financial_Controller:

    @staticmethod
    def ticket_fare_distribution(arr: np.ndarray) -> None:
        plt.hist(arr['fare'], bins=20, edgecolor='black')
        plt.xlabel('Fare')
        plt.title('Ticket Fare Distribution')
        plt.show()

    @staticmethod
    def average_fare_by_class(arr: np.ndarray) -> Dict[int, float]:
        pclasses = np.unique(arr['pclass'])
        average_fare_by_class: Dict[int, float] = {}
        for pclass in pclasses:
            mask = arr['pclass'] == pclass
            average_fare = np.mean(arr['fare'][mask])
            average_fare_by_class[int(pclass)] = float(average_fare)
        return average_fare_by_class

    @staticmethod
    def fare_vs_survival(arr: np.ndarray) -> None:
        sns.boxplot(x=arr['survived'], y=arr['fare'])
        plt.title('Fare vs. Survival')
        plt.show()


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
    controller = Financial_Controller()
    controller.ticket_fare_distribution(data)
    print("Average fare by class:", controller.average_fare_by_class(data))
    controller.fare_vs_survival(data)
