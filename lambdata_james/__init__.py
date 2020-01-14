'''
Lambdata is a collection of data science helper functions
'''
import pandas as pd
import numpy as np

class Thing:
    '''
    Representation of a thing with a name and action
    '''
    def __init__(self, name, action):
        self.name = name
        self.action = action
    
    def about_thing(self):
        print(f'This thing is a {self.name}, it can {self.action}')

#sample df
ones = pd.DataFrame(np.ones(10))
zeros = pd.DataFrame(np.zeros(50))

