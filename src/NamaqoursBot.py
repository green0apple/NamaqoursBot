##-*- coding:utf-8 -*-
import configparser
import json
import requests
import twitter
import time
import telegram.bot
import datetime
import urllib.request
from urllib.parse import urlparse
from threading import Thread, Lock

class TwitterSender(threading.Thread):
	def __init__(self) :
		self.__iniTwitter = configparser.RawConfigParser()
		self.__iniTwitter.read('../conf/twitter/api.ini')
		self.__iniTwitterID = configparser.RawConfigParser()
		self.__iniTwitterID.read('../conf/twitter/id.ini')
		#Set twitter API
		self.__twAPI = twitter.Api(self.__iniTwitter['NamaqoursBot']['consumer_key'],
											self.__iniTwitter['NamaqoursBot']['consumer_secret'],
											self.__iniTwitter['NamaqoursBot']['access_token_key'],
											self.__iniTwitter['NamaqoursBot']['access_token_secret'],
											tweet_mode='extended')
		#Get TwitterID, Nickname
		self.__jsOldTweets = []
		for sNumber, sID in self.__iniTwitterID.items('ID') :
			if self.__iniTwitterID.has_option('Nickname', sID) :
				self.__jsOldTweets.appand = {"id": sID, "nickname": self.__iniTwitterID['Nickname'][sID], "timeline": None, "timestamp": None}
			else :
				self.__jsOldTweets.appand = {"id": sID, "nickname": sID, "timeline": None, "timestamp": None}
		#--end of for

		#Get users timeline (default init)
		#Count of timeline return from each GetUserTimeline is 5
		for jsOldTweet in self.__jsOldTweets :
			jsOldTweet['timestamp'] = self.__twAPI.GetUserTimeline(screen_name=jsOldTweet['id'],count=5)[0].created_at;
			#Wait 1s for Twitter API policy
			time.sleep(1)
		#--end of for

	#Twitter created_at time to python datetime
	def __TwitterTimeToDatetime(sCreatedAt) :
		return time.strptime(sCreatedAt, '%a %b %d %H:%M:%S +0000 %Y')
	#--end of TwitterTimeToDatetime

	def execute(self) :
		while True :
			try :
				#Continue with changing ID
				for jsOldTweet in self.__jsOldTweets :
					#Wait 1s for twitter api policy
					time.sleep(1)
					sID = jsOldTweets['id']
					#Get timeline
					arTimeline = twAPI.GetUserTimeline(screen_name=sID,count=5)

					#Compare last tweet time with gotten timelines(5)
					arTimeline.reverse()
					for Timeline in arTimeline :
						#If last tweet time is older then new tweet, print new tweet
						if TwitterTimeToDatetime(jsOldTweet['timestamp']) < TwitterTimeToDatetime(Timeline.created_at) :
							sNickname = jsOldTweet['nickname']
							#If new tweet is retweet
							if Timeline.retweeted_status != None :
								sTweet = Timeline.retweeted_status.full_text
								sData = urllib.parse.quote(sTweet)
								sTranslated = PapagoSMT(sData)
								print('New retweet from [' + sNickname + '] at ', datetime.datetime.now())
								TelegramSendMessage(sTelegramID, 'New retweet from [' + sNickname + ']' + '\n' + '[Translated]' + '\n' + sTranslated + '\n' + '[Original]' + '\n' + sTweet)
							#--end of if
							else :
								sTweet = Timeline.full_text
								sData = urllib.parse.quote(sTweet)
								sTranslated = PapagoSMT(sData)
								print('New tweet from [' + sNickname + '] at ', datetime.datetime.now())
								TelegramSendMessage(sTelegramID, 'New tweet from [' + sNickname + ']' + '\n' + '[Translated]' + '\n' + sTranslated + '\n' + '[Original]' + '\n' + sTweet)
							#--end of else

							#Update last tweet time
							jsOldTweet['timestamp'] = Timeline.created_at
							#--end of if
						#Wait about 100ms for Papago API policy(10requests/1sec)
						time.sleep(0.11)
					#--end of for
				#--end of for
			except Exception as err:
				print('ERROR TIME : ', datetime.datetime.now())
		                print('ERROR : ', err)
		                #bug : if error is Request Timeout, can't use API(network)
		                if err != 'Timed out' :
						TelegramSendMessage(sTelegramAdmin, 'ERROR : ' + str(err))
			#--end of try
		#--end of while
	#--end of execute
#--eid of class TwitterSender

class InstaSender(threading.Thread):
	def __init__(self) :
		#Read configfile for Instagram ID
		self.__iniInstagram = configparser.RawConfigParser()
		self.__iniInstagram.read('../conf/id.ini')
		
		#Init Instagram crawler
		self.__instaCrawler = Instagram()

		#Get Insta ID, Nickname
		self.__jsOldTimelines = []
		for sNumber, sID in iniInstagram.items('ID') :
			if iniInstagram.has_option('Nickname', sID) :
				self.__jsOldTimelines.append( {"id": sID, "nickname": iniInstagram['Nickname'][sID], "timeline": {"contents": None, "timestamp": 0}} )
			else :
				self.__jsOldTimelines.append( {"id": sID, "nickname": sID, "timeline": {"contents": None, "timestamp": 0}} )
		#--end of for
		
		#Get users timeline (default init)
		#Count of timeline return from each GetUserTimeline is 5
		for jsOldTimeline in self.__jsOldTimelines :
			print(self.__jsOldTimeline['id'])
			jsEdges = self.__instaCrawler.GetProfilePage(jsOldTimeline['id'])[0]['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
			jsOldTimeline['timeline'] = self.__instaCrawler.GetTimelines(jsEdges)[0]
			#Wait 1s for decreasing crawling speed
			time.sleep(1)
		#--end of for
	#--end of __init__
	
	def execute(self) :
		while True :
			try :
				#Get old timeline to compare with new timeline
				for jsOldTimeline in jsOldTimelines :
					#Wait 1s for decreasing crawling speed
					time.sleep(1)

					#Get timeline
					jsProfile = instaCrawler.GetProfilePage(jsOldTimeline['id'])
					jsEdges = jsProfile[0]['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
					jsTimelines = self.__instaCrawler.GetTimelines(jsEdges)

					#Get new timeline to compare with old timeline
					for jsTimeline in jsTimelines :
						#If last post time is older then new one, print
						if jsOldTimeline['timeline']['timestamp'] < jsTimeline['timestamp'] :
							sNickname = jsOldTimeline['nickname']
							sTimeline = jsTimeline['contents']
							sData = urllib.parse.quote(sTimeline)
							sTranslated = PapagoSMT(sData)
							print('New timeline from [' + sNickname + '] at ', datetime.datetime.now())
							TelegramSendMessage(sTelegramID, text='New timeline from [' + sNickname + ']' + '\n' + '[Translated]' + '\n' + sTranslated + '\n' + '[Original]' + '\n' + sTimeline)

							#Update last timeline
							jsOldTimeline['timeline'] = jsTimeline

						#--end of if
					#--end of for
				#--end of for
			except Exception as err:
				print('ERROR TIME : ', datetime.datetime.now())
				print('ERROR : ', err)

				#bug : if error is Request Timeout, can't use API(network)
				if err != 'Timed out' :
					TelegramSendMessage(sTelegramAdmin, 'ERROR : ' + str(err))
			#--end of try
		print('debug::running InstagramCrawler')
		#--end of while
	#--end of execute
#--end of class InstaSender


def TelegramSendMessage(sID, sText):
	mtxTelegram.acquire()
	telBot.send_message(chat_id=sID, text=sText)
	mtxTelegram.release()
#--end of TelegramSendMessage

def PapagoSMT(sText):
	mtxPapago.acquire()
	sText = PAPAGO_JP_TO_KR_QUERY + sText
	PapagoResp = urllib.request.urlopen(reqPapago, data=sText.encode('utf-8'))
	return json.loads(PapagoResp.read().decode('utf-8'))['message']['result']['translatedText']
	mtxPapago.release()
#--end of PapagoSMT
	
if __name__ == '__main__':
	#Read configfile for API keys
	iniPapago = configparser.RawConfigParser()
	iniPapago.read('../conf/naver/papago/api.ini')
	mtxTelegram = threading.Lock()

	#Set Papago API
	reqPapago = urllib.request.Request('https://openapi.naver.com/v1/language/translate')
	reqPapago.add_header('X-Naver-Client-Id',iniPapago['AqoursBotSMT']['X_Naver_Client_Id'])
	reqPapago.add_header('X-Naver-Client-Secret',iniPapago['AqoursBotSMT']['X_Naver_Client_Secret'])
	PAPAGO_JP_TO_KR_QUERY = 'source=' + iniPapago['AqoursBotSMT']['SourceLang'] + '&target=' + iniPapago['AqoursBotSMT']['TargetLang'] + '&text='
	mtxPapago = threading.Lock()

	#Set telegram API
	telBot = telegram.Bot(token=iniTelegram['NamaqoursBot']['token'])

	#Set telegram ID. Bot will be sent new tweet to this ID
	#You can add user id, channel name, group name
	sTelegramID = iniTelegramID['Message']['IDtoReceive']
	#Set Admin ID. Bot will be sent error message to this ID
	sTelegramAdmin = iniTelegramID['Message']['AdminID']

	#Run Thread
	tsTwitterSender = TwitterSender();
	tsTwitterSender.start()
	isInstaSender = InstagramCrawler();
	isInstaSender.start()
	while True:
		pass()
	#--end of while

	print('End of program. Never com here')
#--end of if
