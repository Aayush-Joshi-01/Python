import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from Decorators.Logger_Analysis import analysis_logger
from Models.data_loader import DataLoader
from Utils.data_utils import clean_data, generate_random_scores

# Directory to save visualizations
visualization_dir = 'Reports/Visualizations/'

# Ensure the directory exists
os.makedirs(visualization_dir, exist_ok=True)

@analysis_logger
def plot_group_by_competency(df: pd.DataFrame, save: bool = False) -> None:
    grouped = df.explode('current_skills').groupby('current_skills')['name'].count().sort_values(ascending=False)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=grouped.values, y=grouped.index, palette="viridis")
    plt.xlabel('Count')
    plt.ylabel('Current Skills')
    plt.title('Count of Associates by Competency')
    plt.tight_layout()
    if save:
        plt.savefig(os.path.join(visualization_dir, 'group_by_competency.png'))
    plt.show()

@analysis_logger
def plot_group_by_grade(df: pd.DataFrame, save: bool = False) -> None:
    grouped = df.groupby('grade')['name'].count().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=grouped.index, y=grouped.values, palette="viridis")
    plt.xlabel('Grade')
    plt.ylabel('Count')
    plt.title('Count of Associates by Grade')
    plt.tight_layout()
    if save:
        plt.savefig(os.path.join(visualization_dir, 'group_by_grade.png'))
    plt.show()

@analysis_logger
def plot_group_by_training_status(df: pd.DataFrame, save: bool = False) -> None:
    grouped = df.groupby('training_status')['name'].count().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=grouped.index, y=grouped.values, palette="viridis")
    plt.xlabel('Training Status')
    plt.ylabel('Count')
    plt.title('Count of Associates by Training Status')
    plt.tight_layout()
    if save:
        plt.savefig(os.path.join(visualization_dir, 'group_by_training_status.png'))
    plt.show()

@analysis_logger
def plot_group_by_training_type(df: pd.DataFrame, save: bool = False) -> None:
    grouped = df.groupby('training_type')['name'].count().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=grouped.index, y=grouped.values, palette="viridis")
    plt.xlabel('Training Type')
    plt.ylabel('Count')
    plt.title('Count of Associates by Training Type')
    plt.tight_layout()
    if save:
        plt.savefig(os.path.join(visualization_dir, 'group_by_training_type.png'))
    plt.show()

@analysis_logger
def plot_group_by_upgraded_skills(df: pd.DataFrame, save: bool = False) -> None:
    grouped = df.explode('upgraded_skills').groupby('upgraded_skills')['name'].count().sort_values(ascending=False)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=grouped.values, y=grouped.index, palette="viridis")
    plt.xlabel('Count')
    plt.ylabel('Upgraded Skills')
    plt.title('Count of Associates by Upgraded Skills')
    plt.tight_layout()
    if save:
        plt.savefig(os.path.join(visualization_dir, 'group_by_upgraded_skills.png'))
    plt.show()

@analysis_logger
def plot_training_record_by_status(df: pd.DataFrame, save: bool = False) -> None:
    grouped = df.groupby('status')['name'].count().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=grouped.index, y=grouped.values, palette="viridis")
    plt.xlabel('Training Record Status')
    plt.ylabel('Count')
    plt.title('Training Record Count by Status')
    plt.tight_layout()
    if save:
        plt.savefig(os.path.join(visualization_dir, 'training_record_by_status.png'))
    plt.show()

@analysis_logger
def plot_top_performers_by_score(df: pd.DataFrame, score_column: str = 'final_score', save: bool = False) -> None:
    top_performers = df.sort_values(by=score_column, ascending=False).head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_performers[score_column], y=top_performers['name'], palette="viridis")
    plt.xlabel('Score')
    plt.ylabel('Name')
    plt.title(f'Top 10 Performers by {score_column.replace("_", " ").title()}')
    plt.tight_layout()
    if save:
        plt.savefig(os.path.join(visualization_dir, f'top_performers_by_{score_column}.png'))
    plt.show()

if __name__ == "__main__":
    # Example usage
    loader = DataLoader()
    data = loader.load_data()
    if data is not None:
        cleaned_data = clean_data(data)
        cleaned_data_with_scores = generate_random_scores(cleaned_data)
        
        # Ask the user if they want to save the plots
        save_plots = input("Do you want to save the plots? (yes/no): ").strip().lower() == 'yes'
        
        plot_group_by_competency(cleaned_data_with_scores, save=save_plots)
        plot_group_by_grade(cleaned_data_with_scores, save=save_plots)
        plot_group_by_training_status(cleaned_data_with_scores, save=save_plots)
        plot_group_by_training_type(cleaned_data_with_scores, save=save_plots)
        plot_group_by_upgraded_skills(cleaned_data_with_scores, save=save_plots)
        plot_training_record_by_status(cleaned_data_with_scores, save=save_plots)
        plot_top_performers_by_score(cleaned_data_with_scores, save=save_plots)
