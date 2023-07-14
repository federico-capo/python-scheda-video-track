from bs4 import BeautifulSoup
from lxml import etree
import requests 
from url import *

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
def nvidia():  
    print("----------------")
    print("RTX 3060 Tracking")
    print("----------------") 
    # msi/
    webpage = requests.get(rtx_msi,headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    print("rtx_msi -->",dom.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]')[0].text)
    # pny
    webpage1 = requests.get(rtx_pny,headers=HEADERS)
    soup1 = BeautifulSoup(webpage1.content, "html.parser")
    dom1= etree.HTML(str(soup1))
    print("rtx_pny -->",dom1.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]')[0].text)
    # zotac
    webpage2 = requests.get(rtx_zotac,headers=HEADERS)
    soup2 = BeautifulSoup(webpage2.content, "html.parser")
    dom2= etree.HTML(str(soup2))
    print("rtx_zotac -->",dom2.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]')[0].text)
    # Gigabyte
    webpage3 = requests.get(rtx_gigabyte,headers=HEADERS)
    soup3 = BeautifulSoup(webpage3.content, "html.parser")
    dom3= etree.HTML(str(soup3))
    print("rtx_gigabyte -->",dom3.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]')[0].text)
    # Asus
    webpage4 = requests.get(rtx_asus,headers=HEADERS)
    soup4 = BeautifulSoup(webpage4.content, "html.parser")
    dom4= etree.HTML(str(soup4))
    print("rtx_asus -->",dom4.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]')[0].text)
    # rtx_gainward
    webpage5 = requests.get(rtx_gainward,headers=HEADERS)
    soup5 = BeautifulSoup(webpage5.content, "html.parser")
    dom5= etree.HTML(str(soup5))
    print("rtx_gainward -->",dom5.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]')[0].text)
    
    print("----------------")
    print("Fine tracking RTX 3060")
    print("----------------")
# print("amd o nvidia"," 1 o 2")
# print("---------------------")
# print("Premi 5 per loop infinito")

# amd_nvidia = input()

# if amd_nvidia == "1" :
#     amd()
# else:
#     if amd_nvidia == "2":
#         nvidia()
#     else:
#         if amd_nvidia != "1"or"2":
#             print("per amd 1, per nvidia 2")
#             if amd_nvidia == "5":
#                 while True:
#                     amd()
#                     nvidia()




