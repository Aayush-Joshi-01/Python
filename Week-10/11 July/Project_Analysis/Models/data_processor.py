import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .plot_utils import PlotUtils
from Utils.data_utils import DataUtils  # Import DataUtils


class DataProcessor:
    def __init__(self):
        self.plot_utils = PlotUtils()
        self.data_utils = DataUtils()  # Initialize DataUtils

    def load_data(self):
        # Example: Load data using DataLoader (assumed to be implemented)
        from data_loader import DataLoader
        loader = DataLoader()
        return loader.load_data()

    def preprocess_data(self, data):
        # Preprocess data using DataUtils
        preprocessed_data = self.data_utils.preprocess_data(data)
        return preprocessed_data

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

    def plot_data_distribution(self, data):
        # Plot distributions for numerical columns
        numerical_cols = data.select_dtypes(include=['int', 'float']).columns
        for col in numerical_cols:
            self.plot_utils.plot_histogram(data, col)

    def analyze_trends_over_time(self, data):
        # Example: Analyze trends in steps over time
        data['date'] = pd.to_datetime(data['date'])
        data.set_index('date', inplace=True)
        steps_daily = data['steps'].resample('D').sum()  # Resample daily and sum steps
        self.plot_utils.plot_line_chart(steps_daily.index, steps_daily.values, 'Date', 'Steps', 'Daily Steps Trend')

        # Generate report
        report_text = "Trends Over Time: Daily Steps Trend\n\nAnalyzing trends in steps over time..."
        self.save_report(report_text, 'daily_steps_trend')

    def identify_seasonal_patterns(self, data):
        # Example: Identify seasonal patterns in steps
        data['month'] = pd.to_datetime(data['date']).dt.month
        monthly_avg_steps = data.groupby('month')['steps'].mean()
        self.plot_utils.plot_line_chart(monthly_avg_steps.index, monthly_avg_steps.values, 'Month', 'Average Steps',
                                        'Monthly Average Steps')

        # Generate report
        report_text = "Seasonal Patterns: Monthly Average Steps\n\nIdentifying seasonal patterns in steps..."
        self.save_report(report_text, 'monthly_average_steps')

    def compare_groups(self, data):
        # Example: Compare average calories burned by workout type
        avg_calories_by_workout = data.groupby('workout_type')['calories_burned'].mean().sort_values()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=avg_calories_by_workout.index, y=avg_calories_by_workout.values, palette='viridis')
        plt.title('Average Calories Burned by Workout Type')
        plt.xlabel('Workout Type')
        plt.ylabel('Average Calories Burned')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('Reports/visualizations/average_calories_by_workout_type.png')
        plt.show()

        # Generate report
        report_text = "Comparative Analysis: Average Calories Burned by Workout Type\n\nComparing average calories burned across different workout types..."
        self.save_report(report_text, 'average_calories_by_workout_type')

    def correlation_analysis(self, data):
        # Example: Perform correlation analysis between numerical variables
        numerical_data = data.select_dtypes(include=['int', 'float'])
        correlation_matrix = numerical_data.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Correlation Matrix of Numerical Variables')
        plt.savefig('Reports/visualizations/correlation_matrix.png')
        plt.show()

        # Generate report
        report_text = "Correlation Analysis: Numerical Variables\n\nAnalyzing correlations between numerical variables..."
        self.save_report(report_text, 'correlation_analysis')

    def analyze_location_based_insights(self, data):
        # Example: Analyze activity levels across different locations
        avg_steps_by_location = data.groupby('location')['steps'].mean().sort_values()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=avg_steps_by_location.index, y=avg_steps_by_location.values, palette='Set2')
        plt.title('Average Steps by Location')
        plt.xlabel('Location')
        plt.ylabel('Average Steps')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('Reports/visualizations/average_steps_by_location.png')
        plt.show()

        # Generate report
        report_text = "Spatial Analysis: Average Steps by Location\n\nAnalyzing average steps across different locations..."
        self.save_report(report_text, 'average_steps_by_location')

    def map_activities(self, data):
        # Example: Map activities based on location
        plt.figure(figsize=(12, 8))
        sns.scatterplot(x='location', y='steps', hue='workout_type', data=data, palette='Set2', s=100)
        plt.title('Activities by Location')
        plt.xlabel('Location')
        plt.ylabel('Steps')
        plt.xticks(rotation=45)
        plt.legend(title='Workout Type')
        plt.tight_layout()
        plt.savefig('Reports/visualizations/activities_by_location.png')
        plt.show()

        # Generate report
        report_text = "Spatial Analysis: Activities by Location\n\nMapping activities based on location..."
        self.save_report(report_text, 'activities_by_location')

    def analyze_activity_patterns(self, data):
        # Example: Analyze daily activity patterns
        data['weekday'] = pd.to_datetime(data['date']).dt.day_name()
        avg_steps_by_day = data.groupby('weekday')['steps'].mean().reindex(
            ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=avg_steps_by_day.index, y=avg_steps_by_day.values, marker='o', linestyle='-', color='b')
        plt.title('Average Steps by Day of Week')
        plt.xlabel('Day of Week')
        plt.ylabel('Average Steps')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('Reports/visualizations/average_steps_by_day.png')
        plt.show()

        # Generate report
        report_text = "Behavioral Analysis: Average Steps by Day of Week\n\nAnalyzing average steps by day of the week..."
        self.save_report(report_text, 'average_steps_by_day')

    def analyze_impact_of_weather(self, data):
        # Example: Analyze impact of weather conditions on activity levels
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='weather_conditions', y='steps', data=data, palette='Set2')
        plt.title('Impact of Weather Conditions on Steps')
        plt.xlabel('Weather Conditions')
        plt.ylabel('Steps')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('Reports/visualizations/impact_of_weather_on_steps.png')
        plt.show()

        # Generate report
        report_text = "Behavioral Analysis: Impact of Weather Conditions on Steps\n\nAnalyzing the impact of weather conditions on activity levels..."
        self.save_report(report_text, 'impact_of_weather_on_steps')

    def study_health_impact_of_activity(self, data):
        # Example: Study health impact of activity on heart rate
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='steps', y='heart_rate_avg', hue='mood', data=data, palette='Set2', s=100)
        plt.title('Health Impact of Activity on Heart Rate')
        plt.xlabel('Steps')
        plt.ylabel('Average Heart Rate')
        plt.xticks(rotation=45)
        plt.legend(title='Mood')
        plt.tight_layout()
        plt.savefig('Reports/visualizations/health_impact_of_activity.png')
        plt.show()

        # Generate report
        report_text = "Health Metrics Analysis: Health Impact of Activity on Heart Rate\n\nStudying the impact of activity on average heart rate..."
        self.save_report(report_text, 'health_impact_of_activity')

    def analyze_heart_rate(self, data):
        # Example: Analyze average heart rate during different activities
        avg_heart_rate_by_activity = data.groupby('workout_type')['heart_rate_avg'].mean().sort_values()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=avg_heart_rate_by_activity.index, y=avg_heart_rate_by_activity.values, palette='viridis')
        plt.title('Average Heart Rate by Activity Type')
        plt.xlabel('Activity Type')
        plt.ylabel('Average Heart Rate')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('Reports/visualizations/average_heart_rate_by_activity.png')
        plt.show()

        # Generate report
        report_text = "Health Metrics Analysis: Average Heart Rate by Activity Type\n\nAnalyzing average heart rate during different activities..."
        self.save_report(report_text, 'average_heart_rate_by_activity')

    def build_prediction_models(self, data):
        # Example: Build prediction models for future steps
        # (This is a placeholder for implementing machine learning models if needed)
        pass

    def forecast_trends(self, data):
        # Example: Forecast trends in activity based on historical data
        pass

    def save_report(self, report_text, filename):
        # Save report as text file
        with open(f'Reports/insight_reports/{filename}.txt', 'w') as file:
            file.write(report_text)
        print(f"Report '{filename}.txt' saved successfully.")


if __name__ == "__main__":
    processor = DataProcessor()
    data = processor.load_data()
    if data is not None:
        preprocessed_data = processor.preprocess_data(data)
        processor.calculate_basic_statistics(preprocessed_data)
        processor.plot_data_distribution(preprocessed_data)
        processor.analyze_trends_over_time(preprocessed_data)
        processor.compare_groups(preprocessed_data)
