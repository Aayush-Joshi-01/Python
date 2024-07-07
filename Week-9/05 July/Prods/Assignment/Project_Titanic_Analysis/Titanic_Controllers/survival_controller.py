import numpy as np
import csv
from typing import Dict, List, Tuple
# from ..Titanic_Analysis.load_data import data_structuring

class Survival_Controller:

    @staticmethod
    def overall_survival_rate(arr: np.ndarray) -> float:
        survived_count = np.sum(arr['survived'])
        total_passengers = len(arr)
        survival_rate = (survived_count / total_passengers) * 100
        return float(survival_rate)

    @staticmethod
    def survival_by_class(arr: np.ndarray) -> Dict[int, float]:
        pclasses = np.unique(arr['pclass'])
        survival_by_class: Dict[int, float] = {}
        for pclass in pclasses:
            mask = arr['pclass'] == pclass
            survival_rate = np.mean(arr['survived'][mask]) * 100
            survival_by_class[int(pclass)] = float(survival_rate)
        return survival_by_class

    @staticmethod
    def survival_by_gender(arr: np.ndarray) -> Dict[str, float]:
        genders = np.unique(arr['sex'])
        survival_by_gender: Dict[str, float] = {}
        for gender in genders:
            mask = arr['sex'] == gender
            survival_rate = np.mean(arr['survived'][mask]) * 100
            survival_by_gender[str(gender)] = float(survival_rate)
        return survival_by_gender

    @staticmethod
    def survival_by_age_group(arr: np.ndarray, bins: List[int] = [0, 18, 30, 50, 100]) -> Dict[str, float]:
        age_groups = ['0-18', '19-30', '31-50', '51+']
        age_labels = np.digitize(arr['age'], bins=bins, right=True)
        survival_by_age_group: Dict[str, float] = {}
        for i, label in enumerate(age_labels):
            group_name = age_groups[label - 1]
            if group_name not in survival_by_age_group:
                survival_by_age_group[group_name] = []
            survival_by_age_group[group_name].append(arr['survived'][i])
        
        for group, survivals in survival_by_age_group.items():
            survival_by_age_group[group] = float(np.mean(survivals) * 100)
        
        return survival_by_age_group

    @staticmethod
    def survival_by_family_size(arr: np.ndarray) -> Dict[int, float]:
        family_sizes = np.array(arr['sibsp'] + arr['parch'] + 1)
        unique_sizes = np.unique(family_sizes)
        survival_by_family_size: Dict[int, float] = {}
        for size in unique_sizes:
            mask = family_sizes == size
            survival_rate = np.mean(arr['survived'][mask]) * 100
            survival_by_family_size[int(size)] = float(survival_rate)
        return survival_by_family_size


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
    controller = Survival_Controller()

    print("Overall survival rate:", controller.overall_survival_rate(data))
    print("Survival by class:", controller.survival_by_class(data))
    print("Survival by gender:", controller.survival_by_gender(data))
    print("Survival by age group:", controller.survival_by_age_group(data))
    print("Survival by family size:", controller.survival_by_family_size(data))
