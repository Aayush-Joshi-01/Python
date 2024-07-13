import matplotlib.pyplot as plt
import seaborn as sns
from Models.data_loader import DataLoader
from Decorators.Logger_Analysis import logger_analysis


class PlotUtils:
    def __init__(self):
        # Optionally, you can initialize settings for plotting here
        pass

    @logger_analysis
    def plot_histogram(self, data, column):
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.savefig(f'Reports/visualizations/{column}_histogram.png')
        plt.show()

    @logger_analysis
    def plot_line_chart(self, x_data, y_data, x_label, y_label, title):
        plt.figure(figsize=(10, 6))
        plt.plot(x_data, y_data, marker='o', linestyle='-', color='b', label=y_label)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'Reports/visualizations/{title.replace(" ", "_")}.png')
        plt.show()

    @logger_analysis
    def plot_bar_chart(self, x, y, x_label, y_label, title):
        plt.figure(figsize=(10, 6))
        plt.bar(x, y, color='skyblue')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.xticks(rotation=45)  # Rotate x labels for better readability
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()  # Adjust layout
        plt.show()  # Display the plot


    # Add more plot types as needed for specific analyses


if __name__ == "__main__":
    # Example usage (optional)
    plotter = PlotUtils()
    data_loader = DataLoader()
    # Example plot
    data = data_loader.load_data()
    plotter.plot_histogram(data, 'steps')
