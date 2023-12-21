import os
from utils import read_classification_from_file

class TrainingCorpus:
    def __init__(self, folder_path):
        self.mail_folder_path = folder_path
        
    def get_class(self):
        dic = read_classification_from_file(self.mail_folder_path)
        sender_list = []
        subject_list = []
        for key, value in dic.items():
            if value == "SPAM":
                body = self.is_spam(key)
                sender_list.append(self.sender(body,sender_list))
                subject_list.append(self.subject(body, subject_list))
        return sender_list, subject_list
                
                
    def is_spam(self, file_name):
        file_path = os.path.join(self.mail_folder_path, file_name)
        with open(file_path, 'r', encoding = "utf-8")as file:
            body = file.read()
            body = str.lower(body)
            return body
            
    def sender(self, body, sender_mail):
        array = body.split()
        number = 0
        ret_sender = None
        for word in array:
            if(word == "from:"):
                possible_sender = array[number + 1]
                if possible_sender not in sender_mail:
                    ret_sender = possible_sender
                break
            number += 1                
        return ret_sender
        
    def subject(self, body, subject_mail):
        array = body.split()
        number = 0
        ret_subject = None
        for word in array:
            if(word == "subject:"):
                possible_subject = array[number + 1]
                if possible_subject not in subject_mail:
                    ret_subject = possible_subject
                break
            number += 1                
        return ret_subject