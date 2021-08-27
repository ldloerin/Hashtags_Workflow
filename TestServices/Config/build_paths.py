import os
from TestServices.Config.read_test_json_file import ReadTestJsonFile


class BuildPaths:
    def __init__(self, input):
        self.__get_file_path('main_source_code', input.main_source_code)
        self.__get_file_path('general_hashtag_file', input.general_hashtag_file)
        self.__get_file_path('essential_hashtag_file', input.essential_hashtag_file)
        self.__get_file_path('output_hashtag_file', input.output_hashtag_file)

    def __get_file_path(self, key, relative_path):
        file_path = os.path.join(self.root_path, relative_path)
        file_path = file_path.replace('\\', '/')
        setattr(self, key, file_path)
