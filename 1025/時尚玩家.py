# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:16:27 2023

@author: USER
"""


import requests

from bs4 import BeautifulSoup

url = "https://supertaste.tvbs.com.tw/food"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }


data = requests.get(url,headers=header).text

soup = BeautifulSoup(data,'html.parser')

# contents = soup.find('div',class_='article__content')

contents = soup.find('div',{"class":'article__content'})


foods = contents.find_all('a')


for item in foods:
    title = item.find('h3').text.strip()
    img = item.find('img').get('data-original')
    post_date = item.find('span').text.strip()
    link = 'https://supertaste.tvbs.com.tw'+item.get('href')
    
    
    print(title)
    print(img)
    print(link)
    print(post_date)
    print()