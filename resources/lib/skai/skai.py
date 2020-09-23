# -*- coding: utf-8 -*-

import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser

baseUrl = "https://www.skaitv.gr/"

def get_live_url():
    resp = requests.get(url=(baseUrl + 'live/'))
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'html.parser')
    scripts = soup.find('script', type='application/ld+json')
    res = json.loads(scripts.string)
    print('###############################')
    print(res)
    print('###############################')
