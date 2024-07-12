import sys
from Controller.analysis_controller import AnalysisController


class Interface:
    def __init__(self):
        self.controller = AnalysisController()

    def display_menu(self):
        print("\nWelcome to Data Analysis Application")
        print("===================================")
        print("1. Descriptive Analysis")
        print("2. Temporal Analysis")
        print("3. Comparative Analysis")
        print("4. Spatial Analysis")
        print("5. Behavioral Analysis")
        print("6. Health Metrics Analysis")
        print("7. Predictive Analysis")
        print("8. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ").strip()

            if choice == '1':
                self.controller.perform_descriptive_analysis()
            elif choice == '2':
                self.controller.perform_temporal_analysis()
            elif choice == '3':
                self.controller.perform_comparative_analysis()
            elif choice == '4':
                self.controller.perform_spatial_analysis()
            elif choice == '5':
                self.controller.perform_behavioral_analysis()
            elif choice == '6':
                self.controller.perform_health_metrics_analysis()
            elif choice == '7':
                self.controller.perform_predictive_analysis()
            elif choice == '8':
                print("Exiting the program. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    app = Interface()
    app.run()
