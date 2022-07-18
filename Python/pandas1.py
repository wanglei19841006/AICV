import pandas as pd 
import datetime
from pandas_datareader import data, wb
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2015,8,1)
end = datetime.datetime(2015,8,26)

df = data.DataReader('XOM', 'yahoo', start, end)
print(df.head())

df['High'].plot()
plt.legend()
plt.show()