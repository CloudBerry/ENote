# (C) 2014 Espen Meidell
# espen.meidell@gmail.com
# All rights reserved
import sys
from os.path import expanduser, isfile

path = expanduser("~/.enote.nt")

deftext = "!!!---¤¤¤\nWelcome\nWelcome to ENote!"

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


