import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from Models.data_loader import DataLoader

class DataProcessor:
    def __init__(self, df: pd.DataFrame):
        self.df = DataLoader().load_data()
        self.reports_path = 'Reports/'

    def save_plot(self, plot_func, plot_name):
        if input(f"Do you want to save the plot '{plot_name}'? (y/n): ").lower() == 'y':
            plot_dir = os.path.join(self.reports_path, 'Visualizations')
            os.makedirs(plot_dir, exist_ok=True)
            plot_path = os.path.join(plot_dir, f"{plot_name}.png")
            plot_func()
            plt.savefig(plot_path)
            print(f"Plot saved to {plot_path}")
        else:
            plot_func()
    
    def save_report(self, report_func, report_name):
        if input(f"Do you want to save the report '{report_name}'? (y/n): ").lower() == 'y':
            report_dir = os.path.join(self.reports_path, 'CSV_Reports')
            os.makedirs(report_dir, exist_ok=True)
            report_path = os.path.join(report_dir, f"{report_name}.csv")
            report_func().to_csv(report_path, index=False)
            print(f"Report saved to {report_path}")
        else:
            print("Report not saved.")
    
    def group_by_competency(self):
        return self.df.explode('Current Skills').groupby('Current Skills')

    def group_by_skill(self):
        return self.df.groupby('Training Name')

    def group_by_grade(self):
        return self.df.groupby('Grade')

    def group_by_allocation(self):
        return self.df.groupby('Current Allocation')

    def group_by_project(self):
        return self.df.groupby('Project')

    def group_by_place(self):
        return self.df[['Current location', 'Name']].groupby('Current location')

    def group_by_training_status(self):
        return self.df.groupby('Status')

    def group_by_training_type(self):
        return self.df.groupby('Resource Type')

    def group_by_upgraded_skills(self):
        return self.df.groupby('Upgraded Skills')

    def training_record_by_status(self, status):
        return self.df[self.df['Status'] == status]

    def training_resource_count_by_name(self):
        return self.df['Training Name'].value_counts()

    def total_training_attended(self):
        return self.df.shape[0]

    def competency_training_attended(self, competency):
        return self.df[self.df['Current Skills'].str.contains(competency, case=False, na=False)]

    def top_performers_by_score(self, score_column):
        return self.df.loc[self.df.groupby('Name')[score_column].idxmax()]

    def developer_skills_competency(self):
        current_skills = self.df['Current Skills'].explode().unique()
        return current_skills

    def associate_location_strength(self):
        return self.df.groupby('Current location').size()

    def competency_strength_by_designation(self):
        exploded_df = self.df.explode('Current Skills')
        competency_counts = exploded_df.groupby(['Grade', 'Current Skills']).size().unstack(fill_value=0)
        return competency_counts

    def top_associates_by_skills(self, skill):
        return self.df[self.df['Current Skills'].str.contains(skill, case=False, na=False)]

    def training_status_overview(self):
        return self.df.groupby('Status').size()

    def monthwise_training_completion(self, date_column):
        self.df[date_column] = pd.to_datetime(self.df[date_column])
        self.df['Month'] = self.df[date_column].dt.month
        return self.df.groupby('Month').size()

    def final_training_growth(self):
        return self.df[['Pre Assessment score', 'Final Score']]

    def plot_group_by_competency(self):
        grouped = self.group_by_competency().size()
        self.save_plot(lambda: sns.barplot(x=grouped.index, y=grouped.values),
                       'Group_by_Competency')

    def plot_group_by_skill(self):
        grouped = self.group_by_skill().size()
        self.save_plot(lambda: sns.barplot(x=grouped.index, y=grouped.values),
                       'Group_by_Skill')

    def plot_group_by_grade(self):
        grouped = self.group_by_grade().size()
        self.save_plot(lambda: sns.barplot(x=grouped.index, y=grouped.values),
                       'Group_by_Grade')

    def plot_group_by_allocation(self):
        grouped = self.group_by_allocation().size()
        self.save_plot(lambda: sns.barplot(x=grouped.index, y=grouped.values),
                       'Group_by_Allocation')

    def plot_group_by_project(self):
        grouped = self.group_by_project().size()
        self.save_plot(lambda: sns.barplot(x=grouped.index, y=grouped.values),
                       'Group_by_Project')

    def plot_group_by_place(self):
        grouped = self.group_by_place().size()
        self.save_plot(lambda: sns.barplot(x=grouped.index, y=grouped.values),
                       'Group_by_Place')

    def plot_group_by_training_status(self):
        grouped = self.group_by_training_status().size()
        self.save_plot(lambda: sns.barplot(x=grouped.index, y=grouped.values),
                       'Group_by_Training_Status')

    def plot_group_by_training_type(self):
        grouped = self.group_by_training_type().size()
        self.save_plot(lambda: sns.barplot(x=grouped.index, y=grouped.values),
                       'Group_by_Training_Type')

    def plot_group_by_upgraded_skills(self):
        grouped = self.group_by_upgraded_skills().size()
        self.save_plot(lambda: sns.barplot(x=grouped.index, y=grouped.values),
                       'Group_by_Upgraded_Skills')

    def plot_training_record_by_status(self, status):
        filtered_df = self.training_record_by_status(status)
        self.save_plot(lambda: sns.countplot(x='Status', data=filtered_df),
                       f'Training_Record_by_Status_{status}')

    def plot_top_performers_by_score(self, score_column):
        top_performers = self.top_performers_by_score(score_column)
        self.save_report(lambda: top_performers,
                         f'Top_Performers_By_{score_column}')
        self.save_plot(lambda: sns.barplot(x='Name', y=score_column, data=top_performers),
                       f'Top_Performers_By_{score_column}')

    def plot_developer_skills_competency(self):
        skills = self.developer_skills_competency()
        self.save_report(lambda: pd.DataFrame(skills, columns=['Skill']),
                         'Developer_Skills_Competency')

    def plot_associate_location_strength(self):
        location_strength = self.associate_location_strength()
        self.save_plot(lambda: sns.barplot(x=location_strength.index, y=location_strength.values),
                       'Associate_Location_Strength')

    def plot_competency_strength_by_designation(self):
        competency_strength = self.competency_strength_by_designation()
        self.save_plot(lambda: competency_strength.plot(kind='bar', figsize=(12, 8)),
                       'Competency_Strength_By_Designation')

    def plot_top_associates_by_skills(self, skill):
        top_associates = self.top_associates_by_skills(skill)
        self.save_report(lambda: top_associates,
                         f'Top_Associates_By_Skills_{skill}')
        self.save_plot(lambda: sns.barplot(x='Name', y='Current Skills', data=top_associates),
                       f'Top_Associates_By_Skills_{skill}')

    def plot_training_status_overview(self):
        status_overview = self.training_status_overview()
        self.save_plot(lambda: sns.barplot(x=status_overview.index, y=status_overview.values),
                       'Training_Status_Overview')

    def plot_monthwise_training_completion(self, date_column):
        monthwise_completion = self.monthwise_training_completion(date_column)
        self.save_plot(lambda: sns.lineplot(x=monthwise_completion.index, y=monthwise_completion.values),
                       'Monthwise_Training_Completion')

    def plot_final_training_growth(self):
        growth = self.final_training_growth()
        self.save_plot(lambda: growth.plot(kind='box', figsize=(8, 6)),
                       'Final_Training_Growth')
