#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import random

class Crawler:
    def __init__(self, *, log=None):
        self.logger = None
        if log is not None:
            self.logger = log.add_sub_logger(__name__)

        self.user_agent = ['Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',\
                           'Mozilla/5.0 (X11; Ubuntu; Linux i686;) Firefox/27.0',\
                           'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Chrome/2.0.172.28',\
                           'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Foxy/1; InfoPath.1)',\
                           'Mobile Safari 1.1.3 (iPhone; U; CPU like Mac OS X; en)']

    def __decode(self, data, code):
        return data.content.decode(code)

    def __logger(self, info):
        None

    def get(self, url, *, payload = {}, decode='utf8'):
        headers = { 'User-Agent' : random.choice(self.user_agent) }
        data = requests.get(url, headers=headers, params=payload)
        return self.__decode(data, decode)

    def post(self, url, *, payload = {}, decode='utf8'):
        headers = { 'User-Agent' : random.choice(self.user_agent) }
        data = requests.post(url, headers=headers, params=payload)
        return self.__decode(data, decode)

"""
if __name__=="__main__":
    test = Crawler()
    print(test.post("http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php?download=csv&qdate=104/05/27&selectType=01", decode="big5"))
"""
