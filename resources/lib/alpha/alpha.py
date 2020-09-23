# -*- coding: utf-8 -*-

import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser

baseUrl = "https://www.alphatv.gr/"

def get_live_url():
    resp = requests.get(url=(baseUrl + 'live/'))
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'html.parser')
    live_url = soup.find(id="player").get('data-liveurl')
    # print('###############################')
    # print(live_url)
    # print('###############################')
    return live_url
