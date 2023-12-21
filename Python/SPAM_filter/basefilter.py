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
            for filename, body in Corpus(self.folder_path).emails():
                if(first == True):
                    f.write("\n")
                self.result = self.calculate_result(body)
                first = True
                write = None
                write = filename + " " + "".join(self.result)
                f.write(write)
                
    def calculate_result(self, body):
        raise NotImplementedError("Implement")