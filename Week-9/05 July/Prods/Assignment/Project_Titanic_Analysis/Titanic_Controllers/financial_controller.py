import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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


if __name__ == '__main__':
    controller = Financial_Controller()


    controller.ticket_fare_distribution(data)
    print("Average fare by class:", controller.average_fare_by_class(data))
    controller.fare_vs_survival(data)