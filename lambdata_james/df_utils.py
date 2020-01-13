"""
utility functions for working with DataFrames
"""

import pandas as pd
from sklearn.model_selection import train_test_split

TEST_DF = pd.DataFrame([1,2,3])

#find and return nulls
def three_way_split(X):
    '''
    Perform train, test, val split on input dataframe
    '''
    train, test = train_test_split(X)
    train, val = train_test_split(train)
    return train, test, val

def add_to_df(X, lst, name):
    '''
    Add a list to a dataframe with a given column name. Input dataframe, list, name
    '''
    X[name] = lst
    return X