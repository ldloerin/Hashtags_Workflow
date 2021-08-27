import os
import sys
file_path = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(os.path.split(file_path)[0])
from Services.Config.get_input import GetInput


class RunGetInput(GetInput):
    def execute_workflow(self):
        return self
