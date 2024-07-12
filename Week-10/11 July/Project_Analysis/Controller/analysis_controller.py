from Models.data_loader import DataLoader
from Models.data_processor import DataProcessor
from Models.plot_utils import PlotUtils


class AnalysisController:
    def __init__(self):
        self.data_loader = DataLoader()
        self.data_processor = DataProcessor()
        self.plot_utils = PlotUtils()

    def perform_descriptive_analysis(self):
        """
        Performs descriptive analysis on loaded data.
        """
        try:
            data = self.data_loader.load_data()
            if data is None:
                raise Exception("Failed to load data.")

            # Calculate basic statistics
            self.data_processor.calculate_basic_statistics(data)

            # Plot data distribution
            self.plot_utils.plot_data_distribution(data)

        except Exception as e:
            print(f"Error performing descriptive analysis: {str(e)}")

    def perform_temporal_analysis(self):
        """
        Performs temporal analysis on loaded data.
        """
        try:
            data = self.data_loader.load_data()
            if data is None:
                raise Exception("Failed to load data.")

            # Analyze trends over time
            self.data_processor.analyze_trends_over_time(data)

            # Identify seasonal patterns
            self.data_processor.identify_seasonal_patterns(data)

        except Exception as e:
            print(f"Error performing temporal analysis: {str(e)}")

    def perform_comparative_analysis(self):
        """
        Performs comparative analysis on loaded data.
        """
        try:
            data = self.data_loader.load_data()
            if data is None:
                raise Exception("Failed to load data.")

            # Compare groups
            self.data_processor.compare_groups(data)

            # Analyze correlations
            self.data_processor.correlation_analysis(data)

        except Exception as e:
            print(f"Error performing comparative analysis: {str(e)}")

    def perform_spatial_analysis(self):
        """
        Performs spatial analysis on loaded data.
        """
        try:
            data = self.data_loader.load_data()
            if data is None:
                raise Exception("Failed to load data.")

            # Analyze location-based insights
            self.data_processor.analyze_location_based_insights(data)

            # Map activities
            self.data_processor.map_activities(data)

        except Exception as e:
            print(f"Error performing spatial analysis: {str(e)}")

    def perform_behavioral_analysis(self):
        """
        Performs behavioral analysis on loaded data.
        """
        try:
            data = self.data_loader.load_data()
            if data is None:
                raise Exception("Failed to load data.")

            # Analyze activity patterns
            self.data_processor.analyze_activity_patterns(data)

            # Analyze impact of weather
            self.data_processor.analyze_impact_of_weather(data)

        except Exception as e:
            print(f"Error performing behavioral analysis: {str(e)}")

    def perform_health_metrics_analysis(self):
        """
        Performs health metrics analysis on loaded data.
        """
        try:
            data = self.data_loader.load_data()
            if data is None:
                raise Exception("Failed to load data.")

            # Study health impact of activity
            self.data_processor.study_health_impact_of_activity(data)

            # Analyze heart rate data
            self.data_processor.analyze_heart_rate(data)

        except Exception as e:
            print(f"Error performing health metrics analysis: {str(e)}")

    def perform_predictive_analysis(self):
        """
        Performs predictive analysis on loaded data (optional).
        """
        try:
            data = self.data_loader.load_data()
            if data is None:
                raise Exception("Failed to load data.")

            # Build prediction models
            self.data_processor.build_prediction_models(data)

            # Forecast trends
            self.data_processor.forecast_trends(data)

        except Exception as e:
            print(f"Error performing predictive analysis: {str(e)}")

    # Additional methods can be added based on specific analysis needs


if __name__ == "__main__":
    controller = AnalysisController()
    controller.perform_descriptive_analysis()
    controller.perform_temporal_analysis()
    controller.perform_comparative_analysis()
    controller.perform_spatial_analysis()
    controller.perform_behavioral_analysis()
    controller.perform_health_metrics_analysis()
    controller.perform_predictive_analysis()
