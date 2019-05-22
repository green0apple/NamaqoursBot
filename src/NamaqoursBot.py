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

#Read configfile for API keys
iniTelegram = configparser.RawConfigParser()
iniTelegram.read('../conf/telegram/api.ini')
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
#						telAPI.send_message(chat_id='440486473', text='New retweet from [' + sNickname + ']' + '\n' + '[Original]' + '\n' + sTweet + '\n' + '[Translated]' + '\n' + sTranslated)
						telAPI.send_message(chat_id='440486473', text='New retweet from [' + sNickname + ']' + '\n' + '[Translated]' + '\n' + sTranslated + '\n' + '[Original]' + '\n' + sTweet)
					#--end of if
					else :
						sTweet = Timeline.full_text
						sData = PAPAGO_JP_TO_KR_QUERY + urllib.parse.quote(sTweet)
						PapagoResp = urllib.request.urlopen(reqPapago, data=sData.encode('utf-8'))
						sTranslated = json.loads(PapagoResp.read().decode('utf-8'))['message']['result']['translatedText']

						print('New tweet from [' + sNickname + '] at ', datetime.datetime.now())
#						telAPI.send_message(chat_id='440486473', text='New tweet from [' + sNickname + ']' + '\n' + '[Original]' + '\n' + sTweet + '\n' + '[Translated]' + '\n' + sTranslated)
						telAPI.send_message(chat_id='440486473', text='New tweet from [' + sNickname + ']' + '\n' + '[Translated]' + '\n' + sTranslated + '\n' + '[Original]' + '\n' + sTweet)
					#--end of else

                                        #Update last tweet time
					dctTwitter[TwitterID]['Timestamp'] = Timeline.created_at

				#--end of if
			#--end of for
		#--end of for
	except Exception as err:
		print('ERROR TIME : ', datetime.datetime.now())
		print('ERROR : ', err)
		telAPI.send_message(chat_id='440486473', text='ERROR : ' + str(err))
	#--end of try
#--end of while

#--End of main


