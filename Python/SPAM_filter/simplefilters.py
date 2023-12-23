import random
from basefilter import BaseFilter

class NaiveFilter(BaseFilter):
    def test(folder_path):
        BaseFilter(folder_path, "!truth_OK").write_to_file()

    def calculate_result(self):
        return "OK"

class ParanoidFilter(BaseFilter):
    def test(folder_path):
        BaseFilter(folder_path, "!truth_SPAM").write_to_file()
        
    def calculate_result(self):
        return "SPAM"

class RandomFilter(BaseFilter):
    def test(folder_path):
        BaseFilter(folder_path).write_to_file()
        
    def calculate_result(self):
        if(random.randint(0, 1) == 0):
            result = "SPAM"
        else:
            result = "OK"
        return result


if __name__ == "__main__":
    NaiveFilter.test("./Python/SPAM_filter/test_folder")
    ParanoidFilter.test("./Python/SPAM_filter/test_folder")
    RandomFilter.test("./Python/SPAM_filter/test_folder")