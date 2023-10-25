# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 00:08:49 2023

@author: Administrator
"""



import requests

from bs4 import BeautifulSoup



url = "https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
    }

data = requests.get(url,headers=header).text


soup = BeautifulSoup(data,'html.parser')

contents = soup.find(id="exchangeRate")

rate = contents.find_all('tr',class_='currency')

for item in rate:
    tds = item.find_all('div')
    money = tds[0].text.strip()
    allmoney = money.split()
    print(allmoney[0],allmoney[1])
    print(tds[5].text)
    print(tds[6].text)
    print(tds[7].text)
    print(tds[8].text)
    print(tds[9].text)
    print(tds[10].text)
    print()


    