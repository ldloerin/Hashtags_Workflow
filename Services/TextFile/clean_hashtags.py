import codecs


class CleanHashtags():
    def __init__(self, content, hashtag_file):
        self.content = content
        self.input_file = hashtag_file
        self.__remove_word_wrapping()
        self.__remove_double_content()
        self.__rewrite_hashtag_file()

    def __remove_word_wrapping(self):
        self.new_content = []
        for line in self.content:
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            self.new_content.append(line)

    def __remove_double_content(self):
        self.new_content = sorted(list(dict.fromkeys(self.new_content)))

    def __rewrite_hashtag_file(self):
        new_content = ''
        for line in self.new_content:
            new_content += line
            new_content += '\n'
        f = codecs.open(self.input_file, "w", "utf-8")
        f.write(new_content)
        f.close()
