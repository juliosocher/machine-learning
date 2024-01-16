import pandas as pd 
import numpy as np

monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael palin'])

full_monte = pd.DataFrame({'name': monte, 
                           'info': ['B|C|D', 'B|D', 'A|C', 'B|D', 'B|C', 'B|C|D']})

full_monte['info'].str.get_dummies('|')