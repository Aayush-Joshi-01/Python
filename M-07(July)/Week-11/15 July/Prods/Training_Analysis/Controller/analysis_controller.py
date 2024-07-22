from Models.data_loader import DataLoader
from Models.data_processor import DataProcessor
from Utils.plot_utils import PlotUtils
from Decorators.Logger_Analysis import analysis_logger


class AnalysisController:
    def __init__(self):
        self.data_loader = DataLoader()
        self.data_processor = DataProcessor()
        self.plot_utils = PlotUtils()
    
    

if __name__ == "__main__":
    controller = AnalysisController()
