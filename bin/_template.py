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
__author__ = "F. Brezo and Y. Rubio"
__copyright__ = "Copyright 2014, F. Brezo and Y. Rubio (i3visio)"
__credits__ = ["F. Brezo", "Y. Rubio"]
__license__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "F. Brezo"
__email__ = "contacto@i3visio.com"


from platforms import Platform

class <HERE_GOES_THE_PLATFORM>(Platform):
	""" 
		A <Platform> object for <HERE_GOES_THE_PLATFORM>.
	"""
	def __init__(self):
		""" 
			Constructor... 
		"""
		self.platformName = "<HERE_GOES_THE_PLATFORM>"
		# Add the tags for the platform
		self.tags = ["tag_test1", "tag_test2"]
		self.NICK_WILDCARD = "<HERE_GOES_THE_NICK>"
		# Add the URL below
		self.url = <HERE_GOES_THE_URL>
		# Add the strings to look for when an error appears
		self.notFoundText = ["ERROR test."]
		# Score for the current Platform
		self.score = 0.0
