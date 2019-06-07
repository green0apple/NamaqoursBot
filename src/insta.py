#-*- coding:utf-8 -*-
import sys
import os
import urllib.request
import json
import configparser
import telegram
import threading
import time
import datetime
from bs4 import BeautifulSoup

#<script type="text/javascript">window._sharedData = {json....}
#__INSTA_JSON_TAG = 'script'
#__INSTA_JSON_TAG_ATTRS = {'type':'text/javascript'}
#__INSTA_JSON_TAG_TEXT = 'window._sharedData = '
#__INSTA_URL = 'https://www.instagram.com/'
#__INSTA_TIMELINE_NODE = '/p/'

class Instagram:
	def __init__(self) :
		#<script type="text/javascript">window._sharedData = {json....}
		self.__INSTA_JSON_TAG = 'script'
		self.__INSTA_JSON_TAG_ATTRS = {'type':'text/javascript'}
		self.__INSTA_JSON_TAG_TEXT = 'window._sharedData = '
		self.__INSTA_URL = 'https://www.instagram.com/'
		self.__INSTA_TIMELINE_NODE = '/p/'

	def GetProfilePage(self, sID) :
		#Get Insta timeline
		reqInsta = urllib.request.Request(self.__INSTA_URL + sID)
		rspInsta = urllib.request.urlopen(reqInsta)
		soupInsta = BeautifulSoup(rspInsta.read(), 'html.parser')
		arTags = soupInsta.findAll(self.__INSTA_JSON_TAG, attrs=self.__INSTA_JSON_TAG_ATTRS)

		#Find Insta timeline info(json)
		sJson = ''
		for Tag in arTags :
			if Tag.text.find(self.__INSTA_JSON_TAG_TEXT) != -1 :
				sJson = Tag.text
				break
			#--end of if
		#--end of for

		#make json format
		sJson = sJson[sJson.index(self.__INSTA_JSON_TAG_TEXT) + len(self.__INSTA_JSON_TAG_TEXT):]
		sJson = sJson[:len(sJson)-1]
		sJson = '[' + sJson + ']'
		return json.loads(sJson)
	#--end of GetInstaProfilePage

	def GetTimeline(self, jsEdge) :
		sShortcode = jsEdge['node']['shortcode']
		#Get contents of timeline(html)
		sLink = self.__INSTA_URL + self.__INSTA_TIMELINE_NODE + sShortcode
		reqInsta = urllib.request.Request(sLink)
		rspInsta = urllib.request.urlopen(reqInsta)
		#Parse html
		soupInsta = BeautifulSoup(rspInsta.read(), 'html.parser')
		#Get contents of timeline(text)
		tagTitle = soupInsta.find('title')
		sContents = tagTitle.text

		#remove title
		sContents = sContents[sContents.index(':') + 1:]
		
		return {'contents': sContents, 'link': sLink}
	#--end of GetTimelines
#--end of class Instagram



