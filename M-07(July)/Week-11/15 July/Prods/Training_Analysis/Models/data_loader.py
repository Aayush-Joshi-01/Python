import pandas as pd
from tqdm import tqdm
# from Decorators.Logger_Analysis import analysis_logger


class DataLoader:
    def __init__(self, file_path='Data/cleaned_data.csv'):
        self.file_path = file_path

    # @analysis_logger
    def load_data(self):
        try:
            # Get the number of rows in the file
            with open(self.file_path, 'r') as f:
                total_rows = sum(1 for line in f) - 1  # Subtract 1 for header

            # Load CSV into pandas DataFrame with progress bar
            df = pd.read_csv(self.file_path, chunksize=5)  # Adjust chunksize as needed
            chunks = []
            for chunk in tqdm(df, total=total_rows // 5, desc="Loading data"):  # Adjust total based on chunksize
                chunks.append(chunk)

            df = pd.concat(chunks, ignore_index=True)
            print(f"Data loaded successfully from {self.file_path}")
            return df

        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            return None
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None

    # Additional methods for data validation, cleaning, etc. can be added here


if __name__ == "__main__":
    # Example usage (optional)
    loader = DataLoader()
    data = loader.load_data()
    if data is not None:
        print(data.head())  # Print first few rows of loaded data
