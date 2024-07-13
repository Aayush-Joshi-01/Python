import sys
from Controller.analysis_controller import AnalysisController
from Decorators.Logger_Analysis import logger_analysis
from Routes.analysis_url import route


class Interface:
    def __init__(self):
        self.controller = AnalysisController()

    @logger_analysis
    def display_menu(self):
        print("\nWelcome to Data Analysis Application")
        print("===================================")
        print("/descriptive for descriptive analysis")
        print("/comparative for comparative analysis")
        print("/temporal for temporal analysis")
        print("/spatial for spatial analysis")
        print("/behavioral for behavioral analysis")
        print("/health for health metrics analysis")
        print("/predictive for predictive analysis")
        print("/exit to exit the program")

    @logger_analysis
    def run(self):
        self.display_menu()
        while True:
            choice = input(
                "\nEnter your choice "
                "(descriptive/comparative/temporal/spatial/behavioral/health/predictive/exit): "
                           ).lower()
            if choice in ['n', 'no', 'non', 'faux']:
                print("Exiting the program...")
                sys.exit(0)

            route(choice.strip())
            menu_flag = input("Do you want to see the menu again: ")
            menu_flag = menu_flag.strip()
            if menu_flag.lower() in ['y', 'yes', 'true', 'oui', 'vrai']:
                self.display_menu()
            


if __name__ == "__main__":
    app = Interface()
    app.run()
