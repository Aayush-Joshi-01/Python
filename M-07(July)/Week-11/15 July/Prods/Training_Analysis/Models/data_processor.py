from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from Utils.plot_utils import PlotUtils
from Utils.data_utils import DataUtils

from Decorators.Logger_Analysis import analysis_logger


class DataProcessor:
    def __init__(self):
        self.plot_utils = PlotUtils()
        self.data_utils = DataUtils()
        self.steps_model = None
        self.hr_model = None
        self.mood_model = None
        self.label_encoders = {}

    @analysis_logger
    def load_data(self):
        # Example: Load data using DataLoader (assumed to be implemented)
        from data_loader import DataLoader
        loader = DataLoader()
        return loader.load_data()

    @analysis_logger
    def preprocess_data(self, data):
        # Preprocess data using DataUtils
        preprocessed_data = self.data_utils.preprocess_data(data)
        return preprocessed_data

    @analysis_logger
    def calculate_basic_statistics(self, data):
        # Calculate basic statistics
        basic_stats = data.describe()
        print("\nBasic Statistics:")
        print(basic_stats)

        # Save summary statistics as CSV
        basic_stats.to_csv('Reports/statistical_summaries/basic_statistics.csv', index=True)

        # Generate report
        report_text = f"Basic Statistics:\n\n{basic_stats.to_string()}"
        self.save_report(report_text, 'basic_statistics')

    
    @analysis_logger
    def save_report(self, report_text, filename):
        # Save report as text file
        with open(f'Reports/insight_reports/{filename}.txt', 'w') as file:
            file.write(f"{datetime.datetime.now()} \n \n {report_text}")
        print(f"Report '{filename}.txt' saved successfully.")


if __name__ == "__main__":
    processor = DataProcessor()
    data = processor.load_data()
    if data is not None:
        preprocessed_data = processor.preprocess_data(data)
        processor.calculate_basic_statistics(preprocessed_data)
