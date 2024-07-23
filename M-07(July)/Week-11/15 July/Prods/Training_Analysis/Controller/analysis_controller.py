import pandas as pd
from Models.data_loader import DataLoader
from Models.data_processor import DataProcessor


class DataProcessorController:
    def __init__(self):
        self.data = DataLoader().load_data()
        self.model = DataProcessor(self.data)

    def perform_basic_grouping(self):
        print("Performing basic grouping operations...")
        self.model.group_by_skill()
        self.model.group_by_grade()
        self.model.group_by_allocation()
        self.model.group_by_project()
        self.model.group_by_place()
        self.model.group_by_training_status()
        self.model.group_by_training_type()
        self.model.group_by_upgraded_skills()

    def perform_advanced_grouping(self):
        print("Performing advanced grouping operations...")
        self.model.group_by_competency()

    def generate_general_reports(self):
        print("Generating general reports...")
        self.model.plot_group_by_competency()
        self.model.plot_group_by_skill()
        self.model.plot_group_by_grade()
        self.model.plot_group_by_allocation()
        self.model.plot_group_by_project()
        self.model.plot_group_by_place()
        self.model.plot_group_by_training_status()
        self.model.plot_group_by_training_type()
        self.model.plot_group_by_upgraded_skills()
        self.model.plot_training_status_overview()
        self.model.plot_developer_skills_competency()

    def generate_specific_reports(self, status=None, score_column=None, skill=None, date_column=None):
        print("Generating specific reports...")
        if status:
            self.model.plot_training_record_by_status(status)
        if score_column:
            self.model.plot_top_performers_by_score(score_column)
        if skill:
            self.model.plot_top_associates_by_skills(skill)
        if date_column:
            self.model.plot_monthwise_training_completion(date_column)

    def generate_growth_reports(self):
        print("Generating growth reports...")
        self.model.plot_final_training_growth()
        self.model.plot_associate_location_strength()
        self.model.plot_competency_strength_by_designation()


# Usage example:
if __name__ == "__main__":
    controller = DataProcessorController()

    # Example calls (you can replace with actual calls as needed):
    controller.perform_basic_grouping()
    controller.perform_advanced_grouping()
    controller.generate_general_reports()
    controller.generate_specific_reports(status='Completed', score_column='Final Score', skill='Python',
                                         date_column='Training Date')
    controller.generate_growth_reports()
