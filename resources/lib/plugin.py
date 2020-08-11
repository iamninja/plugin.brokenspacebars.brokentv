# -*- coding: utf-8 -*-

import routing
import logging
import xbmcaddon
import re
from urllib import urlencode
from resources.lib.utils import kodiutils
from resources.lib.utils import kodilogging
from resources.lib.utils.textformat import get_label
from resources.lib.hbbtvert import hbbtvert
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory, setContent

ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()

@plugin.route('/')
def index():
    print("got in")
    addDirectoryItem(plugin.handle, 
        plugin.url_for(show_movies), ListItem("Movies"), True)
    addDirectoryItem(plugin.handle, 
        plugin.url_for(show_series, "tv"), ListItem("TV Series"), True)
    addDirectoryItem(plugin.handle, 
        plugin.url_for(show_series, "web"), ListItem("Web Series"), True)
    addDirectoryItem(plugin.handle, 
        plugin.url_for(show_series, "documentaries"), ListItem("Documentaries"), True)
    addDirectoryItem(plugin.handle, 
        plugin.url_for(show_series, "greek_documentaries"), ListItem("Greek Documentaries"), True)
    addDirectoryItem(plugin.handle, 
        plugin.url_for(show_series, "entertainment"), ListItem("Entertainment"), True)
    addDirectoryItem(plugin.handle, 
        plugin.url_for(show_series, "interviews"), ListItem("Interviews"), True)
    addDirectoryItem(plugin.handle, 
        plugin.url_for(show_series, "sports"), ListItem("Sports"), True)
    addDirectoryItem(plugin.handle, 
        plugin.url_for(show_series, "cartoons"), ListItem("Cartoons"), True)
    addDirectoryItem(plugin.handle, 
        plugin.url_for(show_series, "learn_at_home"), ListItem("Learn At Home"), True)
    addDirectoryItem(plugin.handle, 
        plugin.url_for(show_series, "ert_remembers"), ListItem("ERT Remembers"), True)
    endOfDirectory(plugin.handle)
    


@plugin.route('/category/movies')
def show_movies():
    movie_list = hbbtvert.get_movie_list()
    setContent(plugin.handle, 'video')
    for movie in movie_list:
        list_item = ListItem(label=(get_label(movie.title, movie.expiration_date)))
        list_item.setLabel2(movie.expiration_date)
        list_item.setInfo('video', movie.getMovieInfo())
        list_item.setArt(movie.getMovieArt())
        list_item.setProperty('IsPlayable', 'true')
        url = movie.mp4
        is_folder = False
        addDirectoryItem(plugin.handle, url, list_item, is_folder)
    endOfDirectory(plugin.handle)

@plugin.route('/category/series/<series_type>')
def show_series(series_type):
    series_list = hbbtvert.get_series_list(series_type)
    setContent(plugin.handle, 'video')
    for series in series_list:
        list_item = ListItem(label=(series.title))
        # list_item.setLabel2(movie.expiration_date)
        list_item.setInfo('video', series.getSeriesInfo())
        list_item.setArt(series.getSeriesArt())
        list_item.setProperty('IsPlayable', 'false')
        url = plugin.url_for(show_episodes, series_type, series.idnam)

        is_folder = True
        addDirectoryItem(plugin.handle, url, list_item, is_folder)
    endOfDirectory(plugin.handle)

@plugin.route('/category/series/<series_type>/<idnam>')
def show_episodes(series_type, idnam):
    episode_list = hbbtvert.get_episode_list(idnam)
    setContent(plugin.handle, 'video')
    for episode in episode_list:
        list_item = ListItem(label=(get_label(episode.title, episode.expiration_date)))
        # list_item.setLabel2(episode.expiration_date)
        list_item.setInfo('video', episode.getEpisodeInfo())
        list_item.setArt(episode.getEpisodeArt())
        list_item.setProperty('IsPlayable', 'true')
        url = episode.mp4
        is_folder = False
        addDirectoryItem(plugin.handle, url, list_item, is_folder)
    endOfDirectory(plugin.handle)

def run():
    plugin.run()
