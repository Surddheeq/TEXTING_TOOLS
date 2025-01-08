#Code successfully written by SADIK-RIDER, Hotoro-North, 25/12/2023.
import sys
import time
import os
import random

def runtxt(p):
	for i in p :
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	#ForBOTHTermuxAndWindowsTerminals
	os.system("cls\nclear")

def processor():
		for g in range (100):
			g = g + 1
			time.sleep(0.9)
			clear()
			b = ["Downloading data...","Processing data..","Analysing files..","Please wait.."]
			f = random.choice(b)
			print(f"{f}",g,"%")

processor()
clear(),time.sleep(4.0)
runtxt("FILES DOWNLOADED SUCCESSFULLY!")
time.sleep(4.0)

#             /           E   N  J  O  Y       //                
	                                                              #Surddheeq.                  
