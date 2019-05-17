#-*- coding:utf-8 -*-

import sys
import os
import urllib.request
from bs4 import BeautifulSoup

Req = urllib.request.Request('https://lineblog.me/kobayashi_aika/')
Resp = urllib.request.urlopen(Req)
soup = BeautifulSoup(Resp.read(), 'html.parser')

#print(Resp.read())
print(soup.body)
