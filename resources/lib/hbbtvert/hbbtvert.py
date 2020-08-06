import requests
import json
import xbmcgui
import xbmcplugin
from HTMLParser import HTMLParser
from resources.lib.models.movie import Movie

baseUrl = "http://hbbtv.ert.gr/pub/smarttv/ert/getFeedContent.php"

def get_json_response(param):
    url = baseUrl + "?" + param
    print(url)
    resp = requests.get(url=url)
    resp.encoding = resp.apparent_encoding
    h = HTMLParser()
    content = h.unescape(resp.text)
    return json.loads(content.encode('utf-8'))

def get_movies_list(json_dump):
    movies_list = json_dump['elems'][0]['items']
    movies = []
    for movie in movies_list:
        movies.append(Movie(
            title = movie['title'],
            mp4 = movie['mp4'],
            dur = movie['dur'],
            desc = movie['desc'],
            short_desc = movie['short_desc'],
            expiration_date = movie['expiration_date'],
            pubdate = movie['pubdate'],
            image = movie['image'],
            org = movie['org'],
            bg_img_url = movie['bg_img_url'],
            menu_img_url = movie['menu_img_url'],
            sima_katallilotitas = movie['sima_katallilotitas'],
            series_ep_num = movie['series_ep_num']))
    return movies
    

