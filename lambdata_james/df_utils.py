"""
utility functions for working with DataFrames
"""

import pandas as pd
from sklearn.model_selection import train_test_split


class Thing:
    '''
    Representation of a thing with a name and action
    '''
    def __init__(self, name, action):
        self.name = name
        self.action = action
    
    def about_thing(self):
        print(f'This thing is a {self.name}, it can {self.action}')


#find and return nulls
def three_way_split(X):
    '''
    Perform train, test, val split on input dataframe
    '''
    train, test = train_test_split(X)
    train, val = train_test_split(train)
    return train, test, val

def add_col(X, lst, name):
    '''
    Add a list to a column as dataframe. Input dataframe, list, name
    '''
    X[name] = lst
    return X