# Data Analysis Application

This application is designed for performing various types of data analysis on a dataset using Python. It provides functionalities for descriptive analysis, temporal analysis, comparative analysis, spatial analysis, behavioral analysis, health metrics analysis, and optionally, predictive analysis.

## Project Structure

```
/Project_Analysis
    ├── README.md                # Project overview and instructions
    ├── interface.py             # CLI-based interface for data analysis
    ├── Controllers/
    │   └── analysis_controller.py  # Controller for data analysis methods
    ├── Models/
    │   ├── data_loader.py       # Module for loading data
    │   ├── data_processor.py    # Module for processing data
    │   └── plot_utils.py        # Utility module for plotting data
    ├── Utils/
    │   └── requirements.txt     # Required libraries for the project
    └── Reports/
        └── analysis_reports.md  # Generated reports from data analysis
```

## Setup and Installation

### Prerequisites

- Python 3.x installed on your system.
- `virtualenv` package installed (install using `pip install virtualenv` if not installed).

### Setup

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd Project_Analysis
   ```

2. **Create and activate virtual environment:**

   ```bash
   # Create a virtual environment
   virtualenv .venv

   # Activate the virtual environment
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r Utils/requirements.txt
   ```

### Usage

1. **Run the CLI interface:**

   ```bash
   python interface.py
   ```

2. **Follow the prompts to select the type of analysis you want to perform:**

   - The interface will display a menu with options for different types of data analysis.
   - Choose an option (1-8) to initiate the corresponding analysis.

3. **View the results:**

   - Results will be displayed in the console, and plots (if any) will be generated using Matplotlib and Seaborn.

### Example

```python
# Example usage in interface.py

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
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    app = Interface()
    app.run()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data loading and preprocessing techniques inspired by [Pandas](https://pandas.pydata.org/).
- Visualization powered by [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/).
