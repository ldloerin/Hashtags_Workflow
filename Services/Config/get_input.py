import os
from Services.Config.read_json_file import ReadJsonFile


class GetInput:
    def __init__(self, main_code_file):
        self.code_path = os.path.dirname(main_code_file)
        self.__get_input_parameters()
        self.__get_file_path('general_hashtag_file', 'Input')
        self.__get_file_path('essential_hashtag_file', 'Input')
        self.__get_file_path('output_hashtag_file', 'Output')

    def __get_input_parameters(self):
        parameter_file = os.path.join(self.code_path, "Input", "config.json")
        parameter_file = parameter_file.replace("\\", "/")
        inputs = ReadJsonFile.load(parameter_file)
        for key, value in inputs.items():
            setattr(self, key, value)

    def __get_file_path(self, key, destination):
        file_name = getattr(self, key)
        file_path = os.path.join(self.code_path, destination, file_name)
        file_path = file_path.replace('\\', '/')
        setattr(self, key, file_path)
