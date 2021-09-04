import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from Services.Config.get_input import GetInput
from Services.TextFile.read_text_content import ReadTextContent
from Services.TextFile.clean_hashtags import CleanHashtags
from Services.TextFile.write_text_content import WriteTextContent
from Services.Hashtags.iterate_random_hashtags import IterateRandomHashtags
from Services.Output.write_dockerfile import WriteDockerfile


class HashtagGenerator(GetInput):
    def execute_workflow(self):
        self.__handle_input_files()
        self.__generate_random_hashtags()
        self.__write_random_hashtag_file()
        self.__create_dockerfile()

    def __handle_input_files(self):
        self.hashtag_file = self.general_hashtag_file
        self.content = ReadTextContent.read_file(self.hashtag_file)
        self.general_hashtags = CleanHashtags(self).new_content

        self.hashtag_file = self.essential_hashtag_file
        self.content = ReadTextContent.read_file(self.hashtag_file)
        self.essential_hashtags = CleanHashtags(self).new_content

    def __generate_random_hashtags(self):
        self.output_content = IterateRandomHashtags(self).random_hashtag_text

    def __write_random_hashtag_file(self):
        WriteTextContent(self)

    def __create_dockerfile(self):
        file_path = (os.path.dirname(__file__))
        self.root_path = (os.path.dirname(file_path))
        WriteDockerfile(self)


my_code = HashtagGenerator(__file__)
my_code.execute_workflow()
