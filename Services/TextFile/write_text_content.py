import codecs


class WriteTextContent():
    def __init__(self, input):
        self.output_hashtag_file = input.output_hashtag_file
        self.output_content = input.output_content
        self.__write_file()

    def __write_file(self):
        f = codecs.open(self.output_hashtag_file, "w", "utf-8")
        f.write(self.output_content)
        f.close()
