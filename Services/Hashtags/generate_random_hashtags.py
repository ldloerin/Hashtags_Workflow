import random


class GenerateRandomHashtags:
    def __init__(self, general_hashtags, essential_hashtags, number_of_random_lists):
        self.general_hashtags = general_hashtags
        self.essential_hashtags = essential_hashtags
        self.random_hashtag_list = essential_hashtags.copy()
        self.number_of_random_lists = number_of_random_lists
        self.__iterate_constellations()

    def __iterate_constellations(self):
        self.random_hashtag_text = ''
        for i in range(0, self.number_of_random_lists):
            self.__generate_random_hashtag_list()
            self.__write_random_hashtag_text()
            self.random_hashtag_text += self.my_random_hashtag_text

    def __generate_random_hashtag_list(self):
        amount = 30 - len(self.essential_hashtags)
        randoms = random.sample(range(len(self.general_hashtags)), amount)
        for i in randoms:
            self.random_hashtag_list.append(self.general_hashtags[i])
        random.shuffle(self.random_hashtag_list)

    def __write_random_hashtag_text(self):
        self.my_random_hashtag_text = ''
        for hashtag in self.random_hashtag_list:
            self.my_random_hashtag_text += hashtag
            self.my_random_hashtag_text += ' '
        self.my_random_hashtag_text += '\n\n'
