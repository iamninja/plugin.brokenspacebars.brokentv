# -*- coding: utf-8 -*-

from resources.lib.utils.textformat import strip_tags

class Episode:
    def __init__(self,
    title, mp4, dur, desc, short_desc, expiration_date, pubdate,
    image, org, bg_img_url, menu_img_url,
    sima_katallilotitas, series_ep_num,
    actors, directors, episode_num, season_num):
        self.title = title
        self.mp4 = mp4
        self.dur = dur
        self.desc = strip_tags(desc)
        self.short_desc = short_desc
        self.expiration_date = expiration_date
        self.actors = actors
        self.directors = directors
        self.episode_num = episode_num
        self.season_num = season_num if (season_num != "") else "1"
        self.pubdate = pubdate
        self.image = image
        self.org = org
        self.bg_img_url = bg_img_url
        self.menu_img_url = menu_img_url
        self.sima_katallilotitas = sima_katallilotitas
        self.series_ep_num = series_ep_num
    
    def getEpisodeInfo(self):
        return {
            'plot': self.desc,
            'plotoutline': self.short_desc
        }

    def getEpisodeArt(self):
        return {
            'fanart': self.org,
            'thumb': self.image
        }



class Series:
    def __init__(self,
    title, idnam, short_desc, 
    menu_img_url, bg_img_url, sima_katallilotitas):
        self.title = title
        self.idnam = idnam
        self.short_desc = strip_tags(short_desc).replace("|", "\n")
        self.bg_img_url = bg_img_url
        self.menu_img_url = menu_img_url
        self.sima_katallilotitas = sima_katallilotitas
        self.episodes = []
    
    def getSeriesInfo(self):
        return {
            'plot': self.short_desc,
            'plotoutline': self.short_desc
        }

    def getSeriesArt(self):
        return {
            'fanart': "http://hbbtv.ert.gr" + self.bg_img_url,
            'thumb': "http://hbbtv.ert.gr" + self.menu_img_url
        }