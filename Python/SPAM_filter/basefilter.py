import os
import random
from corpus import Corpus

class BaseFilter:
    def __init__(self, folder_path, file = "!truth.txt"):
        self.result
        self.folder_path = folder_path
        self.file = file

    def write_to_file(self):
        first = False
        file = os.path.join(self.folder_path, self.file)
        with open(file, "w", encoding="utf-8")as f:
            for _ in Corpus(self.folder_path).emails():
                if(first == True):
                    f.write("\n")
                self.result = self.calculate_result()
                first = True
                f.write(self.result)
                
    def calculate_result(self):
        raise NotImplementedError("Implement")