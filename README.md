! If you have any question, please contact to "green0apple@naver.com"(Only Korean, Japanese, English)


## NamAqoursBot
This project is for getting translated SNS(Blog, Twitter, etc...) contents from members of group "Aqours" in anime "Lovelive! Sunshine!!" (Voice actress)
BUT you can use this bot for all tweets, sending with all your own telegram bots (Please refer "How to use?" example for details)

## Build status
[Version 0.9] - 190516 KST
1. All of tweets from "conf/twitter/id.ini" are sent to telegram bot(test bot for only developer) with JP->KR translated contents

## Tests
Please refer "How to use?" example

## Installation
* Install Python3
```sh	
$ sudo apt-get install python3
```

* Install required libraries 
 ```sh	
$ sudo pip3 install python-telegram-bot
$ sudo pip3 install python-twitter
```

* Clone NamAqoursBot
```sh
$ git clone https://github.com/green0apple/NamaqoursBot
```

## How to use
You can use any editor to edit ini file, not only nano
* ##### Add Naver papago SMT API secret and key
```sh
$ nano NamaqoursBot/conf/naver/papago/api.ini
```
Please refer below table for information of section, key, value

| Section/key                        | Explanation              |
| ---------------------------------- | ------------------------ |
| AqoursBotSMT/X_Naver_Client_Id     | Papago SMT API ID        |
| AqoursBotSMT/X_Naver_Client_Secret | Papago SMT API secret    |
| AqoursBotSMT/SourceLang            | Original text languege   |
| AqoursBotSMT/TargetLang            | Translated text languege |

* ##### Add Twitter API secret and key
```sh
$ nano NamaqoursBot/conf/twitter/api.ini
```
Please refer below table for information of section, key, value

| Section/key                      | Explanation                     |
| -------------------------------- | ------------------------------- |
| NamaqoursBot/consumer_key        | Twitter API consumer key        |
| NamaqoursBot/consumer_secret     | Twitter API consumer secret     |
| NamaqoursBot/access_token_key    | Twitter API access token key    |
| NamaqoursBot/access_token_secret | Twitter API access token secret |

* ##### Add Twitter ID you want to get timeline
```sh
$ nano NamaqoursBot/conf/twitter/id.ini
```
Please refer below table for information of section, key, value

| Section/key    | Explanation                         |
| -------------- | ----------------------------------- |
| ID/{Number}    | Twitter ID you want to get timeline |
| Nickname/{ID}  | Nickname for Twitter ID (Optional)  |
    
For example, Twitter IDs are "Lovelive, Sunshine" and Nickname "anju, suwawa"
```
[ID]
0=Lovelive
1=Sunshine
    
[Nickname]
Lovelive=anju
Sunshine=suwawa
```
You don't need to add Nickname.  example, Twitter IDs are "Lovelive, Sunshine" and Nickname "anju"
```
[ID]
0=Lovelive
1=Sunshine
  
[Nickname]
Lovelive=anju
```
* #####  Add Telegram Bot API token. New timeline from twitter can be sent to Telegram by using this Bot
```sh
$ nano NamaqoursBot/conf/telegram/api.ini
```
Please refer below table for information of section, key, value

| Section/key        | Explanation            |
| ------------------ | ---------------------- |
| NamaqoursBot/token | Telegram bot API token |

* #####  Add Telegram ID for receiving tweets and error message
```sh
$ nano NamaqoursBot/conf/telegram/message.ini
```
Please refer below table for information of section, key, value

| Section/key         | Explanation                                              |
| ------------------- | -------------------------------------------------------- |
| Message/IDtoReceive | Telegram ID(or chat, group) for receiveing tweet message |
| Message/Admin       | Telegram ID(or chat, group) receiveing error message     |
    
* ##### Run Bot
```sh
$ python3 NamaoqursBot/src/NamaqoursBot.py
```

## License
This program follows MIT license. Please read LICENSE.txt

If you use this program as commercial, you MUST notify to green0apple@naver.com before use it.

If you use this program as non-commercial, please nofity to green0apple@naver.com.
