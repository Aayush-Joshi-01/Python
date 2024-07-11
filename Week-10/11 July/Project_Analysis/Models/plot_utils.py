import matplotlib.pyplot as plt
import seaborn as sns


class PlotUtils:
    def __init__(self):
        # Optionally, you can initialize settings for plotting here
        pass

    def plot_histogram(self, data, column):
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.savefig(f'Reports/visualizations/{column}_histogram.png')
        plt.show()

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

    # Add more plot types as needed for specific analyses


if __name__ == "__main__":
    # Example usage (optional)
    plotter = PlotUtils()
    # Example plot
    plotter.plot_histogram(data, 'steps')
