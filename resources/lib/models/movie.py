from resources.lib.utils.textformat import strip_tags


class Movie:
    def __init__(self,
    title, mp4, dur, desc, short_desc, expiration_date, pubdate,
    image, org, bg_img_url, menu_img_url,
    sima_katallilotitas, series_ep_num):
        self.title = title
        self.mp4 = mp4
        self.dur = dur
        self.desc = strip_tags(desc)
        self.short_desc = short_desc
        self.expiration_date = expiration_date
        self.pubdate = pubdate
        self.image = image
        self.org = org
        self.bg_img_url = bg_img_url
        self.menu_img_url = menu_img_url
        self.sima_katallilotitas = sima_katallilotitas
        self.series_ep_num = series_ep_num