import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from typing import Dict, Tuple, Any
from Titanic_Analysis.load_data import data_structuring


class Class_Controller:

    @staticmethod
    def passenger_demographics_by_class(arr: np.ndarray) -> Dict[int, Dict[str, Dict[Any, Any] | float]]:
        """
        Calculate passenger demographics (mean age and sex counts) by passenger class.
        """
        class_demographics = {}
        for pclass in np.unique(arr['pclass']):  # Iterate over unique passenger classes
            mask = arr['pclass'] == pclass  # Mask for passengers in the current class
            mean_age = np.mean(arr['age'][mask])  # Calculate mean age for this class
            sex_counts = dict(
                zip(*np.unique(arr['sex'][mask], return_counts=True)))  # Calculate sex counts for this class
            class_demographics[int(pclass)] = {'mean_age': float(mean_age),
                                               'sex_counts': sex_counts}  # Store results in dictionary
        return class_demographics  # Return dictionary of passenger demographics by class

    @staticmethod
    def survival_rates_by_class_and_gender(arr: np.ndarray) -> Dict[Tuple[int, str], float]:
        """
        Calculate survival rates by passenger class and gender.
        """
        survival_rates = {}
        for pclass in np.unique(arr['pclass']):  # Iterate over unique passenger classes
            mask_class = arr['pclass'] == pclass  # Mask for passengers in the current class
            for sex in np.unique(arr['sex'][mask_class]):  # Iterate over unique genders in this class
                mask = np.logical_and(mask_class,
                                      arr['sex'] == sex)  # Mask for passengers of the current gender in this class
                survival_rate = np.mean(
                    arr['survived'][mask]) * 100  # Calculate survival rate for this class and gender
                survival_rates[(int(pclass), str(sex))] = float(survival_rate)  # Store survival rate in dictionary
        return survival_rates  # Return dictionary of survival rates by class and gender

    @staticmethod
    def fare_analysis_by_class(arr: np.ndarray) -> None:
        """
        Perform fare analysis by passenger class and visualize with a boxplot.
        """
        sns.boxplot(x=arr['pclass'], y=arr['fare'])  # Create a boxplot of fare by passenger class using Seaborn
        plt.title('Fare Analysis by Class')  # Set plot title
        plt.show()  # Display the plot


if __name__ == '__main__':
    data = data_structuring()  # Load Titanic dataset using data_structuring function
    controller = Class_Controller()  # Create an instance of Class_Controller

    # Print results of different analyses using methods from Class_Controller
    print("Passenger demographics by class:", controller.passenger_demographics_by_class(data))
    print("Survival rates by class and gender:", controller.survival_rates_by_class_and_gender(data))
    controller.fare_analysis_by_class(data)  # Visualize fare analysis by class using Seaborn
