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


def resultsToCSV(res):
	""" 
		Method to generate the text to be appended to a CSV file.

		Return values:
			csvText as the string to be written in a CSV file.				
	"""
	logger = logging.getLogger("usufy")
	logger.info( "Generating .csv...")
	csvText = "User\tPlatform\tURL\n"
	logger.debug("Going through all the keys in the dictionary...")
	for r in res.keys():
		for p in res[r].keys():
			csvText += str(r) + "\t" + str(p) + "\t" + res[r][p] + "\n" 
	logger.debug("Loading the dictionary onto a csv-style text...")
	return csvText

def resultsToJson(profiles):
	""" 
		Method to generate the text to be appended to a Json file.
		
		List of parameters that the method receives:
		profiles:	a dictionary with the information of the profiles

		Return values:
			jsonText as the string to be written in Json file.                              
	"""
	logger = logging.getLogger("usufy")
	logger.info( "Generating .json...")
	import json
	aux = {}
	logger.debug("Going through all the keys in the dictionary...")
	for user in profiles.keys():
		aux[user] = {}
		for platform in profiles[user].keys():
			aux[user][str(platform)]  = profiles[user][platform]
	logger.debug("Loading the dictionary onto a json-style text...")
	jsonText =  json.dumps(aux)
	return jsonText


