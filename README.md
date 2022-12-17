English | [繁體中文](README_TCH.md)
# Python-Voice-Order
An project that can transfer your voice order into word command.

## Project Purpose
My wish to make this a convenient tool help people who can not read or people can not see or you just don't have hand to use this tool. It will be convenient to just tell bot what you want and it can help you to precess these problems.

## How to use
* There are two script to use it: ```detect_voice_main.py``` and ```order_manager.py```
* It is like what its filename called. ```detect voice function``` and ```order bot```.

## Module you need

> You can use this command to install all the module you need ```pip install -r requirements.txt```

* ```pyaudio```
* ```speech_recognition```
* ```openpyxl```
* ```pygame```
* ```gtts```

## Log
### Ver1.0
* Bot can detect your voice into command.
* there are two method to record voice: pyaudio and speech_recognition.
* you can use excel to edit menu and program will automatically enter the item and price into dictionary.
* Bot will response with real voice.
* You can make you order with format: (多少個什麼和多少個什麼)
* Bot will process order into price and it will calculate total and which item didn't exist.
* Chinese number exchange arabtic number.

## Ver1.1
* Add new method to record: temp record with pyaudio.
* Add what time is it module. Now you can ask bot: 幾點了？

## Ver1.2 Add order bot
* Add order bot class
* Classify file to different folder
* Add new voice detect method(tempfile + pyaudio)
* More conversation option

## Ver1.3 Add Chinese num to arabic number
* Add chinese num module for transform chinese num in string into arabic number.

## Ver1.3.1 Add tkinter module
* Add a ```order_program.py``` can use tkinter to order.

## To do list
* More calculate option
  - [ ] equation calculate(方程式計算)
  - [ ] Budget system(預算系統)
  - [ ] law calculate(法律計算機，判刑、罰款)
  - [ ] promotion calculate(優惠計算機)

* More interesting response
  - [ ] promotion hint(詢問時間和問好時做優惠提醒或點餐提醒)

* technical problem
  - [ ] More clear word spread(字詞分割辨認)
  - [ ] voice detect recorrect(語音辨識修正)

* With a GUI.
  - [ ] May on flask(Online)
  - [ ] TKinter(Local)

* Order option
  - [ ] You can use voice to edit menu price or item
