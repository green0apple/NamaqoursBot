## Project title
This project is for getting translated SNS(Blog, Twitter, etc...) contents from members of group "Aqours" in anime "Lovelive! Sunshine!!" (Voice actress)
BUT you can use this bot for all tweets, sending with all your own telegram bots (Please refer "How to use?" example for details)

## Motivation
The members of Aqours are Japanese. So, they use Japanese.
But many of fans from overseas can't read jp. Also they want to know what the members say. (include me)
So I started this project for everyone who loves "Lovelive! Sunshine!!"

## Build status
[Version 0.9] - 190516 KST
1. All of tweets from "conf/twitter/id.ini" are sent to telegram bot(test bot for only developer) with JP->KR translated contents

## Installation
On modifying

## Tests
Please refer "How to use?" example

## How to use?
0. Prepare(All cases for using)

        0-1) Add API tokens for Papago(Translate), Telegram(Send message), Twitter

                0-1-1) Loading Papago token by modifying conf/naver/papago/api.ini

                0-1-2) Loading Telegram token by modifying conf/telegram/api.ini

                0-1-3) Loading Twitter token by modifying conf/twitter/api.ini

1. If you use this bot for normal, Just run with command "python3 NamaqoursBot.py"

2. If you use this bot for getting another twitter users' tweets

	2-1) Add or delete Twitter ID by modifying conf/twitter/id.ini

	2-2) Run with commend "python3 NamaqoursBot.py"

3. If you use this bot for another language(default Japanese -> Korean)

	3-1) Modifying conf/naver/papago/lang.ini

	3-2) Run with commend "python3 NamaqoursBot.py"

4. For another using case, or you have any answer about this program, please contact to green0apple@naver.com(Only Korean, Japanese, English)

## Credits
On modifying

#### Anything else that seems useful

## License
On modifying
