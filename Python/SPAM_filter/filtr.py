from trainingcorpus import TrainingCorpus
from basefilter import BaseFilter

class MyFilter(BaseFilter):
    def __init__(self):
        pass       
    
    def train(self, folder_path):
        self.sender_list = []
        self.subject_list = []
        train = TrainingCorpus(folder_path)
        self.sender_list, self.subject_list = train.get_class()
        
    def test(self, folder_path):
        BaseFilter(folder_path, "!prediction.txt")
        
    def calculate_result(self, body):
        probability = 0
        array = body.split()
        probability += self.check_sender(array)
        probability += self.check_subject(array)
        if(probability > 0):
            return "SPAM"
        else:
            return "OK"
            
    def check_sender(self, array):
        for word in array:
            if word in self.sender_list:
                return 1
        return 0
    
    def check_subject(self, array):
        for word in array:
            if word in self.subject_list:
                return 1
        return 0

if __name__ == "__main__":
    testing = MyFilter()
    testing.train("./Python/SPAM_filter/spam-data-12-s75-h25/1")
    testing.test("./Python/SPAM_filter/spam-data-12-s75-h25/2")