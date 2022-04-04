#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from datetime import datetime
from pytube import YouTube


ZomTitle = u"""\u001b[31m

       ______ ______  ___ __ __   _______  ______   ______  __     __     
      /_____//_____/\/__//_//_/\/_______/\/_____/\ /_____/\/__/\ /__/\    
      \:::__\\:::_ \ \::\| \| \ \::: _  \ \:::_ \ \\::::_\/\ \::\\:.\ \   
         /: / \:\ \ \ \:.      \ \::(_)  \/\:(_) ) )\:\/___/\_\::_\:_\/   
        /::/___\:\ \ \ \:.\-/\  \ \::  _  \ \: __ `\ \::___\/__\/__\_\_/\ 
       /_:/____/\:\_\ \ \. \  \  \ \::(_)  \ \ \ `\ \ \:\____/\ \ \ \::\ \.
       \_______\/\_____\/\__\/ \__\/\_______\/\_\/ \_\/\_____\/\_\/  \__\/
\u001b[0m"""


if os.name == 'posix':
    _ = os.system('clear')
else:
    _ = os.system('cls')


print(ZomTitle)
print(f"\u001b[33m[{datetime.now().strftime('%H:%M:%S')} INFO] » Checking status... \u001b[0m\n")
input(f"\u001b[33m[{datetime.now().strftime('%H:%M:%S')} INFO] » Press Enter to continue... \u001b[0m")

url = input("Enter video URL:")
yourVideo = YouTube(url)
if input(f"\u001b[33m[{datetime.now().strftime('%H:%M:%S')} INFO] » Do you want to download {yourVideo.title}? [Y/n] \u001b[0m") == "Y":
    print(f"\u001b[33m[{datetime.now().strftime('%H:%M:%S')} INFO] » Downloading... \u001b[0m\n")
    yourVideo = yourVideo.streams.get_highest_resolution()
    yourVideo.download("downloads")
    print(f"\u001b[33m[{datetime.now().strftime('%H:%M:%S')} INFO] » Download complete! \u001b[0m\n")
else:
    print(f"\u001b[33m[{datetime.now().strftime('%H:%M:%S')} INFO] » Download canceled! \u001b[0m\n")


