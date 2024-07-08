import numpy as np
import csv
from typing import Dict, List, Tuple


class Additonal_Controller:

    @staticmethod
    def family_relationships_and_survival(self, arr: np.ndarray) -> Dict[int, float]:
        family_sizes = arr['sibsp'] + arr['parch'] + 1
        unique_sizes = np.unique(family_sizes)
        family_survival: Dict[int, float] = {}
        for size in unique_sizes:
            mask = family_sizes == size
            survival_rate = np.mean(arr['survived'][mask]) * 100
            family_survival[int(size)] = float(survival_rate)
        return family_survival

    @staticmethod
    def survival_rate_by_category(self, data: np.ndarray, category_col: str) -> List[Tuple[str, float]]:
        categories = np.unique(data[category_col])
        survival_rates: List[Tuple[str, float]] = []
        for category in categories:
            total_passengers = np.sum(data[category_col] == category)
            if total_passengers == 0:
                continue
            survived_passengers = np.sum((data[category_col] == category) & (data['survived'] == 1))
            survival_rate = survived_passengers / total_passengers
            survival_rates.append((str(category), float(survival_rate)))
        return survival_rates


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
    controller = Additonal_Controller()

    print("Family relationships and survival:", controller.family_relationships_and_survival(data))
    print("Survival rate by category:", controller.survival_rate_by_category(data, 'sex'))
    print("Survival rate by category:", controller.survival_rate_by_category(data, 'pclass'))
    print("Survival rate by category:", controller.survival_rate_by_category(data, 'embarked'))
    print("Survival rate by category:", controller.survival_rate_by_category(data, 'home_dest'))
    print("Survival rate by category:", controller.survival_rate_by_category(data, 'boat'))
