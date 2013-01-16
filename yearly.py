# Quick & dirty code to do mass calculations of yoy returns for 2012
# Rufino Mendoza 1/1/2013

from pandas import ols, DataFrame
from pandas.io.data import DataReader
from pandas import *
import numpy as np
import datetime

from os.path import exists
import urllib, json
from math import sqrt
import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Import list of securities from csv file
# Make sure class A and B stock symbols correspond to the yahoo finance symbology
def import_data(filename):
	in_file = open(filename, 'r')
	data = [row.strip() for row in in_file]
	in_file.close()
	return data

# Looks up full security name based off stock symbol
def retrieve_name(symbol):
	url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%3D%22"+symbol+"%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	if data['query']['results'] is None:
		output = 'No response from data source'
	else:
		output = data['query']['results']['quote']['Name']
	return output

# This function just gets the raw data and finds the raw yoy
def yoy(symbol):
	data = DataReader(symbol, "yahoo", start=datetime.datetime(2011, 12, 30), end=datetime.datetime(2013, 01, 04))
	print symbol,'from',str(data.ix[0].name)[0:10],'to',str(data.ix[-1].name)[0:10]
	# Eventually want to automate this so it's the last weekday of the year
	return data["Adj Close"].ix[-1]/data["Adj Close"].ix[0]-1

# Puts the y/y returns into a series
def calc_yoy_series(asset_class):
	print ''
	print 'Retrieving performance data . . .'
	yoy_chgs = [float(yoy(stock)) for stock in asset_class]
	yoy_series = Series(yoy_chgs, index=asset_class)
	return yoy_series

# Create a data frame with assets sorted in descending order of return
def generate_yoy_table(asset_class):

	yoy_series = calc_yoy_series(asset_class)
	yoy_series.mean = Series.mean(yoy_series)
	yoy_series.std = Series.std(yoy_series)

	print ''
	print 'Standardizing data . . .'

	for stock in asset_class:
		zed_scores = [(yoy_chg - yoy_series.mean)/yoy_series.std for yoy_chg in yoy_series]
	zscore_series = Series(zed_scores, index=asset_class)

	print ''
	print 'Adding labels . . .'

	names=[retrieve_name(stock) for stock in asset_class]
	name_series = Series(names, index=asset_class)

	data = { 'name' : name_series, 'yoy' : yoy_series, 'zscore' : zscore_series }
	df = DataFrame(data, columns=['name', 'yoy', 'zscore'])
	df_sorted = DataFrame.sort(df, 'yoy', ascending=False)
	print df_sorted
	return df_sorted

def to_percent(y, position):
	# Ignore the passed in position. This has the effect of scaling the default
	# tick locations.
	s = str(100 * y)

	# The percent symbol needs escaping in latex
	if matplotlib.rcParams['text.usetex'] == True:
		return s + r'$\%$'
	else:
		return s + '%'
		
def autolabel(rects):
	# attach some text labels
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
				ha='center', va='bottom')


# Excel Writer is the proc that handles reading and writing to Excel
# writer = ExcelWriter('output.xlsx')

# This skips the first argument which is the program
args = [arg for arg in sys.argv][1::]

# For each argument, it will import the file, generate a table, and then save it to Excel.
for arg in args:
	data = import_data(str(arg))
	table = generate_yoy_table(data)
	table.to_excel(str(arg)+'.xlsx',str(arg))
	table['yoy'].plot(kind='bar')
	formatter = FuncFormatter(to_percent)
	plt.gca().yaxis.set_major_formatter(formatter)
	plt.ylabel('Y/Y % Change')
	plt.savefig(str(arg)+'.svg')
# writer.save()