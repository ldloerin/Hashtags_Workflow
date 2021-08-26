from Services.Hashtags.generate_random_hashtags import GenerateRandomHashtags


class IterateRandomHashtags():
    def __init__(self, input):
        self.general_hashtags = input.general_hashtags
        self.essential_hashtags = input.essential_hashtags
        self.number_of_random_lists = input.number_of_random_lists
        self.random_hashtag_text = ''
        self.__iterate_constellations()

    def __iterate_constellations(self):
        for constellation in range(0,self.number_of_random_lists):
            text = GenerateRandomHashtags(self).my_random_hashtag_text
            self.random_hashtag_text += text
