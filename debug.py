# Quick & dirty code to do mass calculations of yoy returns for 2012
# Rufino Mendoza 1/1/2013
# Should eventually add sys argv

from pandas import ols, DataFrame
from pandas.stats.moments import rolling_std
from pandas.io.data import DataReader
import datetime
from os.path import exists

test = DataReader("MO", "yahoo", start=datetime.datetime(2011, 12, 30))
print test.ix[0]