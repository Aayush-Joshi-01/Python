import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Dict
from Titanic_Analysis.load_data import data_structuring


class Financial_Controller:

    @staticmethod
    def ticket_fare_distribution(arr: np.ndarray) -> None:
        """
        Plot a histogram showing the distribution of ticket fares.
        """
        plt.hist(arr['fare'], bins=20, edgecolor='black')  # Plot histogram of ticket fares
        plt.xlabel('Fare')
        plt.ylabel('Frequency')
        plt.title('Ticket Fare Distribution')
        plt.show()  # Display the plot

    @staticmethod
    def average_fare_by_class(arr: np.ndarray) -> Dict[int, float]:
        """
        Calculate the average fare by passenger class.
        """
        pclasses = np.unique(arr['pclass'])  # Unique passenger classes
        average_fare_by_class: Dict[int, float] = {}
        for pclass in pclasses:
            mask = arr['pclass'] == pclass  # Mask for passengers in the current class
            average_fare = np.mean(arr['fare'][mask])  # Calculate average fare for this class
            average_fare_by_class[int(pclass)] = float(average_fare)  # Store average fare in dictionary
        return average_fare_by_class  # Return dictionary of average fares by class

    @staticmethod
    def fare_vs_survival(arr: np.ndarray) -> None:
        """
        Plot a boxplot comparing ticket fare distribution between survivors and non-survivors.
        """
        sns.boxplot(x=arr['survived'], y=arr['fare'])  # Plot boxplot of fare vs. survival
        plt.title('Fare vs. Survival')
        plt.show()  # Display the plot


if __name__ == '__main__':
    data = data_structuring()  # Load Titanic dataset using data_structuring function
    controller = Financial_Controller()  # Create an instance of Financial_Controller

    # Perform financial analyses using methods from Financial_Controller
    controller.ticket_fare_distribution(data)
    print("Average fare by class:", controller.average_fare_by_class(data))
    controller.fare_vs_survival(data)
