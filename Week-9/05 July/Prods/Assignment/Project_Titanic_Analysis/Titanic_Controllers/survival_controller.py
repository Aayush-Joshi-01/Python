import numpy as np
from typing import Dict, List
from Titanic_Analysis.load_data import data_structuring  # Loads the data for testing

class Survival_Controller:

    @staticmethod
    def overall_survival_rate(arr: np.ndarray) -> float:
        """
        Calculate the overall survival rate of passengers.

        Parameters:
        - arr (np.ndarray): Numpy array containing structured data of passengers.

        Returns:
        - float: Overall survival rate as a percentage.
        """
        survived_count = np.sum(arr['survived'])  # Count of passengers who survived (survived = 1)
        total_passengers = len(arr)  # Total number of passengers
        survival_rate = (survived_count / total_passengers) * 100  # Calculate survival rate as a percentage
        return float(survival_rate)  # Return the survival rate as a float

    @staticmethod
    def survival_by_class(arr: np.ndarray) -> Dict[int, float]:
        """
        Calculate survival rates by passenger class.

        Parameters:
        - arr (np.ndarray): Numpy array containing structured data of passengers.

        Returns:
        - Dict[int, float]: Dictionary where keys are passenger classes (integers) and values are survival rates (floats).
        """
        pclasses = np.unique(arr['pclass'])  # Unique passenger classes
        survival_by_class: Dict[int, float] = {}
        for pclass in pclasses:
            mask = arr['pclass'] == pclass  # Mask for passengers in the current class
            survival_rate = np.mean(arr['survived'][mask]) * 100  # Calculate survival rate for this class
            survival_by_class[int(pclass)] = float(survival_rate)  # Store survival rate in dictionary
        return survival_by_class  # Return dictionary of survival rates by class

    @staticmethod
    def survival_by_gender(arr: np.ndarray) -> Dict[str, float]:
        """
        Calculate survival rates by gender.

        Parameters:
        - arr (np.ndarray): Numpy array containing structured data of passengers.

        Returns:
        - Dict[str, float]: Dictionary where keys are genders (strings) and values are survival rates (floats).
        """
        genders = np.unique(arr['sex'])  # Unique genders (assuming 'sex' is binary)
        survival_by_gender: Dict[str, float] = {}
        for gender in genders:
            mask = arr['sex'] == gender  # Mask for passengers of the current gender
            survival_rate = np.mean(arr['survived'][mask]) * 100  # Calculate survival rate for this gender
            survival_by_gender[str(gender)] = float(survival_rate)  # Store survival rate in dictionary
        return survival_by_gender  # Return dictionary of survival rates by gender

    @staticmethod
    def survival_by_age_group(arr: np.ndarray, bins: List[int] = [0, 18, 30, 50, 100]) -> Dict[str, float]:
        """
        Calculate survival rates by age group.

        Parameters:
        - arr (np.ndarray): Numpy array containing structured data of passengers.
        - bins (List[int]): List of integers defining the bins for age groups (default: [0, 18, 30, 50, 100]).

        Returns:
        - Dict[str, float]: Dictionary where keys are age group labels (strings) and values are survival rates (floats).
        """
        age_groups = ['0-18', '19-30', '31-50', '51+']  # Define age groups
        age_labels = np.digitize(arr['age'], bins=bins, right=True)  # Assign each passenger to an age group
        survival_by_age_group: Dict[str, float] = {}
        for i, label in enumerate(age_labels):
            group_name = age_groups[label - 1]  # Determine age group name
            if group_name not in survival_by_age_group:
                survival_by_age_group[group_name] = []
            survival_by_age_group[group_name].append(arr['survived'][i])  # Append survival status to age group
        for group, survivals in survival_by_age_group.items():
            survival_by_age_group[group] = float(np.mean(survivals) * 100)  # Calculate survival rate for each age group
        return survival_by_age_group  # Return dictionary of survival rates by age group

    @staticmethod
    def survival_by_family_size(arr: np.ndarray) -> Dict[int, float]:
        """
        Calculate survival rates by family size.

        Parameters:
        - arr (np.ndarray): Numpy array containing structured data of passengers.

        Returns:
        - Dict[int, float]: Dictionary where keys are family sizes (integers) and values are survival rates (floats).
        """
        family_sizes = np.array(arr['sibsp'] + arr['parch'] + 1)  # Calculate total family size for each passenger
        unique_sizes = np.unique(family_sizes)  # Unique family sizes
        survival_by_family_size: Dict[int, float] = {}
        for size in unique_sizes:
            mask = family_sizes == size  # Mask for passengers with the current family size
            survival_rate = np.mean(arr['survived'][mask]) * 100  # Calculate survival rate for this family size
            survival_by_family_size[int(size)] = float(survival_rate)  # Store survival rate in dictionary
        return survival_by_family_size  # Return dictionary of survival rates by family size

if __name__ == '__main__':
    # Main execution part
    data = data_structuring()  # Load Titanic dataset using data_structuring function
    controller = Survival_Controller()  # Create an instance of Survival_Controller

    # Print various survival statistics using methods from Survival_Controller
    print("Overall survival rate:", controller.overall_survival_rate(data))
    print("Survival by class:", controller.survival_by_class(data))
    print("Survival by gender:", controller.survival_by_gender(data))
    print("Survival by age group:", controller.survival_by_age_group(data))
    print("Survival by family size:", controller.survival_by_family_size(data))
