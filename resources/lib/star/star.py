# -*- coding: utf-8 -*-

import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser

baseUrl = "https://www.star.gr/"

def get_live_url():
    resp = requests.get(url=(baseUrl + 'tv/live-stream/'))
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, 'html.parser')
    live_url = soup.find_all("div", class_="video_container")[0].get("data-video")
    # print('###############################')
    # print(live_url)
    # print('###############################')
    return live_url
