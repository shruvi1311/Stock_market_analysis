# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:03:51 2022

@author: shruvi shah
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import time
#f=open("stock_market.csv","r")

plots=pd.read_csv("stock_market.csv")
x=[i.split(" ")[1].split(".")[0] for i in plots['Date']]
f=open("stock_market.csv","r")
symbol=f.readline().split(",")
print(symbol)
# y=plots[symbol[1]]
# z=plots[symbol[2]]
# print(x)
# print(y)
# print(z)
# plt.plot(x,y,color='r')
# plt.plot(x,z,c='b')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.show()