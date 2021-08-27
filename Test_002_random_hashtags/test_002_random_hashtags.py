import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from TestServices.Config.get_test_input import GetTestInput
from TestServices.AccessMethods.run_generate_random_hashtags import RunGenerateRandomHashtags

# Get test cofiguration input
config = GetTestInput(__file__)

# Run method to be tested
input = RunGenerateRandomHashtags(config)


class TestClass:
    def test_1_length_random_hashtags(self):
        tested_length = len(input.random_hashtag_list)
        reference_length = config.length_random_hashtag_list
        assert tested_length == reference_length

    def test_2_essential_random_hashtags(self):
        all_essential_hashtags_found = True
        for hashtag in input.essential_hashtags:
            if not hashtag in input.random_hashtag_list:
                all_essential_hashtags_found = False
                break
        assert all_essential_hashtags_found is True
