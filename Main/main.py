import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from Services.Config.get_input import GetInput
from Services.TextFile.read_text_content import ReadTextContent
from Services.TextFile.clean_hashtags import CleanHashtags
from Services.TextFile.write_text_content import WriteTextContent
from Services.Hashtags.generate_random_hashtags import GenerateRandomHashtags
from Services.Output.write_dockerfile import WriteDockerfile


class HashtagGenerator(GetInput):
    def execute_workflow(self):
        self.__handle_input_files()
        self.__generate_random_hashtags()
        self.__write_random_hashtag_file()
        self.__create_dockerfile()

    def __handle_input_files(self):
        hashtag_file = os.path.join(os.path.dirname(__file__), 'Input', self.general_hashtag_file)
        content = ReadTextContent.read_file(hashtag_file)
        self.general_hashtags = CleanHashtags(content, hashtag_file).new_content

        hashtag_file = os.path.join(os.path.dirname(__file__), 'Input', self.essential_hashtag_file)
        content = ReadTextContent.read_file(hashtag_file)
        self.essential_hashtags = CleanHashtags(content, hashtag_file).new_content

    def __generate_random_hashtags(self):
        my_rand_hashtags = GenerateRandomHashtags(self.general_hashtags, self.essential_hashtags, self.number_of_random_lists)
        self.output_content = my_rand_hashtags.random_hashtag_text

    def __write_random_hashtag_file(self):
        output_hashtag_file = os.path.join(os.path.dirname(__file__), 'Output', self.output_hashtag_file)
        WriteTextContent.write_file(output_hashtag_file, self.output_content)

    def __create_dockerfile(self):
        file_path = (os.path.dirname(__file__))
        root_path = (os.path.dirname(file_path))
        WriteDockerfile(root_path, self.output_content)


my_code = HashtagGenerator(__file__)
my_code.execute_workflow()
