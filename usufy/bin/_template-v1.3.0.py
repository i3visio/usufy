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

class <HERE_GOES_THE_PLATFORM_NAME>(Platform):
	""" 
		A <Platform> object for <HERE_GOES_THE_PLATFORM_NAME>.
	"""
	def __init__(self):
		""" 
			Constructor... 
		"""
		self.platformName = "<HERE_GOES_THE_PLATFORM_NAME>"
		# Add the tags for the platform
		self.tags = [<HERE_GO_THE_TAGS>]
		self.NICK_WILDCARD = "<NICK_WILDCARD>"
		# Add the URL below
		self.url = <HERE_GOES_THE_URL>
		# Add the strings to look for when an error appears
		self.notFoundText = [<HERE_GO_THE_NOT_FOUND>]

# This file was automatically generated using _classgenerator.py as part of usufy.py.
# Version of the template:	_template-v1.3.0.py
