import os
import sys
file_path = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(os.path.split(file_path)[0])
from Services.Hashtags.generate_random_hashtags import GenerateRandomHashtags


class RunGenerateRandomHashtags():
    def __init__(self, inputs):
        self.__run_generate_random_hashtags(inputs)

    def __run_generate_random_hashtags(self, inputs):
        self.random_hashtag_list = GenerateRandomHashtags(inputs).random_hashtag_list