import os
# import pytest
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from TestServices.Config.get_test_input import GetTestInput
from TestServices.AccessMethods.run_get_input import RunGetInput

config = GetTestInput(__file__)
my_code = RunGetInput(config.main_source_code)
input = my_code.execute_workflow()


class TestClass:
    def test_001_general_hashtag_file(self):
        assert config.general_hashtag_file == input.general_hashtag_file

    def test_002_essential_hashtag_file(self):
        assert config.essential_hashtag_file == input.essential_hashtag_file

    def test_002_output_hashtag_file(self):
        assert config.output_hashtag_file == input.output_hashtag_file
