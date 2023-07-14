from bs4 import BeautifulSoup
from lxml import etree
import requests 
from url import *

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
def amd():  
    print("----------------")
    print("RX6600 Tracking")
    print("----------------") 
    # xfx/
    webpage = requests.get(xfx,headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    print("xfx -->",dom.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]')[0].text)
    # MSI
    webpage1 = requests.get(msi,headers=HEADERS)
    soup1 = BeautifulSoup(webpage1.content, "html.parser")
    dom1= etree.HTML(str(soup1))
    print("msi -->",dom1.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]')[0].text)
    # Asus
    webpage2 = requests.get(asus,headers=HEADERS)
    soup2 = BeautifulSoup(webpage2.content, "html.parser")
    dom2= etree.HTML(str(soup2))
    print("asus -->",dom2.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]')[0].text)
    # Gigabyte
    webpage3 = requests.get(gigabyte,headers=HEADERS)
    soup3 = BeautifulSoup(webpage3.content, "html.parser")
    dom3= etree.HTML(str(soup3))
    print("Gigabyte -->",dom3.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]')[0].text)
    print("----------------")
    print("Fine tracking rx 6600")
    print("----------------")
