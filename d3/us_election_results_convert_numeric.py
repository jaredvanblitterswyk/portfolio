# -*- coding: utf-8 -*-
"""
Convert state results (strings) to numeric values.

Author: Jared Van Blitterswyk
Date Created: 2021-07-02

"""
import csv
import pandas as pd
import numpy as np

df = pd.read_csv('us_election_results_by_state.csv', index_col = 0, header = 0) 

# replace NaNs with value of 6 (not a state/no vote at the time)
df.fillna(6, inplace = True)

# replace remaining values with dictionary mapping
dict_replace = {'D': 0, 'R': 1, 'I': 2,
                'SR': 3, 'AI': 4, 'PR': 5}

# replace winning party acronym with number for plotting
df.replace(dict_replace, inplace = True)

# show unique winning parties for a given year
year = '2020'
print(df[year].unique())

# export cleaned dataframe to csv
filename = 'us_election_results_by_state_cleaned.csv'
df.to_csv(filename)