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

from platforms import Platform
import random

import logging

class Demo(Platform):
	""" 
		A <Platform> object for Demo using GsmSpain.
	"""
	def __init__(self):
		""" 
			Constructor... 
		"""
		self.platformName = "Demo"
		# Add the tags for the platform
		self.tags = ["social", "technology"]
		self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
		# Add the URL below
		#self.url = "http://www.gsmspain.com/foros/member.php?s=&action=getinfo&username=" + self.NICK_WILDCARD
		self.url = "http://www.gsmspain.com/usuarios/modificar.php"
		# Add the strings to look for when an error appears
		#self.notFoundText = ["Este usuario de GSMspain no tiene perfil en el foro."]
		self.notFoundText = ["<b>ERROR en identificaci"]
		self.forbiddenList = []
		self.score = 20.0

		self._needsCredentials = True
		self.creds = []


	def _getAuthenticated(self, uBrowser):
		""" 
                       Getting authenticated. This method will be overwritten.
		"""
		logger = logging.getLogger("usufy")
		# check if we have creds
		if len(self.creds) > 0:
			# choosing a cred
			c = random.choice(self.creds)
			#print c.urlbase, c.user, c.password
			#br.add_password('http://www.gsmspain.com/usuarios/login.php', 'champ2001', 'hacker')
			urlLogin = "http://www.gsmspain.com/usuarios/login.php"

			r = uBrowser.br.open(urlLogin)

			#for form in br.forms():
			#	print "form is: ", form
			#       raw_input("<PRESS ENTER>")

			#a= int(raw_input("Elige uno de los forms:"))
			# choosing the appropriate form
			uBrowser.br.select_form(nr=1)

			# User credentials
			uBrowser.br.form['usuario'] = c.user
			uBrowser.br.form['password'] = c.password

			uBrowser.br.submit()

			return True
		else:
			logger.debug("No credentials have been added and this platform needs them.")
			return False

