from trainingcorpus import TrainingCorpus
from basefilter import BaseFilter

class MyFilter:
    def __init__(self) -> None:
        self.sender_list = []
        self.subject_list = []
    
    def train(self, folder_path):
        train = TrainingCorpus(folder_path)
        self.sender_list, self.subject_list = train.get_class()
        
    def test(self, folder_path):
        BaseFilter(folder_path, "!prediction.txt")
        
    def calculate_result(self):
        