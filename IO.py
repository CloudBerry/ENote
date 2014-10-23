# (C) 2014 Espen Meidell
# espen.meidell@gmail.com
# All rights reserved
import sys
from os.path import expanduser, isfile

path = expanduser("~/.enote.nt")
prefpath = expanduser("~/.enote.pref")

deftext = "!!!---¤¤¤\nWelcome\nWelcome to ENote!"
defpref = ["no", "11"]

def readFile():
	"""
	Returns list of pages from file
	
	@rtype: List of string
	@return: List of pages 
	"""
	try:
		if not isfile(path):
			f = open(path, "w")
			f.write(deftext)
			f.close()
		
		f = open(path)
		raw_data = f.read()
		f.close()
		pages = raw_data.split("!!!---¤¤¤")
		ret_pages = []
		for p in pages:
			if p == "":
				continue
			pg = [p.split("\n")[1]]
			body = ""
			for i in range(2,len(p.split("\n"))):
				body += p.split("\n")[i]
				body += "\n"
			pg.append(body)
			
			ret_pages.append(pg)
		return ret_pages
		
		
	except:
		print("Error reading file:")
		print(sys.exc_info())
		exit(1)

def writeFile(pageNames, bodies):
	"""
	Write pages from application to file
	@type pageNames: List of strings
	@param pageNames: List of page titles
	@type bodies: List of strings
	@param bodies: Content of the pages
	"""
	try:
		f = open(path, "w")
		text = ""
		for i in range(len(pageNames)):
			text += "!!!---¤¤¤\n"
			text += pageNames[i] + "\n"
			text += bodies[i] + "\n"
		f.write(text)
		f.close()
		
		
	except:
		print(sys.exc_info())
		exit(1)


def readPreferences():
	"""
	Get preferences from file
	@rtype: List
	@return List where [0] if bool for dark theme, [1] is int for font size
	"""
	try:
		if not isfile(prefpath):
			f = open(prefpath, "a")
			for p in defpref:
				f.write(p+"\n")
			f.close()
		
		f = open(prefpath, "r")
		raw_preferences = f.readlines()
		for i in range(len(raw_preferences)): raw_preferences[i] = raw_preferences[i].strip("\n")
		if raw_preferences[0] == "no":
			raw_preferences[0] = False
		else: 
			raw_preferences[0] = True
		raw_preferences[1] = int(raw_preferences[1])
		return raw_preferences
	except:
		print(sys.exc_info())
		exit(1)
	
	
def writePreferences(preferences):
	"""
	Write preferences to file
	@type preferences: List of preferences
	@param preferences: List where [0] if bool for dark theme, [1] is int for font size
	"""
	try:
		f = open(prefpath, "w")
		if preferences[0]:
			preferences[0] = "yes"
		else:
			preferences[0] = "no"
		preferences[1] = str(preferences[1])
		print(preferences)
		text = ""
		for p in preferences:
			text += (p+"\n")
		f.write(text)
		f.close()
		
	except:
		print(sys.exc_info())
		exit(1)

	
	
	
	
	
