import unittest
import pandas as pd
from df_utils import three_way_split

class UtilsTest(unittest.TestCase):
    '''Test df_utils functions'''
    def split_test(self):
        self.assertRaises(TypeError, three_way_split, not pd.DataFrame)