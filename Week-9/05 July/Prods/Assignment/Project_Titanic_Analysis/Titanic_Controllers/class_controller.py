import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

from typing import Dict, Tuple


class Class_Controller:

    @staticmethod
    def passenger_demographics_by_class(arr: np.ndarray) -> Dict[int, Dict[str, int]]:
        class_demographics = {}
        for pclass in np.unique(arr['pclass']):
            mask = arr['pclass'] == pclass
            mean_age = np.mean(arr['age'][mask])
            sex_counts = dict(zip(*np.unique(arr['sex'][mask], return_counts=True)))
            class_demographics[int(pclass)] = {'mean_age': float(mean_age), 'sex_counts': sex_counts}
        return class_demographics

    @staticmethod
    def survival_rates_by_class_and_gender(arr: np.ndarray) -> Dict[Tuple[int, str], float]:
        survival_rates = {}
        for pclass in np.unique(arr['pclass']):
            mask_class = arr['pclass'] == pclass
            for sex in np.unique(arr['sex'][mask_class]):
                mask = np.logical_and(mask_class, arr['sex'] == sex)
                survival_rate = np.mean(arr['survived'][mask]) * 100
                survival_rates[(int(pclass), str(sex))] = float(survival_rate)
        return survival_rates

    @staticmethod
    def fare_analysis_by_class(arr: np.ndarray) -> None:
        sns.boxplot(x=arr['pclass'], y=arr['fare'])
        plt.title('Fare Analysis by Class')
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
    controller = Class_Controller()

    print("Passenger demographics by class:", controller.passenger_demographics_by_class(data))
    print("Survival rates by class and gender:", controller.survival_rates_by_class_and_gender(data))
    controller.fare_analysis_by_class(data)
