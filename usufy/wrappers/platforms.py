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

import urllib2
import os

from utils.usufybrowser import UsufyBrowser
from utils.credentials import Credential

# logging imports
import logging
	
import random

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
		self.score= sco
		# TO-DO:
		#	self.credentials will be an optional parameter that includes a list of Credentials files
		self.creds = []
		
	def __str__(self):
		''' 
			Función para obtener el texto que se representará a la hora de imprimir el objeto.
			
			Return values:
				self.platformName
		'''
		return self.platformName	
		
	def _genURL(self, nick):
		'''	
			Private method that returns an URL for a given nick. 
			
			Return values:
				string containing a URL
		'''
		return self.url.replace(self.NICK_WILDCARD, nick)

	def _getAuthenticated(self, uBrowser):
		''' 
			Getting authenticated. This method will be overwritten.
		'''
		# check if we have creds
		if len(self.creds) > 0:
			# choosing a cred
			c = random.choice(self.creds)
			print url, c.user, c.password
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
		
	def _getResourceFromUserOld(self, url):
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
			#print url
			# check if it needs creds
			if self.needsCredentials():
				authenticated = self._getAuthenticated(uBrowser)
				print authenticated
				if authenticated:
					html = uBrowser.recoverURL(url)		
				else:
					return None
			else: 
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

			Return values:
				True | false
		'''
		for letter in self.forbiddenList:
			if letter in nick:
				return False
		return True		

	def _processProfile(self, oP, html):
		'''	
			Method to process an URL depending on the functioning of the site. By default, it stores the html downloaded on a file.
			This method might be overwritten by each and every class to perform different actions such as indexing the contents with tools like pysolr, for example.

			Return values:
				None
				
			[TO-DO]
				This method will include a call to the process html method.
		'''
		
		logger = logging.getLogger("usufy")
		logger.debug("Writing file: " + oP)
		with open (oP, "w") as oF:
			oF.write(html)
		logger.debug("File saved: " + oP)
		
		#[TO-DO]
		#	The specific platform.py method called: _processHTML will be called from here but in a usufybrowser method.
		
		return True
	
	def getUserPage(self, nick, outputF=None, avoidProcessing=True):
		''' 
			This public method is in charge of recovering the information from the user profile.
			
			List of parameters used by this method:
				nick:		nick to search
				outputF:	will contain a valid path to the outputFolder
				avoidProcessing:will define whether a further process is performed
	
			Return values:
				url	URL del usuario en cuestión una vez que se haya confirmado su validez.
				None	En el caso de que no se haya podido obtener una URL válida.
		'''
		logger = logging.getLogger("usufy")
		# Verifying if the nick is a correct nick
		if self._isValidUser(nick):
			logger.debug("Generating a URL...")
			url = self._genURL(nick)	
			# en función de la respuesta, se hace la comprobación de si el perfil existe o no
			html = self._getResourceFromUserOld(url) 
			if html != None:
				if not avoidProcessing:
					# Storing file if the user has NOT said to avoid the process...	
					logger.debug("Storing the file...")	
					outputPath = os.path.join(outputF, nick)
					if not os.path.exists(outputPath):
						os.makedirs(outputPath)
					self._processProfile(os.path.join(outputPath, nick + "_" + str(self).lower()), html)
				return url
			else:
			#	raise Exception, "UserNotFoundException: the user was not found in " + self.socialNetworkName
				return None
		else:
			# the user is not a valid one
			logger.debug((self.name + ":").ljust(18, ' ') + "The user '" + nick + "' will not be processed in this platform." )
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
	
	def parsingHTML(self, html):
		''' 
			Public method to parse any HTML and process the information found there.
			
			[TO-DO]
		'''
		return True		
		
	def setCredentials(self, creds):
		''' 
			Setting Credentials
		'''
		self.creds = creds
