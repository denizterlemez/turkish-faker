import pandas as pd
import random
import  os
import requests
from bs4 import BeautifulSoup
path = os.path.dirname(__file__)
from lxml import etree



def randommanname():
    df = pd.read_csv(path + "/isimler.csv")

    erkek = df[df.cinsiyet == "E"]
    xds = df[df.cinsiyet == "U"]
    edflist = erkek['isimler'].tolist()
    udflist = xds['isimler'].tolist()
    edflist.append(udflist)
    return random.choice(udflist)




def randomwomanname():
    df = pd.read_csv(path + "/isimler.csv")

    woman = df[df.cinsiyet == "K"]
    xd = df[df.cinsiyet == "U"]
    edflist = woman['isimler'].tolist()
    udflist = xd['isimler'].tolist()
    edflist.append(udflist)
    return random.choice(udflist)


def fakeaddressturkey():
    URL = "https://www.fakeaddresscopy.com/Turkey/"

    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', \
                'Accept-Language': 'en-US, en;q=0.5'})

    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    casperss = dom.xpath("//div[@class='overflow-auto']//div")[0].text
    return casperss



def fakephonenumberturkey():
    URL = "https://www.fakeaddresscopy.com/phone/Turkey/"

    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', \
                'Accept-Language': 'en-US, en;q=0.5'})

    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    casmo = dom.xpath("//div[@class='overflow-auto']//textarea[1]")[0].text
    return casmo


def cooltext():
    s = open(path+"/ozlusozler.txt", "r", encoding="utf-8")
    m = s.readlines()
    l = []
    for i in range(0, len(m) - 1):
        x = m[i]
        z = len(x)
        a = x[:z - 1]
        l.append(a)
    l.append(m[i + 1])
    mamosko = random.choice(l)
    return mamosko
    s.close()



def randomsurname():
    s = open(path+"/surnames.txt", "r", encoding="utf-8")
    m = s.readlines()
    l = []
    for i in range(0, len(m) - 1):
        x = m[i]
        z = len(x)
        a = x[:z - 1]
        l.append(a)
    l.append(m[i + 1])
    void = random.choice(l)
    return void
    s.close()
