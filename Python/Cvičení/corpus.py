import os

class Corpus:

    def __init__(self, path):
        self.file_path = path

    def emails(self):
        file_list = os.listdir(self.file_path)

        for file_name in file_list:
            file_path = os.path.join(self.file_path, file_name)

            if os.path.isfile(file_path):
                with open(file_path, "rt", encoding="utf=8") as f:
                    body = f.readlines()
                yield file_path, body