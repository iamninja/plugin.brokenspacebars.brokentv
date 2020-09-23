# -*- coding: utf-8 -*-

import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from resources.lib.models.movie import Movie
from resources.lib.models.series import Series, Episode

baseUrl = "http://hbbtv.ert.gr/pub/smarttv/ert"
getFeedEndPoint = "/getFeedContent.php"
newLayoutEndPoint = "/feed_NewLayout.php"

def create_url(id=""):
    if id == "":
        return baseUrl + newLayoutEndPoint
    else:
        return baseUrl + getFeedEndPoint + "?categoryIdnam=" + id


def get_json_response(id = ""):
    url = create_url(id)
    print(url)
    resp = requests.get(url=url)
    resp.encoding = resp.apparent_encoding
    h = HTMLParser()
    content = h.unescape(resp.text)
    return json.loads(content.encode('utf-8'))

def get_movie_list():
    json_dump = get_json_response("tainies")
    movie_list_json = json_dump['elems'][0]['items']
    movie_list = []
    for movie in movie_list_json:
        movie_list.append(Movie(
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
            series_ep_num = movie['series_ep_num']
        ))
    return movie_list

def get_series_list_index(series_type):
    switcher = {
        "tv": u'TV Σειρές',
        "web": u'Web Σειρές',
        "documentaries": u'Ξένα Ντοκιμαντέρ',
        "greek_documentaries": u'Ελληνικά Ντοκιμαντέρ',
        "entertainment": u'Ψυχαγωγία',
        "interviews": u'Συνεντεύξεις',
        "sports": u'Αθλητικά',
        "cartoons": u'Διασκέδαση',
        "learn_at_home": u'Μαθαίνουμε στο σπίτι',
        "ert_remembers": u'Η ΕΡΤ θυμάται'
    }
    return switcher.get(series_type)

def get_list_from_json(json_dump, series_type):
    return next(item['items'] for item in json_dump['services'] 
        if (item['masterCategory']) == get_series_list_index(series_type) or
            (item['title']) == get_series_list_index(series_type))

def get_title(title, feed):
    if title != "":
        return title
    else:
        resp = requests.get(feed)
        resp.encoding = resp.apparent_encoding
        h = HTMLParser()
        content = h.unescape(resp.text)
        soup = BeautifulSoup(content, 'html.parser')
        return soup.channel.title.string
        


def get_series_list(series_type):
    json_dump = get_json_response()
    # tvseries_list_json = json_dump['services'][get_series_list_index(series_type)]['items']
    tvseries_list_json = get_list_from_json(json_dump, series_type)
    # pprint(tvseries_list_json)
    tvseries_list = []
    for tvseries in tvseries_list_json:
        tvseries_list.append(Series(
            title = get_title(tvseries['title'], tvseries['feedurl']),
            idnam = tvseries['idnam'],
            menu_img_url = tvseries['menu_img_url'],
            bg_img_url = tvseries['bg_img_url'],
            short_desc = tvseries['short_desc'],
            sima_katallilotitas = tvseries['sima_katallilotitas']
        ))
    return tvseries_list

def get_episode_list(id):
    json_dump = get_json_response(id)
    episode_list_json = json_dump['elems'][0]['items']
    episode_list = []
    for episode in episode_list_json:
        episode_list.append(Episode(
            title = episode['title'],
            mp4 = episode['mp4'],
            dur = episode['dur'],
            desc = episode['desc'],
            short_desc = episode['short_desc'],
            actors = episode['actors'],
            episode_num = episode['episode_num'],
            season_num = episode['season_num'],
            directors = episode['directors'],
            expiration_date = episode['expiration_date'],
            pubdate = episode['pubdate'],
            image = episode['image'],
            org = episode['org'],
            bg_img_url = episode['bg_img_url'],
            menu_img_url = episode['menu_img_url'],
            sima_katallilotitas = episode['sima_katallilotitas'],
            series_ep_num = episode['series_ep_num']
        ))
    return episode_list



    

