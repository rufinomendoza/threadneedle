import pickle
import sys

if (len(sys.argv) == 1):
   portfolio = pickle.load('portfolio.pkl')
   print portfolio

if(str(sys.argv[1]) == 'init'):
   portfolio = str(input('Please add a company'))
   pickle.dump(portfolio, 'portfolio.pkl', 'wb')
   portfolio = pickle.load('portfolio.pkl')

elif(str(sys.argv[1]) == 'del'):
   portfolio = pickle.load('portfolio.pkl')
   filter (lambda x: x != 2, portfolio)
   pickle.dump(portfolio, 'portfolio.pkl', 'wb')
   portfolio = pickle.load('portfolio.pkl')
   print portfolio

elif(str(sys.argv[1]) == 'add'):
   portfolio = pickle.load('portfolio.pkl')
   portfolio.append(x)
   pickle.dump(portfolio, 'portfolio.pkl', 'wb')
   portfolio = pickle.load('portfolio.pkl')
   print portfolio

else:
   print 'Invalid input selection\n'
