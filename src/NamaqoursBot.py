<<<<<<< HEAD
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

class TwitterSender
	def __init__(self) :
		iniTwitter = configparser.RawConfigParser()
		iniTwitter.read('../conf/twitter/api.ini')
		iniTwitterID = configparser.RawConfigParser()
		iniTwitterID.read('../conf/twitter/id.ini')
		#Set twitter API
		twAPI = twitter.Api(iniTwitter['NamaqoursBot']['consumer_key'],
							iniTwitter['NamaqoursBot']['consumer_secret'],
							iniTwitter['NamaqoursBot']['access_token_key'],
							iniTwitter['NamaqoursBot']['access_token_secret'],
							tweet_mode='extended')
		#Get TwitterID, Nickname
		jsOldTweets = []
		for sNumber, sID in iniTwitterID.items('ID') :
			if iniTwitterID.has_option('Nickname', sID) :
				jsOldTweets.appand = {"id": sID, "Nickname": iniTwitterID['Nickname'][sID], "Timeline": None, "Timestamp": None}
			else :
				jsOldTweets.appand = {"id": sID, "Nickname": sID, "Timeline": None, "Timestamp": None}
		#--end of for

		#Get users timeline (default init)
		#Count of timeline return from each GetUserTimeline is 5
		for sID in dctTwitter :
			print(sID)
			dtTwitter[sID]['Timestamp'] = twAPI.GetUserTimeline(screen_name=sID,count=5)[0].created_at;
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
				for TwitterID in dctTwitter :
					#Wait 1s for twitter api policy
					time.sleep(1)

					#Get timeline
					arTimeline = twAPI.GetUserTimeline(screen_name=TwitterID,count=5)

					#Compare last tweet time with gotten timelines(5)
					arTimeline.reverse()
					for Timeline in arTimeline :
						#If last tweet time is older then new tweet, print new tweet
						if TwitterTimeToDatetime(dctTwitter[TwitterID]['Timestamp']) < TwitterTimeToDatetime(Timeline.created_at) :
							sNickname = dctTwitter[TwitterID]['Nickname']
							#If new tweet is retweet
							if Timeline.retweeted_status != None :
								sTweet = Timeline.retweeted_status.full_text
								sData = PAPAGO_JP_TO_KR_QUERY + urllib.parse.quote(sTweet)
								PapagoResp = urllib.request.urlopen(reqPapago, data=sData.encode('utf-8'))
								sTranslated = json.loads(PapagoResp.read().decode('utf-8'))['message']['result']['translatedText']
								print('New retweet from [' + sNickname + '] at ', datetime.datetime.now())
								telAPI.send_message(chat_id=sTelegramID, text='New retweet from [' + sNickname + ']' + '\n' + '[Translated]' + '\n' + sTranslated + '\n' + '[Original]' + '\n' + sTweet)
							#--end of if
							else :
								sTweet = Timeline.full_text
								sData = PAPAGO_JP_TO_KR_QUERY + urllib.parse.quote(sTweet)
								PapagoResp = urllib.request.urlopen(reqPapago, data=sData.encode('utf-8'))
								sTranslated = json.loads(PapagoResp.read().decode('utf-8'))['message']['result']['translatedText']
								print('New tweet from [' + sNickname + '] at ', datetime.datetime.now())
								telAPI.send_message(chat_id=sTelegramID, text='New tweet from [' + sNickname + ']' + '\n' + '[Translated]' + '\n' + sTranslated + '\n' + '[Original]' + '\n' + sTweet)
							#--end of else

							#Update last tweet time
							dctTwitter[TwitterID]['Timestamp'] = Timeline.created_at
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
					telAPI.send_message(chat_id=sTelegramAdmin, text='ERROR : ' + str(err))
			#--end of try
		#--end of while
	#--end of execute
#--eid of class TwitterSender



class InstaSender


#Read configfile for API keys
iniTelegram = configparser.RawConfigParser()
iniTelegram.read('../conf/telegram/api.ini')
iniTelegramID = configparser.RawConfigParser()
iniTelegramID.read('../conf/telegram/message.ini')
iniTwitter = configparser.RawConfigParser()
iniTwitter.read('../conf/twitter/api.ini')
iniTwitterID = configparser.RawConfigParser()
iniTwitterID.read('../conf/twitter/id.ini')
iniPapago = configparser.RawConfigParser()
iniPapago.read('../conf/naver/papago/api.ini')

#Set Papago API
reqPapago = urllib.request.Request('https://openapi.naver.com/v1/language/translate')
reqPapago.add_header('X-Naver-Client-Id',iniPapago['AqoursBotSMT']['X_Naver_Client_Id'])
reqPapago.add_header('X-Naver-Client-Secret',iniPapago['AqoursBotSMT']['X_Naver_Client_Secret'])
PAPAGO_JP_TO_KR_QUERY = 'source=' + iniPapago['AqoursBotSMT']['SourceLang'] + '&target=' + iniPapago['AqoursBotSMT']['TargetLang'] + '&text='

#Set telegram API
telAPI = telegram.Bot(token=iniTelegram['NamaqoursBot']['token'])

#Set telegram ID. Bot will be sent new tweet to this ID
#You can add user id, channel name, group name
sTelegramID = iniTelegramID['Message']['IDtoReceive']
#Set Admin ID. Bot will be sent error message to this ID
sTelegramAdmin = iniTelegramID['Message']['AdminID']

#Set twitter API
twAPI = twitter.Api(iniTwitter['NamaqoursBot']['consumer_key'],
		    iniTwitter['NamaqoursBot']['consumer_secret'],
		    iniTwitter['NamaqoursBot']['access_token_key'],
		    iniTwitter['NamaqoursBot']['access_token_secret'],
		    tweet_mode='extended')

#Get TwitterID, Nickname
dctTwitter = {}
for sNumber, sID in iniTwitterID.items('ID') :
	if iniTwitterID.has_option('Nickname', sID) :
		dctTwitter[sID] = {'Nickname': iniTwitterID['Nickname'][sID], 'Timeline': [], 'Timestamp': ''}
	else :
		dctTwitter[sID] = {'Nickname': sID, 'Timeline': [], 'Timestamp': ''}
#--end of for

#Twitter created_at time to python datetime
def TwitterTimeToDatetime(sCreatedAt) :
	return time.strptime(sCreatedAt, '%a %b %d %H:%M:%S +0000 %Y')
#--end of TwitterTimeToDatetime

	#Get users timeline (default init)
	#Count of timeline return from each GetUserTimeline is 5
	for sID in dctTwitter :
		print(sID)
		dctTwitter[sID]['Timestamp'] = twAPI.GetUserTimeline(screen_name=sID,count=5)[0].created_at;
		#Wait 1s for Twitter API policy
		time.sleep(1)
	#--end of for

	#main loop
	while True :

		try :

			#Continue with changing ID
			for TwitterID in dctTwitter :
				#Wait 1s for twitter api policy
				time.sleep(1)

				#Get timeline
				arTimeline = twAPI.GetUserTimeline(screen_name=TwitterID,count=5)

				#Compare last tweet time with gotten timelines(5)
				arTimeline.reverse()
				for Timeline in arTimeline :
					#If last tweet time is older then new tweet, print new tweet
					if TwitterTimeToDatetime(dctTwitter[TwitterID]['Timestamp']) < TwitterTimeToDatetime(Timeline.created_at) :
						sNickname = dctTwitter[TwitterID]['Nickname']
						#If new tweet is retweet
						if Timeline.retweeted_status != None :
							sTweet = Timeline.retweeted_status.full_text
							sData = PAPAGO_JP_TO_KR_QUERY + urllib.parse.quote(sTweet)
							PapagoResp = urllib.request.urlopen(reqPapago, data=sData.encode('utf-8'))
							sTranslated = json.loads(PapagoResp.read().decode('utf-8'))['message']['result']['translatedText']
							print('New retweet from [' + sNickname + '] at ', datetime.datetime.now())
							telAPI.send_message(chat_id=sTelegramID, text='New retweet from [' + sNickname + ']' + '\n' + '[Translated]' + '\n' + sTranslated + '\n' + '[Original]' + '\n' + sTweet)
						#--end of if
						else :
							sTweet = Timeline.full_text
							sData = PAPAGO_JP_TO_KR_QUERY + urllib.parse.quote(sTweet)
							PapagoResp = urllib.request.urlopen(reqPapago, data=sData.encode('utf-8'))
							sTranslated = json.loads(PapagoResp.read().decode('utf-8'))['message']['result']['translatedText']

							print('New tweet from [' + sNickname + '] at ', datetime.datetime.now())
							telAPI.send_message(chat_id=sTelegramID, text='New tweet from [' + sNickname + ']' + '\n' + '[Translated]' + '\n' + sTranslated + '\n' + '[Original]' + '\n' + sTweet)
						#--end of else

                	                        #Update last tweet time
						dctTwitter[TwitterID]['Timestamp'] = Timeline.created_at
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
				telAPI.send_message(chat_id=sTelegramAdmin, text='ERROR : ' + str(err))
		#--end of try
	#--end of while
#--End of execute


=======
#!/usr/bin/python3 -u

##-*- coding:utf-8 -*-
import configparser
import json
import requests
import twitter
import time
import telegram.bot
import datetime
import urllib.request
import threading
from urllib.parse import urlparse
import sys
sys.path.append('..')
from insta import Instagram

class TwitterSender(threading.Thread):
	def __init__(self) :
		self.__MAX_TIMELINES_COUNT = 10
	
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
				self.__jsOldTweets.append({"id": sID, "nickname": self.__iniTwitterID['Nickname'][sID], "timeline": None, "timestamp": None})
			else :
				self.__jsOldTweets.append({"id": sID, "nickname": sID, "timeline": None, "timestamp": None})
		#--end of for

		#Get users timeline (default init)
		#Count of timeline return from each GetUserTimeline is 5
		for jsOldTweet in self.__jsOldTweets :
			print("Twitter ID Init : " + jsOldTweet['id']);
			jsOldTweet['timestamp'] = self.__twAPI.GetUserTimeline(screen_name=jsOldTweet['id'],count=self.__MAX_TIMELINES_COUNT)[0].created_at;
			#Wait 1s for Twitter API policy
			time.sleep(1)
		#--end of for
		
		#Init thread
		threading.Thread.__init__(self)
		
	#--end if __init__
	#Twitter created_at time to python datetime
	@staticmethod
	def __TwitterTimeToDatetime(sCreatedAt) :
		return time.strptime(sCreatedAt, '%a %b %d %H:%M:%S +0000 %Y')
	#--end of TwitterTimeToDatetime

	def run(self) :
		print('TwitterSender : start run')
		while True :
			try :
				#Continue with changing ID
				for jsOldTweet in self.__jsOldTweets :
					#Wait 1s for twitter api policy
					time.sleep(1)
					sID = jsOldTweet['id']
					#Get timeline
					arTimeline = self.__twAPI.GetUserTimeline(screen_name=sID,count=self.__MAX_TIMELINES_COUNT)
					#Compare last tweet time with gotten timelines(__MAX_TIMELINES_COUNT)
					arTimeline.reverse()
					for Timeline in arTimeline :
						#If last tweet time is older then new tweet, print new tweet
						if self.__TwitterTimeToDatetime(jsOldTweet['timestamp']) < self.__TwitterTimeToDatetime(Timeline.created_at) :
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
				print('TWITTER THREAD ERROR TIME : ', datetime.datetime.now())
				print('TWITTER THREADERROR : ', err)
				#bug : if error is Request Timeout, can't use API(network)
				if err != 'Timed out' :
					TelegramSendMessage(sTelegramAdmin, 'ERROR : ' + str(err))
			#--end of try
		#--end of while
	#--end of run
#--end of class TwitterSender

# Instagram not supported
# Maybe Instagram blocks robot. Random reset packet received from Instagram
"""
class InstaSender(threading.Thread):
	def __init__(self) :
		#Read configfile for Instagram ID
		self.__iniInstagram = configparser.RawConfigParser()
		self.__iniInstagram.read('../conf/instagram/id.ini')
		
		#Init Instagram crawler
		self.__instaCrawler = Instagram()

		#Get Insta ID, Nickname
		self.__jsOldTimelines = []
		for sNumber, sID in self.__iniInstagram.items('ID') :
			if self.__iniInstagram.has_option('Nickname', sID) :
				self.__jsOldTimelines.append( {"id": sID, "nickname": self.__iniInstagram['Nickname'][sID], "timestamp": 0} )
			else :
				self.__jsOldTimelines.append( {"id": sID, "nickname": sID, "timestamp": 0} )
		#--end of for
		
		#Get users timeline (default init)
		for jsOldTimeline in self.__jsOldTimelines :
			print("Instagram ID Init : " + jsOldTimeline['id']);
			mtxURLRquest.acquire()
			jsEdges = self.__instaCrawler.GetProfilePage(jsOldTimeline['id'])[0]['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
			mtxURLRquest.release()
			jsOldTimeline['timestamp'] = jsEdges[0]['node']['taken_at_timestamp']
			#Wait 1s for decreasing crawling speed
			time.sleep(1)
		#--end of for
		
		#Init thread
		threading.Thread.__init__(self)
		
	#--end of __init__
	
	def run(self) :
		print('InstaSender : start run')
		while True :
			try :
				#Get old timeline to compare with new timeline
				for jsOldTimeline in self.__jsOldTimelines :
					#Wait 1s for decreasing crawling speed
					time.sleep(2)

					#Get timeline
					mtxURLRquest.acquire()
					jsProfile = self.__instaCrawler.GetProfilePage(jsOldTimeline['id'])
					mtxURLRquest.release()
					jsEdges = jsProfile[0]['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
					
					#Get new timeline to compare with old timeline
					for jsEdge in jsEdges :
						#If last post time is older then new one, print
						if jsOldTimeline['timestamp'] < jsEdge['node']['taken_at_timestamp'] :
							#Wait 1s for decreasing crawling speed
							time.sleep(1)

							mtxURLRquest.acquire()
							jsTimeline = self.__instaCrawler.GetTimeline(jsEdge)
							mtxURLRquest.release()
							sTimeline = jsTimeline['contents']
							sLink = jsTimeline['link']
							sNickname = jsOldTimeline['nickname']
							sData = urllib.parse.quote(sTimeline)
							sTranslated = PapagoSMT(sData)
							print('New timeline from [' + sNickname + '] at ', datetime.datetime.now())
							TelegramSendMessage(sTelegramID, 'New timeline from [' + sNickname + ']' + '\n' + '[Translated]' + '\n' + sTranslated + '\n' + '[Original]' + '\n' + sTimeline + '\n' + sLink )

							#Update last timeline
							jsOldTimeline['timestamp'] = jsEdge['node']['taken_at_timestamp']

						#--end of if
					#--end of for
				#--end of for
				#For thread safe
				time.sleep(0.05)
				print('INSTAGRAM THREAD RUNNING')
			except Exception as err:
				if mtxURLRquest.locked == True : 
					mtxURLRquest.release()
				#--end of if
				print('INSTAGRAM THREAD ERROR TIME : ', datetime.datetime.now())
				print('INSTAGRAM THREAD ERROR : ', err)

				#bug : if error is Request Timeout, can't use API(network)
				if err != 'Timed out' :
					TelegramSendMessage(sTelegramAdmin, 'ERROR : ' + str(err))
				continue
			#--end of try
		#--end of while
	#--end of run
#--end of class InstaSender
"""

def TelegramSendMessage(sID, sText):
	telBot.send_message(chat_id=sID, text=sText)
#--end of TelegramSendMessage

def PapagoSMT(sText):
	sText = PAPAGO_JP_TO_KR_QUERY + sText
	sTranslated = json.loads(urllib.request.urlopen(reqPapago, data=sText.encode('utf-8')).read().decode('utf-8'))['message']['result']['translatedText']
	return sTranslated
#--end of PapagoSMT
	
if __name__ == '__main__':

	
	#Read configfile for API keys
	iniPapago = configparser.RawConfigParser()
	iniPapago.read('../conf/naver/papago/api.ini')

	#Set Papago API
	reqPapago = urllib.request.Request('https://openapi.naver.com/v1/language/translate')
	reqPapago.add_header('X-Naver-Client-Id',iniPapago['AqoursBotSMT']['X_Naver_Client_Id'])
	reqPapago.add_header('X-Naver-Client-Secret',iniPapago['AqoursBotSMT']['X_Naver_Client_Secret'])
	reqPapago.add_header('User-agent', 'Mozilla/5.0')
	PAPAGO_JP_TO_KR_QUERY = 'source=' + iniPapago['AqoursBotSMT']['SourceLang'] + '&target=' + iniPapago['AqoursBotSMT']['TargetLang'] + '&text='

	#Set telegram API
	iniTelegram = configparser.RawConfigParser()
	iniTelegram.read('../conf/telegram/api.ini')
	telBot = telegram.Bot(token=iniTelegram['NamaqoursBot']['token'])

	#Set telegram ID. Bot will be sent new tweet to this ID
	#You can add user id, channel name, group name
	iniTelegramID = configparser.RawConfigParser()
	iniTelegramID.read('../conf/telegram/message.ini')
	sTelegramID = iniTelegramID['Message']['IDtoReceive']
	#Set Admin ID. Bot will be sent error message to this ID
	sTelegramAdmin = iniTelegramID['Message']['AdminID']

	#Run Thread
	tsTwitterSender = TwitterSender()
	arThreads = [tsTwitterSender]
	for t in arThreads:
		t.start()
	#--end of for
	
	while True:
		for t in arThreads:
			t.join()
		#--end of for
	#--end of while

	print('End of program. Never come here')
#--end of if
>>>>>>> v1.0
