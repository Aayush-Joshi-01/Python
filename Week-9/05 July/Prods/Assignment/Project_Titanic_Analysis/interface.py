import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv

from Titanic_routes.url import route


def main():
    while True:
        print("\nTitanic Dataset Analysis Menu:")
        print("/survival for survival analysis")
        print("/demographic for demographic analysis")
        print("/finance for financial analysis")
        print("/class for class based analysis")
        print("/additional for additional analysis")
        print("exit to exit")
        choice = input("\nEnter your Url Choice with / : ")
        if choice == "exit":
            break
        route(choice)


if __name__ == "__main__":
    main()
