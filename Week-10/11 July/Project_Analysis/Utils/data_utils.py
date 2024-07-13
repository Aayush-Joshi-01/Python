import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from Models.data_loader import DataLoader
from Decorators.Logger_Analysis import logger_analysis

class DataUtils:
    def __init__(self):
        pass

    @logger_analysis
    def preprocess_data(self, data):
        # Example: Data preprocessing steps
        # Convert date column to datetime format
        data['date'] = pd.to_datetime(data['date'])

        # Handle missing values (if any)
        data.fillna(0, inplace=True)  # Replace NaN with 0 (this is a simplistic example)

        return data

    @logger_analysis
    def scale_data(self, data):
        # Example: Scaling numerical data
        numerical_cols = data.select_dtypes(include=['int', 'float']).columns
        scaler = StandardScaler()
        data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

        return data

    @logger_analysis
    def reduce_dimensionality(self, data):
        # Example: Reduce dimensionality using PCA (Principal Component Analysis)
        numerical_cols = data.select_dtypes(include=['int', 'float']).columns
        pca = PCA(n_components=2)
        principal_components = pca.fit_transform(data[numerical_cols])
        principal_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
        data = pd.concat([data, principal_df], axis=1)
        return data


if __name__ == "__main__":
    # Example usage (optional)

    loader = DataLoader()
    data = loader.load_data()
    if data is not None:
        utils = DataUtils()
        preprocessed_data = utils.preprocess_data(data)
        scaled_data = utils.scale_data(preprocessed_data)
        reduced_data = utils.reduce_dimensionality(scaled_data)
        print(reduced_data.head())
