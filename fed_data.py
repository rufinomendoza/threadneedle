from pandas import ols, DataFrame
from pandas.stats.moments import rolling_std
from pandas.io.data import DataReader
import datetime
import numpy as np
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt

def series_dates(year, month, day):
	return datetime.datetime(year, month, day)

start_date = series_dates(1990, 1, 1)
end_date = series_dates(2012, 6, 30) #or datetime.datetime.today()

# Equity Index

sp500 = DataReader("SP500", "fred", start=start_date, end=end_date)["VALUE"]

# Yield Curve

treas_30_year = DataReader("DGS30", "fred", start=start_date, end=end_date)["VALUE"]
treas_20_year = DataReader("DGS20", "fred", start=start_date, end=end_date)["VALUE"]
treas_10_year = DataReader("DGS10", "fred", start=start_date, end=end_date)["VALUE"]
treas_7_year = DataReader("DGS7", "fred", start=start_date, end=end_date)["VALUE"]
treas_5_year = DataReader("DGS5", "fred", start=start_date, end=end_date)["VALUE"]
treas_3_year = DataReader("DGS3", "fred", start=start_date, end=end_date)["VALUE"]
treas_2_year = DataReader("DGS2", "fred", start=start_date, end=end_date)["VALUE"]
treas_1_year = DataReader("DGS1", "fred", start=start_date, end=end_date)["VALUE"]
treas_6_month = DataReader("DGS6MO", "fred", start=start_date, end=end_date)["VALUE"]
treas_3_month = DataReader("DGS3MO", "fred", start=start_date, end=end_date)["VALUE"]
treas_1_month = DataReader("DGS1MO", "fred", start=start_date, end=end_date)["VALUE"]

# plt.plot(sp500)
# plt.savefig('sp500')