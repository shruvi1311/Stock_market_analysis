# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 00:19:29 2022

@author: shruvi shah
"""

import bs4
import requests
from bs4 import BeautifulSoup

def parsePrice():
    r = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
    soup = bs4.BeautifulSoup(r.text,"lxml")
    #print(soup)
    k = soup.find('div',{'class':"My(6px) Pos(r) smartphone_Mt(6px) W(100%)"})
    price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})[0].find('fin-streamer').text
    print(price)

print(parsePrice())

# stock_names = []
# for stock in stock_picks:
#     stock_names.append(stock.h3.get_text())
# stock_names.pop()
# print(len(stock_names))

# for stock in stock_picks:
#     price = stock.aside.h4.get_text()
#     current_price.append(price.strip())
# print(current_price)
'''
current_price = stocks.find_all(class_='current-price')
# Current Price
current_p = []
for change in current_price:
    price = change.get_text()
    current_p.append(price.strip())
    
print(len(current_p))

price_change = stocks.find_all(class_='price-change-amount')
# Get Change Price
change_price = []
for change in price_change:
    price = change.get_text()
    change_price.append(price.strip())

print(len(change_price))
stock_symbol = []
for stock in stock_picks:
    stock_symbol.append(stock.a.span.get_text())
stock_symbol.pop()
print(len(stock_symbol))

percent_change = stocks.find_all(class_='price-change-percent')
# Get Change Percent
change_pct = []
for pct in percent_change:
    price = pct.get_text()
    change_pct.append(price.strip())
print(len(change_pct))

data = {'Symbol':stock_symbol, 'Company':stock_names, 'Price':current_p, 'PriceChange':change_price, 'PercentChange':change_pct}

df = pd.DataFrame(data)
df.head()
print(df)'''

