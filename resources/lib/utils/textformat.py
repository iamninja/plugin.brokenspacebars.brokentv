# -*- coding: utf-8 -*-

import re
from HTMLParser import HTMLParser
from StringIO import StringIO

# Strip ml tags i.e. <...>
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# Strip ml tags - regex edition
def strip_tags_re(html):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', html)

# Format list item label
def get_label(title, expiration):
    if (expiration):
        return (title + "[CR]" + "[COLOR red]" + "[LIGHT]" +
        "(Available until " + expiration + ")" + 
        "[/LIGHT]" + "[/COLOR]")
    else:
        return (title)