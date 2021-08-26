import os
import pytest
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
# from Services.Config.get_input import GetInput

# config = GetInput(__file__)


class TestClass:
    def test_001_dummy(self):
        x = 1
        y = 1
        assert x == y

    def test_002_simple_assert(self):
        x = 1
        y = 1
        assert x == y

    @pytest.mark.parametrize("x, y, z", [(1, 1, 2), (2, 2, 4)])
    def test_003_multiple_assert(self, x, y, z):
        assert x + y == z
