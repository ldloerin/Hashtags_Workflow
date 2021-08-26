import os
import pytest
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
from Services.Config.get_input import GetInput
from Source.build_mail_address import BuildMailAddress

config = GetInput(__file__)


class TestClass:
    def test_001_build_mail_address(self):
        test_code_file = os.path.join(
            os.path.split(os.path.dirname(__file__))[0],
            config.test_code_path,
            config.test_code_name,
        )
        my_code = BuildMailAddress(test_code_file)
        my_code.execute_workflow()
        ret_value = my_code.mail_address
        assert ret_value == config.assert_value

    def test_002_simple_assert(self):
        x = 1
        y = 1
        assert x == y

    @pytest.mark.parametrize("x, y, z", [(1, 1, 2), (2, 2, 4)])
    def test_003_multiple_assert(self, x, y, z):
        assert x + y == z
