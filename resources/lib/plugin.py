# -*- coding: utf-8 -*-

import routing
import logging
import xbmcaddon
import re
from urllib import urlencode
from resources.lib.utils import kodiutils
from resources.lib.utils import kodilogging
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
    addDirectoryItem(plugin.handle, plugin.url_for(
        show_category, "movies"), ListItem("Movies"), True)
    # addDirectoryItem(plugin.handle, plugin.url_for(
    #     show_category, "two"), ListItem("Category Two"), True)
    endOfDirectory(plugin.handle)


@plugin.route('/category/<category_id>')
def show_category(category_id):
    dump = hbbtvert.get_json_response("categoryIdnam=tainies")
    movies = hbbtvert.get_movies_list(dump)
    setContent(plugin.handle, 'video')
    for movie in movies:
        list_item = ListItem(label=(movie.title + 
        "[CR]" + "[COLOR red]" + "[LIGHT]" +"(Available until " + movie.expiration_date + ")" + "[/LIGHT]" + "[/COLOR]"))
        list_item.setLabel2(movie.expiration_date)
        list_item.setInfo('video', {
            'plot': movie.desc,
            'plotoutline': movie.short_desc
        })
        list_item.setArt({'fanart': movie.org,
                            'thumb': movie.image})
        list_item.setProperty('IsPlayable', 'true')
        url = movie.mp4
        is_folder = False
        addDirectoryItem(plugin.handle, url, list_item, is_folder)
    endOfDirectory(plugin.handle)

def run():
    plugin.run()
