import numpy as np
import csv
from typing import Dict, List, Tuple
from Titanic_Analysis.load_data import data_structuring # Loads the data for testing

class Additonal_Controller:

    @staticmethod
    def family_relationships_and_survival(arr: np.ndarray) -> Dict[int, float]:
        """
        Calculate survival rates based on family relationships (sibsp + parch + 1).
        
        Parameters:
        arr (np.ndarray): Numpy structured array containing Titanic dataset.

        Returns:
        Dict[int, float]: Dictionary where keys are family sizes and values are survival rates (%).
        """
        family_sizes = arr['sibsp'] + arr['parch'] + 1  # Calculate family sizes for each passenger
        unique_sizes = np.unique(family_sizes)  # Unique family sizes
        family_survival: Dict[int, float] = {}
        for size in unique_sizes:
            mask = family_sizes == size  # Mask for passengers with the current family size
            survival_rate = np.mean(arr['survived'][mask]) * 100  # Calculate survival rate for this family size
            family_survival[int(size)] = float(survival_rate)  # Store survival rate in dictionary
        return family_survival  # Return dictionary of survival rates by family size

    @staticmethod
    def survival_rate_by_category(data: np.ndarray, category_col: str) -> List[Tuple[str, float]]:
        """
        Calculate survival rates by a categorical column in the dataset.
        
        Parameters:
        data (np.ndarray): Numpy structured array containing Titanic dataset.
        category_col (str): Name of the column in the dataset to group by.

        Returns:
        List[Tuple[str, float]]: List of tuples where each tuple contains a category and its survival rate (%).
        """
        categories = np.unique(data[category_col])  # Unique categories in the specified column
        survival_rates: List[Tuple[str, float]] = []
        for category in categories:
            total_passengers = np.sum(data[category_col] == category)  # Total passengers in this category
            if total_passengers == 0:
                continue
            survived_passengers = np.sum((data[category_col] == category) & (data['survived'] == 1))  # Survived passengers in this category
            survival_rate = survived_passengers / total_passengers  # Calculate survival rate
            survival_rates.append((str(category), float(survival_rate)))  # Append category and survival rate to list
        return survival_rates  # Return list of tuples with category and survival rate

if __name__ == '__main__':
    data = data_structuring()  # Load Titanic dataset using data_structuring function
    controller = Additonal_Controller()  # Create an instance of Additonal_Controller

    # Print results of different survival rate calculations using methods from Additonal_Controller
    print("Family relationships and survival:", controller.family_relationships_and_survival(data))
    print("Survival rate by category (sex):", controller.survival_rate_by_category(data, 'sex'))
    print("Survival rate by category (pclass):", controller.survival_rate_by_category(data, 'pclass'))
    print("Survival rate by category (embarked):", controller.survival_rate_by_category(data, 'embarked'))
    print("Survival rate by category (home_dest):", controller.survival_rate_by_category(data, 'home_dest'))
    print("Survival rate by category (boat):", controller.survival_rate_by_category(data, 'boat'))
