"""
test_my_lib is explicit
"""
import sys
import os

# This is for retrieve the parent folder in the pythonpath
# which help us for the import
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
PARENT_FOLDER = os.path.dirname(CURRENT_FOLDER)
sys.path.append(PARENT_FOLDER)
from lib.my_lib import func_to_test


def test_func_to_test():
    """
    docstring for test_func_to_test
    """
    assert func_to_test(1, 4) == 5
