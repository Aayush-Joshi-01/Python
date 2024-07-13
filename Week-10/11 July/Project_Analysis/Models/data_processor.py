from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from sklearn.linear_model import BayesianRidge
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from Utils.plot_utils import PlotUtils
from Utils.data_utils import DataUtils


class DataProcessor:
    def __init__(self):
        self.plot_utils = PlotUtils()
        self.data_utils = DataUtils() 
        self.steps_model = None
        self.hr_model = None
        self.mood_model = None
        self.label_encoders = {}

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
        # Convert 'date' column to datetime

        data['date'] = pd.to_datetime(data['date'])
        data.set_index('date', inplace=True)

        # Resample monthly and sum steps
        steps_monthly = data['steps'].resample('ME').sum()  # Resample monthly and sum steps

        # Plot monthly steps trend
        self.plot_utils.plot_line_chart(steps_monthly.index, steps_monthly.values, 'Month', 'Steps', 'Monthly Steps Trend')

        # Generate report
        report_text = f"""Trends Over Time: Monthly Steps Trend\n\nAnalyzing trends in steps over time...
        {steps_monthly}
        """
        self.save_report(report_text, 'monthly_steps_trend')



    def identify_seasonal_patterns(self, data):
        # Check if 'date' column exists
        data = data.reset_index()
        if 'date' not in data.columns:
            raise ValueError("The 'date' column is missing from the data.")

        # Convert 'date' column to datetime
        data['date'] = pd.to_datetime(data['date'], errors='coerce')
        
        # Drop rows with NaT in 'date' due to conversion errors
        data.dropna(subset=['date'], inplace=True)

        # Define seasons based on months
        seasons = {
            'Winter': [11, 12, 1, 2],
            'Spring': [3, 4],
            'Summer': [5, 6, 7, 8],
            'Fall': [9, 10]
        }
        
        # Create a new column for the season
        data['season'] = data['date'].dt.month.map(
            lambda x: next((season for season, months in seasons.items() if x in months), None)
            )
        
        # Calculate average steps per season
        seasonal_avg_steps = data.groupby('season')['steps'].mean()

        # Plot seasonal average steps
        self.plot_utils.plot_bar_chart(seasonal_avg_steps.index, seasonal_avg_steps.values, 'Season', 'Average Steps',
                                        'Average Steps by Season')

        # Generate report
        report_text = f"""
        Seasonal Patterns: Average Steps by Season\n\nIdentifying seasonal patterns in steps...
        {seasonal_avg_steps}
        """
        self.save_report(report_text, 'average_steps_by_season')



    def compare_groups(self, data):
        # Example: Compare average calories burned by workout type
        avg_calories_by_workout = data.groupby('workout_type')['calories_burned'].mean().sort_values() - data['calories_burned'].mean() 
        plt.figure(figsize=(10, 6))
        sns.barplot(x=avg_calories_by_workout.index, y=avg_calories_by_workout.values)
        plt.title('Average Calories Burned by Workout Type')
        plt.xlabel('Workout Type')
        plt.ylabel('Average Calories Burned(Grouped by Workout) - Total Average Calories')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('Reports/visualizations/average_calories_by_workout_type.png')
        plt.show()

        # Generate report
        report_text = f"""Comparative Analysis: Average Calories Burned by Workout Type
        \n\nComparing average calories burned across different workout types...
        {data.groupby('workout_type')['calories_burned'].mean().sort_values()}
        """
        self.save_report(report_text, 'average_calories_by_workout_type')

    def correlation_analysis(self, data):
        # Example: Perform correlation analysis between numerical variables
        numerical_data = data.select_dtypes(include=['int', 'float'])
        numerical_data.drop('user_id', axis=1, inplace=True)
        correlation_matrix = numerical_data.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-0.002, vmax=0.002)
        plt.title('Correlation Matrix of Numerical Variables')
        plt.savefig('Reports/visualizations/correlation_matrix.png')
        plt.show()

        # Generate report
        report_text = f"""Correlation Analysis: Numerical Variables\n
        \nAnalyzing correlations between numerical variables...
        {correlation_matrix}
        """
        self.save_report(report_text, 'correlation_analysis')

    def analyze_location_based_insights(self, data):
        # Example: Analyze activity levels across different locations
        avg_steps_by_location = data.groupby('location')['steps'].mean().sort_values() - data['steps'].mean()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=avg_steps_by_location.index, y=avg_steps_by_location.values)
        plt.title('Average Steps by Location')
        plt.xlabel('Location')
        plt.ylabel('Average Steps(Grouped by Locations) - Total Average Steps')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('Reports/visualizations/average_steps_by_location.png')
        plt.show()

        # Generate report
        report_text = f"""Spatial Analysis: Average Steps by Location\n\nAnalyzing average steps across different locations...
        {avg_steps_by_location} 
        """
        self.save_report(report_text, 'average_steps_by_location')

    def map_activities(self, data):
        # Example: Map activities based on location
        plt.figure(figsize=(12, 8))
        sns.scatterplot(x='location', y='steps', hue='workout_type', data=data, s=100)
        plt.title('Activities by Location')
        plt.xlabel('Location')
        plt.ylabel('Steps')
        plt.xticks(rotation=45)
        plt.legend(title='Workout Type')
        plt.tight_layout()
        plt.savefig('Reports/visualizations/activities_by_location.png')
        plt.show()

        # Generate report
        report_text = f"""Spatial Analysis: Activities by Location\n\nMapping activities based on location...\n
        {pd.pivot_table(data, values='steps', index='location', columns='workout_type', aggfunc='mean')}"""
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
        report_text = f"""Behavioral Analysis: Average Steps by Day of Week\n\nAnalyzing average steps by day of the week...
        {avg_steps_by_day}
        """
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
        # report_text = "Behavioral Analysis: Impact of Weather Conditions on Steps\n\nAnalyzing the impact of weather conditions on activity levels..."
        # self.save_report(report_text, 'impact_of_weather_on_steps')

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
        # report_text = "Health Metrics Analysis: Health Impact of Activity on Heart Rate\n\nStudying the impact of activity on average heart rate..."
        # self.save_report(report_text, 'health_impact_of_activity')

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
        report_text = f"""Health Metrics Analysis: Average Heart Rate by Activity Type
        \n\nAnalyzing average heart rate during different activities...
        {avg_heart_rate_by_activity}
        """
        self.save_report(report_text, 'average_heart_rate_by_activity')


    def prediction_preprocess_data(self, data):
        label_encoders = {}
        # Convert 'date' column to datetime
        data['date'] = pd.to_datetime(data['date'], errors='coerce')
        data.dropna(subset=['date'], inplace=True)

        # Define seasons
        seasons = {
            'Winter': [12, 1, 2],
            'Spring': [3, 4, 5],
            'Summer': [6, 7, 8],
            'Fall': [9, 10, 11]
        }
        data['season'] = data['date'].dt.month.map(lambda x: next((season for season, months in seasons.items() if x in months), None))

        # Encode categorical variables
        for column in ['weather_conditions', 'location', 'mood', 'season']:
            le = LabelEncoder()
            data[column] = le.fit_transform(data[column])
            label_encoders[column] = le
        return data, label_encoders

    def prediction_models(self, data):
        # Preprocess data
        self.data, self.label_encoders = self.prediction_preprocess_data(data)
        # Prepare features and targets
        features = self.data[['weather_conditions', 'location', 'season', 'active_minutes', 'sleep_hours']]
        target_steps = self.data['steps']
        target_heart_rate = self.data['heart_rate_avg']
        target_mood = self.data['mood']

        # Split the data for steps and heart rate
        X_train, X_test, y_train_steps, y_test_steps = train_test_split(features, target_steps, test_size=0.2, random_state=42)
        X_train_hr, X_test_hr, y_train_hr, y_test_hr = train_test_split(features, target_heart_rate, test_size=0.2, random_state=42)

        # Fit Bayesian Ridge models
        self.steps_model = BayesianRidge()
        self.steps_model.fit(X_train, y_train_steps)

        self.hr_model = BayesianRidge()
        self.hr_model.fit(X_train_hr, y_train_hr)

        # Fit Gaussian Naive Bayes model for mood
        X_train_mood, X_test_mood, y_train_mood, y_test_mood = train_test_split(features, target_mood, test_size=0.2, random_state=42)
        self.mood_model = GaussianNB()
        self.mood_model.fit(X_train_mood, y_train_mood)

        # Optionally, you can print accuracy for mood model
        mood_predictions = self.mood_model.predict(X_test_mood)
        accuracy = accuracy_score(y_test_mood, mood_predictions)
        print(f"Mood prediction accuracy: {accuracy:.2f}")

    def forecast_trends(self, data):
        # For simplicity, forecast trends can be based on the fitted models
        # Here you might want to analyze the historical data and predict future trends.
        self.data, self.label_encoders = self.prediction_preprocess_data(data)
        # Example: Calculate average steps and heart rate by season
        trend_data = self.data.groupby('season').agg({'steps': 'mean', 'heart_rate_avg': 'mean'}).reset_index()
        print("Average Steps and Heart Rate by Season:")
        print(trend_data)

        # Forecast future trends based on historical average (simple example)
        # In practice, you'd use time series forecasting methods here
        forecasted_trends = {
            'Winter': trend_data.loc[trend_data['season'] == 'Winter'],
            'Spring': trend_data.loc[trend_data['season'] == 'Spring'],
            'Summer': trend_data.loc[trend_data['season'] == 'Summer'],
            'Fall': trend_data.loc[trend_data['season'] == 'Fall']
        }
        print(forecasted_trends)

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
        processor.plot_data_distribution(preprocessed_data)
        processor.analyze_trends_over_time(preprocessed_data)
        processor.compare_groups(preprocessed_data)
