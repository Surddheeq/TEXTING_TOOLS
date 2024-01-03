#Code Successfully written by SADIK MAGAJI SALEH , WEDNESDAY/2/2024, MADE IN KANO,NG.

def MTN():
	import random
	import time
	import os
	os.system("cls\nclear")
	import sys
	print("                  𝙵𝚁𝙴𝙴 𝙼𝚃𝙽 𝙽𝚄𝙼𝙱𝙴𝚁𝚂 𝙱𝚈 𝚂𝙰𝙳𝙸𝙺 𝚁𝙸𝙳𝙴𝚁\n\n                This is an Mtn number generator zone..\n")
	type = input("\nMTN NUMBER STARTING POINT [Example: 0813, 0906, 0709, 0703, ETC ]: ")
	if type in ["0813","0803","0906","0709","0706","0903","0703","0806","0810","0814","0816","0913"]:
		 time.sleep(1.0)
		 print(f"Checking.. {type}\nCongratulations.. {type} can be used")
		 time.sleep(1.5)
	else:
		time.sleep(1.0)
		print(f"Checking.. {type}!\nSorry, You need a 4 digits Numbers to get accurate MTN phone Number!")
		time.sleep(1.5)
		return MTN()
	limits = 5000000
	print("DO YOU WANT TO SEE LIMITS??:\n[01]: Yes\n[02]: No")
	Ans = input("Answer: ")
	if Ans in ["Yes","01","1","YES"]:
		print(f"The maximum limit to crack is '{limits}'")
	else:
		print("oh Great! ")
		False
	try:
		limit = int(input("How many Numbers do you want to crack?: "))
		if limit < 1:
			print(f"Ouuch! cracking numbers should be above  {limit}")
			return MTN()
		elif limit > limits:
			print(f"ooouch! cracking numbers should be less than what you provided which is  '{limit}'")
			return MTN()
	except ValueError:
		time.sleep(3.5)
		g = "="
		print(f"'\nWhat you specified isn't a valid numeric number.. Please use valid Numbers to continue\n RESTARTING ENGINE..\n")
		time.sleep(3.5)
		linex = g *7
		print(f"\n{linex}   M   A  I   N       M   E   N   U    {linex}")
		time.sleep(5.0)
		return MTN()
	else:
		secretA = 1111111
		secretB = 9999999
		try:
			for total in range(limit):
				totally = random.randint(secretA,secretB)
				os.system("cd $HOME\ncd /sdcard")#S1
				dir_path = "MTN"
				if not os.path.exists(dir_path):
					time.sleep(2.0)
					print("Directory doesnt exists!")
					time.sleep(1.5)
					print("Creating folder.. please wait..")
					os.mkdir("MTN")#s2
				folder = os.system("cd /sdcard")#S3
				files = "sdcard/MTN" #S4
				f = open(f"/{files}/MTN_Numbers.txt",'a')
				print(f"{type}{totally}", file = f)
				print(f"{type}{totally}")
				f.close()
		except FileExistsError:
				print("folder already existed")
				import time
				time.sleep(3.0)
				os.system("cd $HOME\ncd /sdcard")#S3
				os.mkdir("MTN")
				files = "/sdcard/MTN/MTN_Numbers.txt" #S4
				print(f"{type}{totally}")
				f = open(f"{files}{type}{totally}",'a')
				f.write(f"{type}{totally}")
				f.close()
		except Exception as e:exit(str(e))
import time
MTN()
time.sleep(2.5)
print(f"Numbers have been generated successfully")
#SOURCE-CODE IS FREE, BUT PLEASE GIVE CREDIT
                                        #  -surddheeq™