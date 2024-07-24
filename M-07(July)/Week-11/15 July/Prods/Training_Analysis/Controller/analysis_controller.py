import pandas as pd
from Models.data_loader import DataLoader
from Models.data_processor import DataProcessor
from time import sleep
from Controller.group_viewer import show_data
from Decorators.Logger_Analysis import analysis_logger


class DataProcessorController:
    def __init__(self):
        self.data = None
        self.model = None

    @analysis_logger
    def perform_basic_grouping(self):
        self.data = DataLoader().load_data()
        self.model = DataProcessor(self.data)
        print("Performing basic grouping operations...\n")
        grouped_data = self.model.group_by_skill()
        show_data(grouped_data=grouped_data, type_name="Group By Skill", columns=['Name','Emp ID','Current Skills','Current location'])
        grouped_data = self.model.group_by_grade()
        show_data(grouped_data=grouped_data, type_name="Group By Grade",columns=['Name', 'Emp ID', 'Grade', 'Current location', 'Project'])
        grouped_data = self.model.group_by_allocation()
        show_data(grouped_data=grouped_data, type_name="Group By Allocation", columns=['Name', 'Emp ID', 'Current Allocation', 'Status'])
        grouped_data = self.model.group_by_project()
        show_data(grouped_data=grouped_data, type_name="Group By Project", columns=['Name', 'Emp ID', 'Current Allocation', 'Status', 'Project'])
        grouped_data = self.model.group_by_place()
        show_data(grouped_data=grouped_data, type_name="Group By Place")
        grouped_data = self.model.group_by_training_status()
        show_data(grouped_data=grouped_data, type_name="Group By Status", columns=['Name', 'Emp ID', 'Status'])
        grouped_data = self.model.group_by_training_type()
        show_data(grouped_data=grouped_data, type_name="Group By Type", columns=['Name', 'Emp ID', 'Resource Type'])
        grouped_data = self.model.group_by_upgraded_skills()
        show_data(grouped_data=grouped_data, type_name="Group By Upgraded Skills", columns=['Name', 'Emp ID', 'Upgraded Skills', 'Current Skills', 'Final Score ', 'Pre Assessment score'])

    @analysis_logger
    def perform_advanced_grouping(self):
        self.data = DataLoader().load_data()
        self.model = DataProcessor(self.data)
        print("Performing advanced grouping operations...")
        grouped_data = self.model.group_by_competency()
        show_data(grouped_data=grouped_data, type_name="Group By Upgraded Skills")

    @analysis_logger
    def generate_general_reports(self):
        self.data = DataLoader().load_data()
        self.model = DataProcessor(self.data)
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

    @analysis_logger
    def generate_specific_reports(self, status=None, score_column=None, skill=None, date_column=None):
        self.data = DataLoader().load_data()
        self.model = DataProcessor(self.data)
        print("Generating specific reports...")
        if status:
            self.model.plot_training_record_by_status(status)
        if score_column:
            self.model.plot_top_performers_by_score(score_column)
        if skill:
            self.model.plot_top_associates_by_skills(skill)
        if date_column:
            self.model.plot_monthwise_training_completion(date_column)

    @analysis_logger
    def generate_growth_reports(self):
        self.data = DataLoader().load_data()
        self.model = DataProcessor(self.data)
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
