"""using pandas web data reader to extract stock prices"""
"""We will be grabbing stock data from Yahoo Finance"""
import pandas as pd 
import numpy as np
import datetime #date library
from datetime import date
import pandas_datareader.data as web
from pandas import Series, DataFrame
import plotly.graph_objects as go

#print = ("What stock do you want to analyze?")
#print = ("Notice: Use stock ticker")
#stock = input()

#Get todays date 
today = date.today()

#Find Start and End Date
start = datetime.datetime(2020, 1, 1) 
end = datetime.datetime(2020, 12, 9)
#end = datetime.datetime(today.year, today.month, today.day)
#print(end)

"""Using Dataframe Constructor"""
df = web.DataReader("PFE", 'yahoo', start, end)
df.tail()
"""Shows Last 5 rows"""
#print(df.tail(5))

"""Show the rolling mean for the past 100 days"""
close_px = df['Adj Close']
mavg = close_px.rolling(window=100).mean()

#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

#adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl._version

#Adjusting the style of matplotlib
style.use('ggplot')

close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.legend()
plt.show()

#return deviation formula
rets = close_px / close_px.shift(1)-1
rets.plot(label='return')
plt.show()

#Analysing competition stocks
dfcomp = web.DataReader(['AAPL', 'GE', 'GOOG', 'IBM', 'MSFT'], 'yahoo', start=start, end=end)['Adj Close']
#print competitor data for the last 5 day
print(dfcomp.tail())

#Correlation Analysis
retscomp = dfcomp.pct_change()
corr = retscomp.corr()
plt.scatter(retscomp.AAPL, retscomp.GE)
plt.xlabel('Returns AAPL')
plt.ylabel('Returns GE')
plt.show()

pd.plotting.scatter_matrix(retscomp, diagonal='kde', figsize=(10, 10))
plt.show()

#Using heatmaps for a correlation
plt.imshow(corr, cmap='hot', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns)
plt.show()

#Stocks returns rate and risk
plt.scatter(retscomp.mean(), retscomp.std())
plt.xlabel('Expected Returns')
plt.ylabel('Risk')
for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):
    plt.annotate(
        label,
        xy = (x, y), xytext = (20, -20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round, pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad=0'))
plt.show()

"""Predict Future Stock Prices"""
"""Pre-processing & Cross Validation will be used to clean up and process the data"""
#Libraries to predict future stock prices
import math
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#Libraries to plot data
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import style
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

#Feature Engineering
df.columns

dfreg = df.loc[:,['Adj Close', 'Volume']]
dfreg['HL_PCT'] = (df['High'] - df['Low'])/df['Close']*100.0
dfreg['PCT_Change'] = (df['Close']-df['Open']) / df['Open']*100.0
dfreg.head()
print(dfreg)

#Drop Missing value
dfreg.fillna(value=-99999, inplace=True)

#We want to separate 1% of the data to forecast
forecast_out = int(math.ceil(0.01 * len(dfreg)))

#Separating the label here, we want to predict the Adj Close
forecast_col = 'Adj Close'
dfreg['label'] = dfreg[forecast_col].shift(-forecast_out)
X = np.array(dfreg.drop(['label'], 1))

#Scale the X so that everyone can hae the same distrobution for linear regression
X = preprocessing.scale(X)

#We want to find Data Series of late X and early X (train) for model generation and evaluation
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

#separate label and identify it as y
y = np.array(dfreg['label'])
y = y[:-forecast_out]

#training data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Linear Regression
clfreg = LinearRegression(n_jobs=-1)
clfreg.fit(X_train, y_train)

#Quadratic regression 2
clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
clfpoly2.fit(X_train, y_train)

#Quadratic regression 3
clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
clfpoly3.fit(X_train, y_train)

#KNN Regression
clfknn = KNeighborsRegressor(n_neighbors = 2)
clfknn.fit(X_train, y_train)

confidencereg = clfreg.score(X_test, y_test)
confidencepoly2 = clfpoly2.score(X_test, y_test)
confidencepoly3 = clfpoly3.score(X_test, y_test)
confidenceknn = clfknn.score(X_test, y_test)

#results
print('The linear regression confidence is {}'.format(confidencereg))
print('The quadratic regression 2 confidence is {}'.format(confidencepoly2))
print('The quadratic regression 3 confidence is {}'.format(confidencepoly3))
print('The KNN confidence is {}'.format(confidenceknn))

#Stocks Forecast
forecast_set = clfreg.predict(X_lately)
dfreg['Forecast'] = np.nan
print(forecast_set)

last_date = dfreg.iloc[-1].name
last_unix = last_date
next_unix = last_unix + datetime.timedelta(days=1)

for i in forecast_set:
    next_date = next_unix
    next_unix += datetime.timedelta(days=1)
    dfreg.loc[next_date] = [np.nan for _ in range(len(dfreg.columns)-1)]+[i]
dfreg['Adj Close'].tail(500).plot()
dfreg['Forecast'].tail(500).plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()