from pandas import Series, DataFrame,Panel
import datas as pd

import pandas as pd
import pasdas.io.data as web

tickers = ['AAPL', 'GS']
sd = '1/1/2000'
ed = '6/1/2012'
px = Panel({t: web.get_data_yahoo(t,sd,ed) for t in tickers})

#
close.save('pickled')
read = pd.load ('pickled')
read
#

close.to_csv('csv')
csv = pd.read_csv('csv', index_col=, parse_dates=True) #idx parse
csv.index[0]

px.ix[10:20, 'AAPL']
px.ix[10:20, 'GS']

pl = px.copy()
zero_neg_mask = pl <= 0
pl[zero_neg_mask] = np.nan
pl.ix[10:20, 'AAPL']

filled = p1.fillna(method='ffill')
filled.ix[10:20, 'AAPL']

limited = p1.fillna(method='ffill',limit=2)
filled.ix[10:20,'AAPL']


pl.AAPL.rank()