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


def generateProfile(profDict):
	""" 
		Method that calculates de exposure of a profile.
		
		List of parameters that it receives:
		profDict:	Dictionary {"nick1": {Plat1: url1, Plat2: url2, ..., PlatN: urlN}, ..., "nickN" : {Plat1: url1, ..., PlatN: urlN}}

		Return values:
			A dictionary in the form: {"Activism": 3, "Adult": 1.25, ... "Opinions": 4.0}
	"""
	logger = logging.getLogger("usufy")
	res = {}
	res["Activism"]	= 0.0
	res["Adult"] = 0.0
	res["Contact"] = 0.0
	# Add here the rest of the vars as defined in utils.attributes.
	
	# Constant
	POWER = 5
	
	logger.debug("Generating logarithmic progression...")
	for nick in profDict.keys():
		print nick
		for p in profDict[nick].keys():
			res["Activism"] += pow(POWER, p.att.activism)
			res["Adult"] += pow(POWER, p.att.adult)
			res["Contact"] += pow(POWER, p.att.contact)
			# Add here the rest of the vars as defined in utils.attributes.

	logger.debug("Calculating index...")
	import math
	for cat in res.keys():
		# "{0:.2f}".format(a)
		res[cat] = "{0:.2f}".format(math.log(res[cat], POWER))
	return res
		
