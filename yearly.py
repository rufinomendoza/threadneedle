# Quick & dirty code to do mass calculations of yoy returns for 2012
# Rufino Mendoza 1/1/2013
# Should eventually add sys argv

from pandas import ols, DataFrame
from pandas.stats.moments import rolling_std
from pandas.io.data import DataReader
import datetime
from os.path import exists

# This function just gets the raw data and finds the raw yoy
def yoy(symbol):
	start = DataReader(symbol, "yahoo", start=datetime.datetime(2011, 12, 30))
	end = DataReader(symbol, "yahoo", start=datetime.datetime(2012, 12, 31), end=datetime.datetime(2012, 12, 31))
	print symbol
	# Eventually want to automate this so it's the last weekday of the year
	return end["Adj Close"].ix[0]/start["Adj Close"].ix[0]-1

# Create a dictionary with assets sorted in descending order of return
def all_assets_yoy(asset_class):
	d = {}
	for stock in asset_class:
		yoy_chg = yoy(stock)
		d[stock] = yoy_chg
	return d

# Then we format it so it can be written to a file in a human readable output
def yoy_fmt(asset_class):
	yoy_fmt = []
	for stock in asset_class:
		yoy_string = str(yoy(stock))
		yoy_fmt.append(stock)
		yoy_fmt.append(",")
		yoy_fmt.append(yoy_string)
		yoy_fmt.append("\n")
	return yoy_fmt

# Does the same thing as yoy_fmt but sorted by return
def sorted_yoy_fmt(asset_class):
	data = all_assets_yoy(asset_class)
	output = []
	for i, v in sorted(data.iteritems(), key=lambda (k,v): (v,k), reverse=True):
		output.append(i)
		output.append(",")
		output.append(str(v))
		output.append("\n")
	return output

# Can import list of securities from csv file
# Make sure class A and B stock symbols correspond to the yahoo finance symbology
def import_data(filename):
	in_file = open(filename, 'r')
	data = []
	for row in in_file:
		data.append(row.strip())
	in_file.close()
	return data

# Actual writing of the file
def write(label, asset_class):
	filename='%s.csv' % label
	lines = sorted_yoy_fmt(asset_class)
	exists(filename)
	out_file = open(filename, 'w')
	out_file.writelines(lines)
	out_file.close()

# Enter the sets of assets you want to compare
spx_index = import_data('sp500_input.csv')
ixn = ['AAPL', 'ORCL', 'MSFT', 'GOOG', 'BRCM']
dow = ['XOM', 'GE']

# For each item in the dictionary, the key will double as the name of the file that is outputted
# Select what you actually want to write a file for
types = {'Tech' : ixn}

for i, v in types.iteritems():
	write(i, v)