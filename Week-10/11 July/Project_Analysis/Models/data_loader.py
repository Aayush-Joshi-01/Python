import pandas as pd


class DataLoader:
    def __init__(self, file_path='Data/fitness_tracker_dataset.csv'):
        self.file_path = file_path

    def load_data(self):
        try:
            # Load CSV into pandas DataFrame
            df = pd.read_csv(self.file_path)
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
