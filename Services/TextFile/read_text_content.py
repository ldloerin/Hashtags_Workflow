import codecs


class ReadTextContent:
    def read_file(text_file):
        f = codecs.open(text_file, "r", "utf-8")
        content = f.readlines()
        f.close()
        return content
