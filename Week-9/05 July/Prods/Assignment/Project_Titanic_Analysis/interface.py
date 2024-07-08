import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
from Titanic_Decorators.log_generator import titanic_logger
from Titanic_routes.url import route  # Assuming route function from Titanic_routes.url


@titanic_logger
def main():
    """
    Main function to provide a menu-driven interface for Titanic dataset analysis.
    """
    while True:
        print("\nTitanic Dataset Analysis Menu:")
        print("/survival for survival analysis")
        print("/demographic for demographic analysis")
        print("/finance for financial analysis")
        print("/class for class-based analysis")
        print("/additional for additional analysis")
        print("exit to exit")
        
        choice = input("\nEnter your URL choice with /: ")
        
        if choice == "exit":
            break
        
        route(choice)  # Call the route function to handle the chosen URL route


if __name__ == "__main__":
    main()
