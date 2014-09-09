# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This file is part of usufy.py.
#
#	Usufy is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################


import os
import random
import re

from utils.usufybrowser import UsufyBrowser
from utils.credentials import Credential
import utils.general as general

# logging imports
import logging
	


class Platform():
	''' 
		<Platform> class.
	'''
	def __init__(self):
		''' 
			Constructor without parameters...
		'''
		pass

	def __init__(self, pName, tags, url, notFT, forChars, sco):
		''' 
			Constructor with parameters. This method permits the developer to instantiate dinamically Platform objects.
		'''
		self.platformName = pName
		# These tags will be the one used to label this platform
		self.tags = tags
		# CONSTANT OF TEXT TO REPLACE
		self.NICK_WILDCARD = "HERE_GOES_THE_NICK"
		# Usually it will contain a phrase like  \"<HERE_GOES_THE_NICK>\" that will be the place where the nick will be included
		self.url = url
		# Text to find when the user was NOT found
		self.notFoundText = notFT
		# List of forbidden characters in this platform
		self.forbiddenList = forChars

		# TO-DO:
		#	self.credentials will be an optional parameter that includes a list of Credentials files
		self.creds = []

		# Delimiters of the current platform:
		self.fieldDelimiters = {}
		# Examples:
		# self.fieldDelimiters["name"] = {"start": "<person>", "end": "</person>"}
		# self.fieldDelimiters["email"] = {"start": "<email>", "end": "</email>"}

		# Ffields found. This attribute will be feeded when running the program.
		self.foundFields = {}
		
	def __str__(self):
		''' 
			Función para obtener el texto que se representará a la hora de imprimir el objeto.
			
			:return:	self.platformName
		'''
		return self.platformName	
		
	def _genURL(self, nick):
		'''	
			Private method that returns an URL for a given nick. 
			:param nick:			

			:return:	string containing a URL
		'''
		return self.url.replace(self.NICK_WILDCARD, nick)

	def _genURLEnum(self, id):
		'''	
			Private method that returns an URL for a given id. 
			:param id:	is an int value.

			:return:	string containing a URL
		'''
		return self.urlEnumeration.replace("<HERE_GOES_THE_USER_ID>", str(id))		
		
	def _getAuthenticated(self, uBrowser):
		''' 
			Getting authenticated. This method will be overwritten.
		'''
		# check if we have creds
		if len(self.creds) > 0:
			# choosing a cred
			c = random.choice(self.creds)
			#print url, c.user, c.password
			# adding the credential
			uBrowser.setNewPassword(url, c.user, c.password)

			# Finishing the authentication
			# [TO-DO]
			return False
		else:
			logger.debug("No credentials have been added and this platform needs them.")
			return False

	def _doesTheUserExist(self, html):
		''' 
			Method that performs the verification of the existence or not of a given profile. This method may be rewrritten.
		'''
		for t in self.notFoundText:
			if t in html:
				return None
		return html
		
	def _getResourceFromUser(self, url):
		''' 
			Este método privado de la clase padre puede ser sobreescrito por cada clase hija si la verificación
			a realizar es más compleja que la verificación estándar.

			Valores retornados:
				html	Si el usuario en cuestión existe en esta red social.
				None	Si el usuario en cuestión no existe en esta red social.
		'''
		logger = logging.getLogger("usufy")
		
		logger.debug("Trying to recover the url: " + url)
		try:
			uBrowser = UsufyBrowser()
			# check if it needs creds
			if self.needsCredentials():
				logger.debug("Trying to get authenticated in " + str(self) + "...")
				authenticated = self._getAuthenticated(uBrowser)
				if authenticated:
					logger.debug("Recovering the targetted url (authenticated)...")
					html = uBrowser.recoverURL(url)		
				else:
					logger.debug("Something happened when trying to get authenticated... ")
					return None
			else:
				logger.debug("Recovering the targetted url...")

				html = uBrowser.recoverURL(url)
		except :
			# no se ha conseguido retornar una URL de perfil, por lo que se devuelve None
			logger.debug("Something happened when trying to recover the resource... No file will be returned.")
			return None
		
		if self._doesTheUserExist(html):
			logger.debug("The key text has NOT been found in the downloaded file. The profile DOES exist and the html is returned.")
			return html
		else:
			# Returning that it does not exist
			logger.debug("The key text has been found in the downloaded file. The profile does NOT exist.")
			return None
		
	def _isValidUser(self, nick):
		'''	
			Method to verify if a given nick is processable by the platform. The system looks for the forbidden characters in self.Forbidden list.
			:param nick:

			:return:	True | False
		'''
		for letter in self.forbiddenList:
			if letter in nick:
				return False
		return True		

	def cleanFoundFields(self):
		''' 
			Method that cleans up the fields recovered.
			
			[TO-DO]
		'''
		pass		
	
	def _getUserIdList(self, platformFolder, action):
		'''
		'''
		listUserId = []
		if not os.path.exists(platformFolder):
			# the platform is being created
			os.makedirs(platformFolder)		
			listUserId = range(self.iNumber, self.fNumber+1)
		else:
			folder = os.path.join(platformFolder, "raw")
			if not os.path.exists(folder):
				listUserId = range(self.iNumber, self.fNumber+1)
			else:				
				if action == "start":
					# restarting the enumeration from the very beginning
					listUserId = range(self.iNumber, self.fNumber+1)
				elif action == "update":
					# Grabbing the list of already processed ids
					filenames = general.getFilesFromAFolder(folder)
					for f in filenames:
						# extracting the "1" from 1_platform_date.html
						id = f.split('_')[0]
						listUserId.append(id)
						# extracting the user id and appending
						#id = int(cabecera.split('-')[1])
						#if id not in listUserId:
						#	listUserId.append(id)
					lastIndex = listUserId[len(listUserId) - 1]
					# appending 1% new possible indexes
					for i in range(lastIndex, lastIndex+(lastIndex/100)):
						listUserId.append(i)						
		return listUserId
	
	def collectProfiles(self, outputFolder= None, avoidProcessing = False, avoidDownload = False, action = "start"):
		'''
			Method that performs the user enumeration tasks
			
			:param outputFolder:	local file where saving the obtained information.
			:param avoidProcessing:boolean var that defines whether the profiles will NOT be processed (stored in this version).
			:param avoidDownload: boolean var that defines whether the profiles will NOT be downloaded (stored in this version).

			:return:	number of profiles processed
		'''
		logger = logging.getLogger("usufy")
		foundUsers = 0
		try:
			if not os.path.exists(outputFolder):
				os.makedirs(outputFolder)
			# Generating the raw output file
			platformFolder = os.path.join(outputFolder, str(self))
			
			listUserId = self._getUserIdList(platformFolder, action)
			
			# action:	start or update
			if action == "start" or action == "update":
				listUserId = self._getUserIdList(platformFolder, action)
				print "The system will try to look for " + str(len(listUserId)) + " user ids..."
				#logger.info("The system will try to look for " + str(len(listUserId)) + " user ids...")
				for id in listUserId:
					urlEnum = self._genURLEnum(id)
					html = self._getResourceFromUser(urlEnum)

					if html != None:
						# Generating current time
						strTime = general.getCurrentStrDatetime()
						if not avoidDownload:
							# Storing file if the user has NOT said to avoid the process...	
							logger.info("Storing the file...")	
							# Generating the raw output folder
							rawFolder = os.path.join(platformFolder, "raw")
							if not os.path.exists(rawFolder):
								os.makedirs(rawFolder)
								
							# Obtaining the rawFilename
							rawFilename = os.path.join( rawFolder, str(id) + "_" + str(self).lower() + "_" + strTime + ".html")
							
							logger.debug("Writing file: " + rawFilename)
							with open (rawFilename, "w") as oF:
								oF.write(html)
							logger.debug("File saved: " + rawFilename)
							
							# Calculating md5 and update raw and processed history
							rawHistoryName = os.path.join( platformFolder, "history_raw.csv" )
							with open (rawHistoryName, "a") as oF:
								oF.write(rawFilename + "\t" + general.fileToMD5(rawFilename) + "\n")
								
						if not avoidProcessing:
						
							# Recovering the processed data
							logger.info("Processing user #" + str(id))
							res = self.processProfile(info=html, url=urlEnum)
							
							# Generating the proc output folder
							procFolder = os.path.join(platformFolder, "proc")
							if not os.path.exists(procFolder):
								os.makedirs(procFolder)
								
							# Obtaining the procFilename
							procFilename = os.path.join( procFolder, str(id) + "_" + str(self).lower() + "_" + strTime + ".json")
							
							logger.debug("Writing file: " + procFilename)
							with open (procFilename, "w") as oF:
								oF.write(res)
							logger.debug("File saved: " + procFilename)
							
							# Calculating md5 and update the processed history
							procHistoryName = os.path.join( platformFolder, "history_proc.csv" )
							with open (procHistoryName, "a") as oF:
								oF.write(procFilename + "\t" + general.fileToMD5(procFilename) + "\n")
						foundUsers+=1
					else:
						#	raise Exception, "UserNotFoundException: the user was not found in " + self.socialNetworkName
						#	return None
						logger.debug("User not found...")	
						pass
			# action:	legacy
			else:
				# mode to recover html already downloaded
				legacyFolder = os.path.join(platformFolder, "legacy")
				# Grabbing the list of already processed ids
				filenames = general.getFilesFromAFolder(legacyFolder)
				for f in filenames:
					id =  f.split('.')[0]
					# opening file
					html = ""
					legacyFilename = os.path.join(legacyFolder, f)
					with open(legacyFilename, 'r') as iF:
						html = iF.read()
					# Generating current time
					strTime = general.getCurrentStrDatetime()
					if not avoidDownload:
						# Storing file if the user has NOT said to avoid the process...	
						logger.debug("Storing user #" + str(id))
						
						# Generating the raw output folder if it does NOT exist
						rawFolder = os.path.join(platformFolder, "raw")
						if not os.path.exists(rawFolder):
							os.makedirs(rawFolder)
						
						# Obtaining the rawFilename
						rawFilename = os.path.join( rawFolder, id + "_" + str(self).lower() + "_" + strTime + ".html")
						
						# Writing the raw file
						logger.debug("Writing file: " + rawFilename)
						with open (rawFilename, "w") as oF:
							oF.write(html)
						logger.debug("File saved: " + rawFilename)
						
						# Calculating md5 and update raw and processed history
						rawHistoryName = os.path.join( platformFolder, "history_raw.csv" )
						
						# Calculating md5 and update the raw history						
						with open (rawHistoryName, "a") as oF:
							oF.write(rawFilename + "\t" + general.fileToMD5(rawFilename) + "\n")
						
					if not avoidProcessing:
						# Recovering the processed data
						logger.debug("Processing user #" + str(id))
						urlEnum = self._genURLEnum(id)
						res = self.processProfile(info=html, url=urlEnum)
	
						# Generating the proc output folder
						procFolder = os.path.join(platformFolder, "proc")
						if not os.path.exists(procFolder):
							os.makedirs(procFolder)
							
						# Obtaining the procFilename
						procFilename = os.path.join( procFolder, str(id) + "_" + str(self).lower() + "_" + strTime + ".json")
						
						# Writing the proc file
						logger.debug("Writing file: " + procFilename)
						with open (procFilename, "w") as oF:
							oF.write(res)
						logger.debug("File saved: " + procFilename)
						
						# Calculating md5 and update the processed history
						procHistoryName = os.path.join( platformFolder, "history_proc.csv" )
						with open (procHistoryName, "a") as oF:
							oF.write(procFilename + "\t" + general.fileToMD5(procFilename) + "\n")
					foundUsers+=1
				
			return foundUsers
		except:
			pass
		pass
	
	
	def getUserPage(self, nick, outputF="./", avoidProcessing=False, avoidDownload = False):
		''' 
			This public method is in charge of recovering the information from the user profile.
			
			List of parameters used by this method:
			:param nick:		nick to search
			:param outputF:		will contain a valid path to the outputFolder
			:param avoidProcessing:boolean var that defines whether the profiles will NOT be processed .
			:param avoidDownload: boolean var that defines whether the profiles will NOT be downloaded.
			:return:
				url	URL del usuario en cuestión una vez que se haya confirmado su validez.
				None	En el caso de que no se haya podido obtener una URL válida.
		'''
		logger = logging.getLogger("usufy")
		# Verifying if the nick is a correct nick
		if self._isValidUser(nick):
			logger.debug("Generating a URL...")
			url = self._genURL(nick)	
			# en función de la respuesta, se hace la comprobación de si el perfil existe o no
			html = self._getResourceFromUser(url) 
			if html != None:
				# Generating current time
				strTime = general.getCurrentStrDatetime()

				outputPath = os.path.join(outputF, nick)
				if not os.path.exists(outputPath):
					os.makedirs(outputPath)
				if not avoidDownload:
					# Storing file if the user has NOT said to avoid the process...	
					logger.info("Storing the file...")	

					# Generating the raw folder
					rawFolder = os.path.join(outputPath, "raw")
					if not os.path.exists(rawFolder):
						os.makedirs(rawFolder)
					
					# Obtaining the rawFilename
					rawFilename = os.path.join( rawFolder, nick + "_" + str(self).lower() + "_" + strTime + ".html")
					
					# Writing the raw file
					logger.debug("Writing file: " + rawFilename)
					with open (rawFilename, "w") as oF:
						oF.write(html)
					logger.debug("File saved: " + rawFilename)
					
					# Calculating md5 and update raw history
					rawHistoryName = os.path.join( outputPath, "history_raw.csv" )
					with open (rawHistoryName, "a") as oF:
						oF.write(rawFilename + "\t" + general.fileToMD5(rawFilename) + "\n")
				if not avoidProcessing:
					# Generating the proc output folder
					procFolder = os.path.join(outputPath, "proc")
					if not os.path.exists(procFolder):
						os.makedirs(procFolder)
					
					# Obtaining the procFilename
					procFilename = os.path.join( procFolder, nick + "_" + str(self).lower() + "_" + strTime + ".json")
					
					# Recovering the processed data
					res = self.processProfile(info=html, nick=nick, url=url)
					
					# Writing the proc file
					logger.debug("Writing file: " + procFilename)
					with open (procFilename, "w") as oF:
						oF.write(res)
					logger.debug("File saved: " + procFilename)
					
					# Calculating md5 and update raw history
					procHistoryName = os.path.join( outputPath, "history_proc.csv" )
					with open (procHistoryName, "a") as oF:
						oF.write(procFilename + "\t" + general.fileToMD5(procFilename) + "\n")
				return url
			else:
			#	raise Exception, "UserNotFoundException: the user was not found in " + self.socialNetworkName
				logger.debug("The user was NOT found.")
				return None
		else:
			# the user is not a valid one
			logger.debug((str(self) + ":").ljust(18, ' ') + "The user '" + nick + "' will not be processed in this platform." )
			return None

	def needsCredentials(self):
		''' 
			Returns if it needsCredentials.
			IT captures the exception if the option does not exist. This way we do not have to recode all the platforms
		'''
		try:
			return self._needsCredentials		
		except:
			return False	

	
	def processProfile(self, info=None, nick=None, url=None):
		'''	
			Method to process an URL depending on the functioning of the site. By default, it stores the html downloaded on a file.
			This method might be overwritten by each and every class to perform different actions such as indexing the contents with tools like pysolr, for example.

			:return: 	json text to be stored on a processed file.
		'''
		def escapingSpecialCharacters(aux):
			'''
			'''
			return aux
			escapingValues = ['(', ')', '[', ']', '-', '\\',]
			
			for esc in escapingValues:
				aux = aux.replace(esc, "\\" + esc)
			return aux
		
		def cleanSpecialChars(auxList):
			'''
			'''
			final = []
			cleaningChars = ["\n", "\t", "\r"]
			for elem in auxList:				
				for c in cleaningChars:
					elem = elem.replace(c, '')
				# Deleting html tags from in between and putting an space instead
				elem = re.sub(r'<.+?>', ' ', elem)
				final.append(elem)
			return final


		logger = logging.getLogger("usufy")
		try:
			# May be revisited in the future so as to add any additional check of whether the profile is correct.
			self.foundFields["platform"] = self.platformName
			self.foundFields["nick"] = nick
			self.foundFields["url"] = url

			#print "Fields to check:\t" + str(self.fieldDelimiters.keys())
			# Going through all the possible fields for the platform
			for field in self.fieldDelimiters.keys():
				#print "-------------------"
				#print field
				delimiters = self.fieldDelimiters[field]
				start = escapingSpecialCharacters(delimiters["start"])
				end = escapingSpecialCharacters(delimiters["end"])
				# Example: 
				#	a = "blablablabalbal<person>James</person> asdadsasdasd <person>John</person>asdasd"
				# 	values = re.findall("<person>(.*?)</person>", a)
				#	(result): ['James', 'John']
				#print "Regexp:\t" + start + "(.*?)" + end
				# re.DOTALL matches with the . any field including \n
				values = re.findall(start + "(.*?)" + end, info, re.DOTALL)
				#print "Values:\t" + str(values)
				# If something has been found, we store the fields
				if len(values) > 0:
					self.foundFields[field] = cleanSpecialChars(values)
			
			# Method that parametrised each and every field depending on its characteristics.
			#	This method WILL BE overwritten in each child class. By default, it does NOTHING
			self.cleanFoundFields()
			
			print general.dictToJson(self.foundFields)
			return general.dictToJson(self.foundFields)
		except:
			logger.debug("Something happened when processing " + str(self) + "... Are self.foundFields or self.fieldDelimiters defined?")
			# Adding the basic values
			aux = {}
			aux["platform"] = self.platformName
			aux["nick"] = nick
			aux["url"] = url
			return general.dictToJson(aux)
			
	def setCredentials(self, creds):
		''' 
			Setting Credentials
		'''
		self.creds = creds
