import pandas as pd
import numpy as np
from Decorators.Logger_Analysis import analysis_logger
from Models.data_loader import DataLoader


@analysis_logger
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the input DataFrame by handling missing values, removing duplicates,
    standardizing column formats, cleaning skills, and generating random scores.

    Args:
        df (pd.DataFrame): The DataFrame to clean.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Standardize column names (convert to lower case)
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    # Clean and create a list of unique skills for each row in 'current_skills' column
    if 'current_skills' in df.columns:
        current_skills_column = df['current_skills']
        cleaned_skills = current_skills_column.str.split(r'\s*\+\s*|\s*,\s*|\s*and\s*|\s*;\s*|\s*\|\s*').explode().str.strip()
        unique_skills = cleaned_skills.unique()
        df['current_skills'] = cleaned_skills.groupby(cleaned_skills.index).agg(list)

    # Example: Convert date columns to datetime format
    if 'date_column' in df.columns:
        df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')

    # Example: Standardize text columns to lower case
    text_columns = ['name', 'upgraded_skills', 'training_type']
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].str.lower().str.strip()

    print("Data cleaned successfully.")
    return df

@analysis_logger
def generate_random_scores(df: pd.DataFrame, score_columns: list = ['pre_assessment_score', 'final_score']) -> pd.DataFrame:
    """
    Generates random scores for specified columns in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to update.
        score_columns (list): List of column names for which to generate random scores.

    Returns:
        pd.DataFrame: The updated DataFrame with random scores.
    """
    
    for column in score_columns:
        df[column] = np.random.randint(0, 101, size=len(df))

    print(f"Random scores generated for columns: {score_columns}.")
    return df

if __name__ == "__main__":
    # Example usage
    loader = DataLoader()
    data = loader.load_data()
    if data is not None:
        cleaned_data = clean_data(data)
        cleaned_data_with_scores = generate_random_scores(cleaned_data)
        print(cleaned_data_with_scores.head())  # Print first few rows of cleaned data with random scores
