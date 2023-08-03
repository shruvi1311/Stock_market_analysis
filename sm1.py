import os
import csv
import pandas as pd

live_market_index = {
         'Broad Market Indices': ['NIFTY 50', 'NIFTY NEXT 50', 'NIFTY MIDCAP 50', 'NIFTY MIDCAP 100',
                                  'NIFTY MIDCAP 150', 'NIFTY SMALLCAP 50', 'NIFTY SMALLCAP 100',
                                  'NIFTY SMALLCAP 250', 'NIFTY MIDSMALLCAP 400', 'NIFTY 100', 'NIFTY 200'],
         'Sectoral Indices': ["NIFTY AUTO", "NIFTY BANK", "NIFTY ENERGY", "NIFTY FINANCIAL SERVICES",
                              "NIFTY FINANCIAL SERVICES 25/50", "NIFTY FMCG", "NIFTY IT", "NIFTY MEDIA",
                              "NIFTY METAL", "NIFTY PHARMA", "NIFTY PSU BANK", "NIFTY REALTY",
                              "NIFTY PRIVATE BANK"],
         'Others': ['Securities in F&O', 'Permitted to Trade'],
         'Strategy Indices': ['NIFTY DIVIDEND OPPORTUNITIES 50', 'NIFTY50 VALUE 20', 'NIFTY100 QUALITY 30',
                              'NIFTY50 EQUAL WEIGHT', 'NIFTY100 EQUAL WEIGHT', 'NIFTY100 LOW VOLATILITY 30',
                              'NIFTY ALPHA 50', 'NIFTY200 QUALITY 30', 'NIFTY ALPHA LOW-VOLATILITY 30',
                              'NIFTY200 MOMENTUM 30'],
         'Thematic Indices': ['NIFTY COMMODITIES', 'NIFTY INDIA CONSUMPTION', 'NIFTY CPSE', 'NIFTY INFRASTRUCTURE',
                              'NIFTY MNC', 'NIFTY GROWTH SECTORS 15', 'NIFTY PSE', 'NIFTY SERVICES SECTOR',
                              'NIFTY100 LIQUID 15', 'NIFTY MIDCAP LIQUID 15']}
a = live_market_index
def live_market_data(indices,key):
       
        #indices = "Sectoral Indices"    # input
        # key = "NIFTY FINANCIAL SERVICES 25/50"     # input
        data = session.get(f"https://www.nseindia.com/api/equity-stockIndices?index={self.live_market_index[indices][self.live_market_index[indices].index(key)].upper().replace(' ','%20').replace('&', '%26')}", headers=self.headers).json()["data"]
        df = pd.DataFrame(data)

        #return list(df["symbol"])
        return df
for i in a:
    for j in range(len(a[i])):        
        print(i,a[i][j])
        symbol=list(live_market_data(i,a[i][j])["symbol"])
       # price=list(nse.live_market_data(i,a[i][j])["lastPrice"])
        symbol.insert(0,"Date")

        a[i][j] = a[i][j].replace('/','_')
        with open(i+'/'+a[i][j]+'.csv','w') as f:
            w = csv.writer(f)
            w.writerow(symbol)
