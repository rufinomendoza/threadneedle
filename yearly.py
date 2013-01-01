# Quick & dirty code to do mass calculations
# Rufino Mendoza 1/1/2013
# Should eventually add sys argv and import functions

from pandas import ols, DataFrame
from pandas.stats.moments import rolling_std
from pandas.io.data import DataReader
import datetime
from os.path import exists

# This function just gets the raw data and finds the raw yoy
def yoy(symbol):
	start = DataReader(symbol, "yahoo", start=datetime.datetime(2011, 12, 30), end=datetime.datetime(2011, 12, 30))
	end = DataReader(symbol, "yahoo", start=datetime.datetime(2012, 12, 31), end=datetime.datetime(2012, 12, 31))
	# Eventually want to automate this so it's the last weekday of the year
	return end["Adj Close"].ix[0]/start["Adj Close"].ix[0]-1

# Then we format it so it can be written to a file in a human readable output
def yoy_formatted(asset_class):
	yoy_formatted = []
	for stock in asset_class:
		yoy_fmt = str(yoy(stock))	
		yoy_formatted.append(stock)
		yoy_formatted.append(",")
		yoy_formatted.append(yoy_fmt)
		yoy_formatted.append("\n")
	print yoy_formatted
	return yoy_formatted

# Actual writing of the file
def write(label, asset_class):
	filename='%s.csv' % label
	lines = yoy_formatted(asset_class)
	exists(filename)
	out_file = open(filename, 'w')
	out_file.writelines(lines)
	out_file.close()

# Enter the sets of assets you want to compare
ixn = ['AAPL', 'ORCL']
dow = ['XOM', 'GE']

# For each item in the dictionary, the key will double as the name of the file that is outputted
types = {'Tech Companies': ixn,'Dow Jones': dow}

for i, v in types.iteritems():
	write(i, v)