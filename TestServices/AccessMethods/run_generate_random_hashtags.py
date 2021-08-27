import os
import sys
file_path = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(os.path.split(file_path)[0])
from TestServices.Generic.string_to_list import StringToList
from Services.Hashtags.generate_random_hashtags import GenerateRandomHashtags


class RunGenerateRandomHashtags():
    def __init__(self, input):
        self.general_hashtags = StringToList(input.general_hashtags).output_list
        self.essential_hashtags = StringToList(input.essential_hashtags).output_list
        self.__execute_workflow()

    def __execute_workflow(self):
        self.random_hashtag_list = GenerateRandomHashtags(self).random_hashtag_list
