<<<<<<< HEAD
! README.md is under modifying. So project explanation is not good, 
Please understand. ! If you have any question, please contact to 
"green0apple@naver.com"(Only Korean, Japanese, English)
## NamAqoursBot
This project is for getting translated SNS(Blog, Twitter, etc...) 
contents from members of group "Aqours" in anime "Lovelive! Sunshine!!" 
(Voice actress) BUT you can use this bot for all tweets, sending with 
all your own telegram bots (Please refer "How to use?" example for 
details)
## Build status
[Version 0.9] - 190516 KST 1. All of tweets from "conf/twitter/id.ini" 
are sent to telegram bot(test bot for only developer) with JP->KR 
translated contents
## Tests
Please refer "How to use?" example
<<<<<<< HEAD
## Installation
#
* Install Python3
    ```sh
	$ sudo apt-get install python3 * Install required libraries
    ```sh
    $ sudo pip3 install python-telegram-bot
	$ sudo pip3 install python-twitter * Clone NamAqoursBot
    ```sh
    $ git clone https://github.com/green0apple/NamaqoursBot
    ```
## How to use
You can use any editor to edit ini file, not only nano * ##### Add Naver 
papago SMT API secret and key
    #
    ```sh
    $ nano NamaqoursBot/conf/naver/papago/api.ini
    ```
    Please refer below table for information of section, key, value
    
    | Section/key | Explanation | ---------------------------------- | 
    | ------------------------ | AqoursBotSMT/X_Naver_Client_Id | Papago 
    | SMT API ID | AqoursBotSMT/X_Naver_Client_Secret | Papago SMT API 
    | secret | AqoursBotSMT/SourceLang | Original text languege | 
    | AqoursBotSMT/TargetLang | Translated text languege |
* ##### Add Twitter API secret and key
    #
    ```sh
    $ nano NamaqoursBot/conf/twitter/api.ini
    ```
    Please refer below table for information of section, key, value
    
    | Section/key | Explanation | -------------------------------- | 
    | ------------------------------- | NamaqoursBot/consumer_key | 
    | Twitter API consumer key | NamaqoursBot/consumer_secret | Twitter 
    | API consumer secret | NamaqoursBot/access_token_key | Twitter API 
    | access token key | NamaqoursBot/access_token_secret | Twitter API 
    | access token secret |
* ##### Add Twitter ID you want to get timeline
    #
    ```sh
    $ nano NamaqoursBot/conf/twitter/id.ini
    ```
    Please refer below table for information of section, key, value
    
    | Section/key | Explanation | -------------- | 
    | ----------------------------------- | ID/{Number} | Twitter ID you 
    | want to get timeline | Nickname/{ID} | Nickname for Twitter ID 
    | (Optional) |
    
    For example, Twitter IDs are "Lovelive, Sunshine" and Nickname 
"anju, suwawa"
    ```
    [ID]
    0=Lovelive
    1=Sunshine
    
    [Nickname]
    Lovelive=anju
    Sunshine=suwawa
    ```
    You don't need to add Nickname.  example, Twitter IDs are "Lovelive, 
Sunshine" and Nickname "anju"
    ```
    [ID]
    0=Lovelive
    1=Sunshine
    
    [Nickname]
    Lovelive=anju
    ``` * ##### Add Telegram Bot API token. New timeline from twitter 
can be sent to Telegram by using this Bot
    #
    ```sh
    $ nano NamaqoursBot/conf/telegram/api.ini
    ```
    Please refer below table for information of section, key, value
    
    | Section/key | Explanation | -------------------------------- | 
    | ------------------------------- | NamaqoursBot/consumer_key | 
    | Twitter API consumer key | NamaqoursBot/consumer_secret | Twitter 
    | API consumer secret | NamaqoursBot/access_token_key | Twitter API 
    | access token key | NamaqoursBot/access_token_secret | Twitter API 
    | access token secret |
* ##### Run Bot
    #
    ```sh
    $ python3 NamaoqursBot/src/NamaqoursBot.py
    ```
## License
This program follows MIT license. Please read LICENSE.txt
#
If you use this program as commercial, you MUST notify to 
green0apple@naver.com before use it.
#
If you use this program as non-commercial, please nofity to 
green0apple@naver.com.
=======

## How to use? (With installation)
0. Prepare(All cases for using)
	
	0-1) Install Python3
		
		0-1-1) apt-get install python3

	0-2) Install required libraries 
		
		0-2-1) pip3 install python-telegram-bot
		
		0-2-2) pip3 install python-twitter
		

	0-3) Add API tokens for Papago(Translate), Telegram(Send message), Twitter

		0-3-1) Loading Papago token by modifying conf/naver/papago/api.ini

		0-3-2) Loading Telegram token by modifying conf/telegram/api.ini

		0-3-3) Loading Twitter token by modifying conf/twitter/api.ini

1. If you use this bot for normal, Just run with command "python3 NamaqoursBot.py"

2. If you use this bot for getting another twitter users' tweets

	2-1) Add or delete Twitter ID by modifying conf/twitter/id.ini

	2-2) Run with commend "python3 NamaqoursBot.py"

3. If you use this bot for another language(default Japanese -> Korean)

	3-1) Modifying conf/naver/papago/api.ini

	3-2) Run with commend "python3 NamaqoursBot.py"


## License
On modifying
>>>>>>> parent of 2bf3924... Update README.md
