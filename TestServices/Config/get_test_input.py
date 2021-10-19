import os
from TestServices.Config.read_test_json import ReadTestJson


class GetTestInput:
    def __init__(self, main_code_file):
        super().__init__()
        self.code_path = os.path.dirname(main_code_file)
        self.__get_input_parameters()

    def __get_input_parameters(self):
        json_file = os.path.join(self.code_path, "Input", "config.json")
        json_file = json_file.replace("\\", "/")
        inputs = ReadTestJson.read_json_file(json_file)
        for key, value in inputs.items():
            setattr(self, key, value)
