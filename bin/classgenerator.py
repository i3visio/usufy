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

import argparse


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Automatic generator of classes', prog='_classgenerator.py', epilog="The file must contain the following information:\r\n\tPlatformName;\"http://test1.com/\" + self.NICK_WILDCARD\r\nNote that the part after the ';' should be a python-like valid string.")
	parser._optionals.title = "Input options (one required)"
	# añadimos las funciones posibles
	parser.add_argument('-f', '--file',  metavar='<path_to_file_name>', action='store', type=argparse.FileType('r'), help='path to the file where the list of Classes is stored (one per line).', required=True)
	
	args = parser.parse_args()	
	
	with open("_template.py", "r") as tempF:
		base = tempF.read()
		
	platforms = args.file.read().splitlines()
	
	for linea in platforms:
		aux = base
		info = linea.split(";")
		print "Generando " + info[0].lower() + ".py..."
		with open(info[0].lower() + ".py", "w") as oF:
			aux = aux.replace("<HERE_GOES_THE_PLATFORM>", info[0])
			aux = aux.replace("<HERE_GOES_THE_URL>", info[1])
			oF.write(aux)
		
