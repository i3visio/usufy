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

import argparse

""" 
	Fields to read from the CSV file:
		- Name of the file
		- Name of the platform (e. g.: Boonex)
		- Tags (e.g.: "social", "contact")
		- Usufy URL (e.g.: "http://twitter.com/" + self.NICK_WILDCARD)
		- notFoundText (e.g.: "<title>Platform</title>", "Error 404")

	The current version of this program
	# This file was automatically generated using _classgenerator.py v0.1.0 as part of usufy.py.
"""

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Automatic generator of classes', prog='_classgenerator.py', epilog="The file must contain the following information:Name of the file;Name of the platform;Tags;Usufy URL;notFoundTextNote that the part after the ';' should be a python-like valid string.", add_help=False)
	parser._optionals.title = "Input options (one required)"
	# adding the option
	parser.add_argument('-f', '--file',  metavar='<path_to_input_file_name>',  action='store', type=argparse.FileType('r'), help='path to the file where the list of Classes is stored (one per line).', required=True)
	parser.add_argument('-t', '--template',  metavar='<path_to_template_file_name>',  default='./_template-v1.3.0.py', action='store', type=argparse.FileType('r'), help='path to the template file.', required=False)
	
	groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
	groupAbout.add_argument('-h', '--help', action='help', help='shows this help and exists.')
	groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')

	args = parser.parse_args()	

	with open("../utils/config_usufy.py", "r") as tempF:
		config = tempF.read()

	# Reading the _template-vX.X.X.py file
	base = args.template.read()
		
	# Reading the platforms to be processed
	platforms = args.file.read().splitlines()

	for linea in platforms:
		# eliminating the comments
		if linea[0] != "#":
			# loading the blanck template
			aux = base

			# Processing 
			print "Processing:\t" + linea
			info = linea.split(";")
		

			# Creating the wrapper
			print "\tStep 1:\tCreating: " + info[0].lower() + ".py..."
			with open(info[0].lower() + ".py", "w") as oF:
				aux = aux.replace("<HERE_GOES_THE_PLATFORM_NAME>", info[1])
				aux = aux.replace("<HERE_GO_THE_TAGS>", info[2])
				aux = aux.replace("<HERE_GOES_THE_URL>", info[3])
				aux = aux.replace("<HERE_GO_THE_NOT_FOUND>", info[4])
				oF.write(aux)

			# Editing the config_usufy
			print "\tStep 2:\tAdding the recently generated wrapper to a new config_usufy.py..."
			importText = "from wrappers." + info[0] + " import " + info[1]
			config = config.replace("# <ADD_HERE_THE_NEW_IMPORTS>", importText + "\n# <ADD_HERE_THE_NEW_IMPORTS>")
			appendText = "listAll.append(" + info[1] +"())"
			config = config.replace("# <ADD_HERE_THE_NEW_PLATFORMS>", appendText + "\n\t# <ADD_HERE_THE_NEW_PLATFORMS>")

	print "Writing down the recently generated config_usufy.py..."
	with open("config_usufy.py", "w") as oF:
		oF.write(config)
