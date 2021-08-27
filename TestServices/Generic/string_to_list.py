class StringToList():
    def __init__(self, input_list):
        self.input_list = input_list
        self.__clean_list()
        self.__convert_string_to_list()

    def __clean_list(self):
        self.input_list = self.input_list.replace("[", "")
        self.input_list = self.input_list.replace("]", "")
        self.input_list = self.input_list.replace(", ", ",")
        self.input_list = self.input_list.replace(" ,", ",")

    def __convert_string_to_list(self):
        self.output_list = self.input_list.split(",")
