#CreatedBy:
	#Abubakarsaddeeq081@gmail.com /SADIK-RIDER '' 
import os
import sys
import time

def tool_logo():
	f = "×"
	u= f*40
	c = "_"
	k = c*20
	print(f"{u.upper()}\n\n   FILE    AND     FOLDER     DOCTOR\n       -{k}-\n\nDEVELOPER: SADIK MAGAJI SALEH\nGITHUB: surddheeq\nFACEBOOK: Surddheeq\nMADE: KANO, NIGERIA.\n{u}")

def runtxt(s):
	for i in s + "\n":
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.03)
runtxt("Welcome to this mini tool... it's mini but holy LOL!"),time.sleep(4.0),os.system("clear\ncls")

tool_logo()
def create_folder():
			import os
			create = input("\nInput desired directory alias : ")
			try:
				if create in [""," "]:
					print("You entered Nothing!")
				if create in [(create)]:
					p= os.mkdir((create))
					import time
					time.sleep(3.0)
					a = create.upper()
					print(f"A new folder {a} is created sucessfully")
					return create_folder()
				else:
					return create_folder()
			except FileExistsError:
				print("The Folder already exist here")
				return create_folder()
			except FileNotFoundError:
				print("\nFile not found or file isnt created")
				return create_folder()

def ScreenANDLocate():
	view = input("\nType (ls) to see screen items or press (ENTER KEY) to skip and (cd) to locate into a desired folder, (E.g: cd Download) : ")
	view = os.system((view))
	if view in [""," "]:
		print("Nothing entered!")
	elif view in ["ls"]:
		os.system("ls")
	elif view in [(view)]:
		os.system("cd")
	else:
		print(" isn't need here, Absolutely INVALID🤔")

def FolderFile_Remover():
			def Yes():
				os.system("ls")
			def No():
				False
			h= input("Do You want to view folders [Yes/No]? : ")
			if h in [""," "]:
				print("input something!")
				return FolderFile_Remover()
			elif h in ["y","Y","Yes","YES","yes"]:
				Yes()
			elif h in ["no","No","NO","n","N"]:
				No()
			else:
				runtxt("invalid choice!")
				return FolderFile_Remover()
		
			remove = input("\nFile or Folder name to remove :")
			if remove in ["" ," "]:
				print(f"{remove} isn't a valid command!")
				runtxt("Swifty returning to File remover menu..")
				return FolderFile_Remover()
			elif remove == remove:
				rmv = "rm -rf "
				rmv2 = remove
				os.system(f"{rmv}{rmv2}")
				import time
				time.sleep(2.0)
				print(f"{remove} Successfully removed")
			else:
				print(f"Sorry, Failed to remove File/Folder because it doesn't exist.")

def content():
	print(f"\n[01] - CREATE FOLDERS\n[02] - REMOVE FILES AND FOLDERS\n[03] - LOCATE YOUR FILES\n[04] - VISIT DEVELOPER PROFILE")
	content = input("\nCHOOSE AN OPTION: ")
	if content in [""," "]:
		print("oh sorry, you haven't enter anything!")
	elif content in ["1","01"]:
		create_folder()
	elif content in ["2","02"]:
		FolderFile_Remover()
	elif content in ["3","03"]:
		ScreenANDLocate()
	elif content in ["4","04"]:
		print("Lol, sorry.. under upgrade!")
		os.system("clear")
		time.sleep(2.0)
		runtxt("please wait while the server respond.. ")
		os.system("xdg-open https://www.facebook.com/surddheeq\nxdg-open https://www.instagram.com/surddheeq\nxdg-open https://www.github.com/surddheeq")
	else:
		print(f"sorry, {content} isn't a valid option here.")

content()
#Source_code can be used by 3rd parties, but please give credit to main developer -SurddheeqXDA