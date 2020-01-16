import unittest
import df_utils as du
import pandas as pd

class UtilTest(unittest.TestCase):
    '''Test df utils functions'''
    def split_test(self):
        self.assertRaises(TypeError, du.three_way_split, not isinstance(pd.DataFrame))