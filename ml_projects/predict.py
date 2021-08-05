import pandas as pd
from datetime import datetime
import numpy as np

# read in stock prices
stocks = pd.read_csv('sphist.csv')

# convert Date columns to date-time format
stocks['Date'] = pd.to_datetime(stocks['Date'])

# sort by ascending date (default of sort_values)
stocks.sort_values(by =['Date'], axis = 0, inplace = True)
# re-index with default values to keep original index
stocks.reset_index(inplace = True)

# compute a few stock indicators 
# ----- avgerage price from last 5 days -----
# ----- std dev of price from last 5 days -----
# ----- average price from last 365 days -----
# ----- std dev of price from last 365 days -----

# I'll use a simple, more 'brute force' approach to compute the metrics instead of using time series tools built in pandas, we will use itterrows. The time series tools for computing these metrics will include the current trading day, which will cause leakage in our predictions. To avoid this we would have to reindex each row by 1 and then assign to its orginal day.

# initialize new columns
stocks['5_day_avg'] = np.zeros((len(stocks),))
stocks['5_day_stddev'] = np.zeros((len(stocks),))
stocks['365_day_avg'] = np.zeros((len(stocks),))
stocks['365_day_stddev'] = np.zeros((len(stocks),))

for index, row in stocks.iterrows():
    
    if index >= 5 and index < 365:
        past_5_days = stocks.loc[index-5:index,'Close']
        stocks.loc[index,'5_day_avg'] = past_5_days.mean()
        stocks.loc[index,'5_day_stddev'] = past_5_days.std()
    elif index >= 365:
        past_5_days = stocks.loc[index-5:index,'Close']
        past_365_days = stocks.loc[index-365:index,'Close']
        
        stocks.loc[index,'5_day_avg'] = past_5_days.mean()
        stocks.loc[index,'5_day_stddev'] = past_5_days.std()
        stocks.loc[index,'365_day_avg'] = past_365_days.mean()
        stocks.loc[index,'365_day_stddev'] = past_365_days.std()
        
# remove rows where data is missing (within 1 year of start date)
stocks = stocks[stocks['Date'] > datetime(year=1951, month=1, day=2)]
# remove any data with nans
stocks.dropna(axis=0, inplace = True)

# generate two new dataframes for fitting and model evaluation
train = stocks[stocks['Date'] < datetime(year=2013, month=1, day=1)]
test = stocks[stocks['Date'] >= datetime(year=2013, month=1, day=1)]
print('Train dataframe:')
print(train.head(5))
print('Test dataframe:')
print(test.head(5))
        
