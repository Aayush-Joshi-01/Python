import numpy as np
import matplotlib.pyplot as plt
from typing import Dict
from Titanic_Analysis.load_data import data_structuring  # Loads the data for testing

class Demographic_Controller:

    @staticmethod
    def passenger_count_by_class(arr: np.ndarray) -> Dict[int, int]:
        """
        Calculate the count of passengers by passenger class.

        Parameters:
        - arr (np.ndarray): Numpy array containing structured data of passengers.

        Returns:
        - Dict[int, int]: Dictionary where keys are passenger classes (integers) and values are passenger counts (integers).
        """
        class_counts = np.bincount(arr['pclass'])  # Count occurrences of each passenger class
        passenger_count_by_class: Dict[int, int] = {}
        for pclass in np.unique(arr['pclass']):
            passenger_count_by_class[int(pclass)] = int(class_counts[pclass])
        return passenger_count_by_class  # Return dictionary of passenger counts by class

    @staticmethod
    def gender_distribution(arr: np.ndarray) -> Dict[str, int]:
        """
        Calculate the distribution of passengers by gender.

        Parameters:
        - arr (np.ndarray): Numpy array containing structured data of passengers.

        Returns:
        - Dict[str, int]: Dictionary where keys are genders (strings) and values are counts of passengers of each gender (integers).
        """
        gender_counts = dict(zip(*np.unique(arr['sex'], return_counts=True)))  # Count occurrences of each gender
        return gender_counts  # Return dictionary of gender distribution

    @staticmethod
    def age_distribution(arr: np.ndarray) -> None:
        """
        Display a histogram showing the age distribution of passengers.

        Parameters:
        - arr (np.ndarray): Numpy array containing structured data of passengers.

        Returns:
        - None
        """
        plt.hist(arr['age'], bins=20, edgecolor='black')  # Plot histogram of passenger ages
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.title('Age Distribution of Passengers')
        plt.show()  # Display the plot

    @staticmethod
    def embarkation_port_analysis(arr: np.ndarray) -> Dict[str, int]:
        """
        Analyze the count of passengers embarked from each port.

        Parameters:
        - arr (np.ndarray): Numpy array containing structured data of passengers.

        Returns:
        - Dict[str, int]: Dictionary where keys are embarkation ports (strings) and values are counts of passengers embarked from each port (integers).
        """
        embarkation_port_counts = dict(zip(*np.unique(arr['embarked'], return_counts=True)))  # Count occurrences of each embarkation port
        return embarkation_port_counts  # Return dictionary of embarkation port counts

if __name__ == '__main__':
    data = data_structuring()  # Load Titanic dataset using data_structuring function
    controller = Demographic_Controller()  # Create an instance of Demographic_Controller

    # Print various demographic statistics using methods from Demographic_Controller
    print("Passenger count by class:", controller.passenger_count_by_class(data))
    print("Gender distribution:", controller.gender_distribution(data))
    controller.age_distribution(data)
    print("Embarkation port analysis:", controller.embarkation_port_analysis(data))
