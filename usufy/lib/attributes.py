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

# logging imports
import logging

class Attributes():
	""" 
		List of attributes for the platforms.
	"""
	def __init__(self):
		""" 
			Creation of the attributtes.
		"""
		self.activism = 0
		self.adult = 0
		self.contact = 0
		self.ecommerce = 0
		self.gambling = 0
		self.hacking = 0
		self.opinions = 0
		# add here new tags

	def __init__(self, activism = 0, adult = 0, contact = 0, ecommerce = 0, gambling = 0, hacking = 0, opinions = 0):
		""" 
			Creation of the attributtes.
		"""
		self.activism = activism
		self.adult = adult
		self.contact = contact
		self.ecommerce = ecommerce
		self.gambling = gambling
		self.hacking = hacking
		self.opinions = opinions

	def __str__(self):
		"""
		"""
		text = 	"Activism:" + str(self.activism) + "; " + "Adult:" + self.adult + "; " + "Contact:" + self.contact + "; " + "Ecommerce:" + self.ecommerce + "; " + "Gambling:" + self.gambling + "; " + "Hacking:" + self.hacking + "; " + "Opinions:" + self.opinions + "; " 
		return text
