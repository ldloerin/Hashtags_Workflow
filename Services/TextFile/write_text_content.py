import codecs


class WriteTextContent:
    def write_file(output_file, output_content):
        f = codecs.open(output_file, "w", "utf-8")
        f.write(output_content)
        f.close()
