import pandas as pd
import numpy as np
from pandas import Series, DataFrame

train = pd.read_csv('data/train.csv')

#set up ticket price bins
fare_ceiling = 40
idx = pd.IndexSlice
mask = train.loc[:, idx['Fare']] > fare_ceiling
train[mask] = fare_ceiling - 1