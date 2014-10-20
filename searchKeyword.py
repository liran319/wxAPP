#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib2


class KeyWordParser(object):
    """docstring for ClassName"""
    def __init__(self, keyword):
        self.keyword = keyword
    
    def Youku(self):
        search_addr = r"http://www.soku.com/v?keyword=" + self.keyword
        return search_addr

a = KeyWordParser('火影')

url = a.Youku()
htmlpage = urllib2.urlopen(url).read()

print url
print htmlpage