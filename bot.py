# 1-1-2024 GIFT ,  Github @surddheeq.
import os
import sys
import time

def clear():
	os.system("cls\nclear")
#Import Modules
def write(q):
	for sadeeq in q + "\n":
		sys.stdout.write(sadeeq)
		sys.stdout.flush()
		time.sleep(0.03)
def Modules():
	try:
		import requests
		import tgpt2
	except ModuleNotFoundError:
		os.system("pip install tgpt2\npip install requests")
	try:
		request = requests.get("https://www.google.com")
	except requests.exceptions.ConnectionError:
		write("NO INTERNET CONNECTION AT THIS CURRENT MOMENT.. TRY AGAIN LATER!")
		time.sleep(1.0)
		clear()
		return Modules()
	else:
		time.sleep(1.0)
		name = input("Whats Your Name:")
		time.sleep(1.0)
		clear()
		time.sleep(1.0)
		f = "-"
		o= f*56
		print(f"WELCOME {name.upper()} TO MY MINI CHAT GPT TOOL !!! \n\n{o}")
		time.sleep(1.0)
		write("I do hope you got lotta question to ask me??")
		print(o)

#Bot Engine modules
from tgpt2 import TGPT as My_Dico
def bot_engine():
	bot = My_Dico()
	while True:
		print(bot.chat(input("\nWhat's Your Question?: ")))

Modules(),bot_engine() #Surddheeq