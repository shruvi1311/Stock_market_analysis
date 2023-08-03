import bs4
import requests
from bs4 import BeautifulSoup


r = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
soup = bs4.BeautifulSoup(r.text,"lxml")
print(soup)
k = soup.find('div',{'class':"D(ib) Va(m) Maw(65%) Ov(h)"})
print(k)

