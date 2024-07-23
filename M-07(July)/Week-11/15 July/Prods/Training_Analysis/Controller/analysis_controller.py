import pandas as pd
from Models.data_loader import DataLoader
from Models.data_processor import DataProcessor

class DataProcessorController:
    def __init__(self, df: pd.DataFrame):
        self.processor = DataProcessor(df)

    def perform_basic_grouping(self):
        print("Performing basic grouping operations...")
        self.processor.group_by_skill()
        self.processor.group_by_grade()
        self.processor.group_by_allocation()
        self.processor.group_by_project()
        self.processor.group_by_place()
        self.processor.group_by_training_status()
        self.processor.group_by_training_type()
        self.processor.group_by_upgraded_skills()

    def perform_advanced_grouping(self):
        print("Performing advanced grouping operations...")
        self.processor.group_by_competency()

    def generate_general_reports(self):
        print("Generating general reports...")
        self.processor.plot_group_by_competency()
        self.processor.plot_group_by_skill()
        self.processor.plot_group_by_grade()
        self.processor.plot_group_by_allocation()
        self.processor.plot_group_by_project()
        self.processor.plot_group_by_place()
        self.processor.plot_group_by_training_status()
        self.processor.plot_group_by_training_type()
        self.processor.plot_group_by_upgraded_skills()
        self.processor.plot_training_status_overview()
        self.processor.plot_developer_skills_competency()

    def generate_specific_reports(self, status=None, score_column=None, skill=None, date_column=None):
        print("Generating specific reports...")
        if status:
            self.processor.plot_training_record_by_status(status)
        if score_column:
            self.processor.plot_top_performers_by_score(score_column)
        if skill:
            self.processor.plot_top_associates_by_skills(skill)
        if date_column:
            self.processor.plot_monthwise_training_completion(date_column)

    def generate_growth_reports(self):
        print("Generating growth reports...")
        self.processor.plot_final_training_growth()
        self.processor.plot_associate_location_strength()
        self.processor.plot_competency_strength_by_designation()

# Usage example:
if __name__ == "__main__":
    df = DataLoader().load_data()
    controller = DataProcessorController(df)

    # Example calls (you can replace with actual calls as needed):
    controller.perform_basic_grouping()
    controller.perform_advanced_grouping()
    controller.generate_general_reports()
    controller.generate_specific_reports(status='Completed', score_column='Final Score', skill='Python', date_column='Training Date')
    controller.generate_growth_reports()
