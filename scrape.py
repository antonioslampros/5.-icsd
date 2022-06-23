
# Search for lines that start with From and have an at sign
import urllib.request, urllib.parse, urllib.error
import re
import requests
import numpy as np
import pandas as pd
import lxml.html
def getMarketCapAndVol(links):
    i=0
    name = []
    market_cap = []
    volume_24 = []
    price_change_24 = []
    price = []
    for link in links:
        if i <=5:
            link.decode()
            html = requests.get('https://www.coindesk.com'+link.decode())
            doc = lxml.html.fromstring(html.content)
            name.append( doc.xpath('//h1[@class="typography__StyledTypography-owin6q-0 jZEoye long-title"]/text()')[0]) # 24h%
            price_change_24.append(doc.xpath('//h6[@class="typography__StyledTypography-owin6q-0 bclXpS"]/text()')[0]) # 24h%
            price.append( doc.xpath('//span[@class="typography__StyledTypography-owin6q-0 ktzuAh"]/text()')[0]) # current price
            market_cap.append(doc.xpath('//p[@class="typography__StyledTypography-owin6q-0 fIdWRj"]/text()')[0].strip("B").strip("$"))
            volume_24.append(doc.xpath('//p[@class="typography__StyledTypography-owin6q-0 fIdWRj"]/text()')[1].strip("$"))
            #df2.append(name,market_cap[0],market_cap[1],price_change_24[0],price[0])
            i += 1
    df2 = pd.DataFrame(
    {
            "Name":name,
            "Market Cap":market_cap,
            "24H Volume":volume_24,
            "24H Change":price_change_24,
            "Price":price,
    })
            #df2 = pd.DataFrame(name)
    print(df2)
        
    df2.to_excel("output.xlsx")
    

url = 'https://www.coindesk.com/data/'
html = urllib.request.urlopen(url).read()
links = re.findall(b'href=\"(/price.*?)\"', html)
getMarketCapAndVol(links)
#for link in links:
#print(link.decode())
#print(links[0].decode())
#print(links[1].decode())
#print(links[2].decode())
#print(links[3].decode())

# #print(links[4].decode())
# new_link = 'https://www.coindesk.com'+links[0].decode()

# inner_page   = urllib.request.urlopen(new_link).read()
# page = requests.get('https://www.coindesk.com/price/bitcoin/')
# html = requests.get('https://www.coindesk.com'+links[0].decode())
# getMarketCapAndVol(html)
# doc = lxml.html.fromstring(html.content)
 
#This will create a list of buyers:

#This will create a list of prices

#prices = tree.xpath('//span[@class="item-price"]/text()')
# inner_page   = urllib.request.urlopen(new_link).read()
# inner_links = re.findall(b'<div class="Box-sc-1hpkeeg-0 ', inner_page)

# Co