# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is free software: you can redistribute it and/or modify
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
''' 
squaty.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
For details, run:
	python squaty.py --license
'''
__author__ = "Felix Brezo, Yaiza Rubio "
__copyright__ = "Copyright 2014, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "GPLv3"
__version__ = "v0.1.0"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"

import argparse

import logging

def genNicksWithWords(nicks):
	'''
		Adding new words for the nicks.
		
		:param nicks: 	list of nicks as an string array.
	'''
	# initiating the list of words to be added
	words = []
	words.append('_real_')
	words.append('_official_')
	words.append('_oficial_')
	
	# Defining the working list of nicks
	aux = list(nicks)
	
	for n in nicks:
		for w in words:
			# appending the word to the list
			newNick = n+w
			if newNick not in aux:
				aux.append(newNick)
			# starting with the word
			newNick = w+n
			if newNick not in aux:
				aux.append(newNick)		
	return aux

def genNicksWithL33t(nicks):
	'''
		Adding some of the changes for the leet mode.
		
		:param nicks: 	list of nicks as an string array.
	'''
	# initiating the list of letters that will be changed amongst them
	changes = {}
	changes ['a'] = ['4']
	changes ['b'] = ['8', '|3']
	changes ['c'] = []
	changes ['d'] = []
	changes ['e'] = ['3']
	changes ['f'] = []
	changes ['g'] = ['9']
	changes ['h'] = ['|-|']
	changes ['i'] = ['1']
	changes ['j'] = []
	changes ['k'] = []
	changes ['l'] = ['1']
	changes ['m'] = ['nn', '|v|']
	changes ['n'] = ['|\\|']
	changes ['o'] = ['0']
	changes ['p'] = []
	changes ['q'] = ['9']
	changes ['r'] = []
	changes ['s'] = ['5']
	changes ['t'] = ['7']
	changes ['u'] = []
	changes ['v'] = ['\\/']
	changes ['w'] = ['vv', '\\/\\/']
	changes ['x'] = ['><', '*']
	changes ['y'] = []
	changes ['z'] = ['2']

	# Defining the working list of nicks
	aux = list(nicks)
	
	for n in nicks:
		for letter in changes.keys():
			waysOfRepresentingLetter = changes[letter]
			for change in waysOfRepresentingLetter:
				newNick = n.replace(letter, change)
			if newNick not in aux:
				aux.append(newNick)		
	return aux	

def genNicksWithYears(nicks):
	'''
		Adding new characters for the nicks.
		
		:param nicks: 	list of nicks as an string array.
	'''
	
	# Defining the working list of nicks
	aux = list(nicks)
	
	for n in nicks:
		for i in range (0,100):
			# appending 00 to 99 to the nick
			newNick = n + str(i).rjust(2,'0')
			if newNick not in aux:
				aux.append(newNick)
			# appending 1900 to 1999 to the nick
			newNick = n + "19" + str(i).rjust(2,'0')
			if newNick not in aux:
				aux.append(newNick)
			# appending 2000 to 2099 to the nick
			newNick = n + "20" + str(i).rjust(2,'0')
			if newNick not in aux:
				aux.append(newNick)
	return aux
	
def genNicksWithLocal(nicks, alfa2 = None, alfa3 = None):
	'''
		Adding localized tags for countries to the nicks.
		
		:param nicks: 	list of nicks as an string array.
	'''
	if alfa2 == None:
		alfa2 = ['_ad', '_ae', '_af', '_ag', '_ai', '_al', '_am', '_ao', '_aq', '_ar', '_as', '_at', '_au', '_aw', '_ax', '_az', '_ba', '_bb', '_bd', '_be', '_bf', '_bg', '_bh', '_bi', '_bj', '_bl', '_bm', '_bn', '_bo', '_bq', '_br', '_bs', '_bt', '_bv', '_bw', '_by', '_bz', '_ca', '_cc', '_cd', '_cf', '_cg', '_ch', '_ci', '_ck', '_cl', '_cm', '_cn', '_co', '_cr', '_cu', '_cv', '_cw', '_cx', '_cy', '_cz', '_de', '_dj', '_dk', '_dm', '_do', '_dz', '_ec', '_ee', '_eg', '_eh', '_er', '_es', '_et', '_fi', '_fj', '_fk', '_fm', '_fo', '_fr', '_ga', '_gb', '_gd', '_ge', '_gf', '_gg', '_gh', '_gi', '_gl', '_gm', '_gn', '_gp', '_gq', '_gr', '_gs', '_gt', '_gu', '_gw', '_gy', '_hk', '_hm', '_hn', '_hr', '_ht', '_hu', '_id', '_ie', '_il', '_im', '_in', '_io', '_iq', '_ir', '_is', '_it', '_je', '_jm', '_jo', '_jp', '_ke', '_kg', '_kh', '_ki', '_km', '_kn', '_kp', '_kr', '_kw', '_ky', '_kz', '_la', '_lb', '_lc', '_li', '_lk', '_lr', '_ls', '_lt', '_lu', '_lv', '_ly', '_ma', '_mc', '_md', '_me', '_mf', '_mg', '_mh', '_mk', '_ml', '_mm', '_mn', '_mo', '_mp', '_mq', '_mr', '_ms', '_mt', '_mu', '_mv', '_mw', '_mx', '_my', '_mz', '_na', '_nc', '_ne', '_nf', '_ng', '_ni', '_nl', '_no', '_np', '_nr', '_nu', '_nz', '_om', '_pa', '_pe', '_pf', '_pg', '_ph', '_pk', '_pl', '_pm', '_pn', '_pr', '_ps', '_pt', '_pw', '_py', '_qa', '_re', '_ro', '_rs', '_ru', '_rw', '_sa', '_sb', '_sc', '_sd', '_se', '_sg', '_sh', '_si', '_sj', '_sk', '_sl', '_sm', '_sn', '_so', '_sr', '_ss', '_st', '_sv', '_sx', '_sy', '_sz', '_tc', '_td', '_tf', '_tg', '_th', '_tj', '_tk', '_tla', '_tm', '_tn', '_to', '_tr', '_tt', '_tv', '_tw', '_tz', '_ua', '_ug', '_um', '_us', '_uy', '_uz', '_va', '_vc', '_ve', '_vg', '_vi', '_vn', '_vu', '_wf', '_ws', '_ye', '_yt', '_za', '_zm', '_zw']

	if alfa3 == None:
		alfa3 = ['abw', '_afg', '_ago', '_aia', '_ala', '_alb', '_and', '_are', '_arg', '_arm', '_asm', '_ata', '_atf', '_atg', '_aus', '_aut', '_aze', '_bdi', '_bel', '_ben', '_bes', '_bfa', '_bgd', '_bgr', '_bhr', '_bhs', '_bih', '_blm', '_blr', '_blz', '_bmu', '_bol', '_bra', '_brb', '_brn', '_btn', '_bvt', '_bwa', '_caf', '_can', '_cck', '_che', '_chl', '_chn', '_civ', '_cmr', '_cod', '_cog', '_cok', '_col', '_com', '_cpv', '_cri', '_cub', '_cuw', '_cxr', '_cym', '_cyp', '_cze', '_deu', '_dji', '_dma', '_dnk', '_dom', '_dza', '_ecu', '_egy', '_eri', '_esh', '_esp', '_est', '_eth', '_fin', '_fji', '_flk', '_fra', '_fro', '_fsm', '_gab', '_gbr', '_geo', '_ggy', '_gha', '_gib', '_gin', '_glp', '_gmb', '_gnb', '_gnq', '_grc', '_grd', '_grl', '_gtm', '_guf', '_gum', '_guy', '_hkg', '_hmd', '_hnd', '_hrv', '_hti', '_hun', '_idn', '_imn', '_ind', '_iot', '_irl', '_irn', '_irq', '_isl', '_isr', '_ita', '_jam', '_jey', '_jor', '_jpn', '_kaz', '_ken', '_kgz', '_khm', '_kir', '_kna', '_kor', '_kwt', '_lao', '_lbn', '_lbr', '_lby', '_lca', '_lie', '_lka', '_lso', '_ltu', '_lux', '_lva', '_mac', '_maf', '_mar', '_mco', '_mda', '_mdg', '_mdv', '_mex', '_mhl', '_mkd', '_mli', '_mlt', '_mmr', '_mne', '_mng', '_mnp', '_moz', '_mrt', '_msr', '_mtq', '_mus', '_mwi', '_mys', '_myt', '_nam', '_ncl', '_ner', '_nfk', '_nga', '_nic', '_niu', '_nld', '_nor', '_npl', '_nru', '_nzl', '_omn', '_pak', '_pan', '_pcn', '_per', '_phl', '_plw', '_png', '_pol', '_pri', '_prk', '_prt', '_pry', '_pse', '_pyf', '_qat', '_reu', '_rou', '_rus', '_rwa', '_sau', '_sdn', '_sen', '_sgp', '_sgs', '_shn', '_sjm', '_slb', '_sle', '_slv', '_smr', '_som', '_spm', '_srb', '_ssd', '_stp', '_sur', '_svk', '_svn', '_swe', '_swz', '_sxm', '_syc', '_syr', '_tca', '_tcd', '_tgo', '_tha', '_tjk', '_tkl', '_tkm', '_tls', '_ton', '_tto', '_tun', '_tur', '_tuv', '_twn', '_tza', '_uga', '_ukr', '_umi', '_ury', '_usa', '_uzb', '_vat', '_vct', '_ven', '_vgb', '_vir', '_vnm', '_vut', '_wlf', '_wsm', '_yem', '_zaf', '_zmb', '_zwe']
	# Defining the working list of nicks
	aux = list(nicks)
	
	for n in nicks:
		for tag in alfa2:
			# appending a two-character country tag to the nick
			newNick = n + tag
			if newNick not in aux:
				aux.append(newNick)
		for tag in alfa3:
			# appending a three-character country tag to the nick
			newNick = n + tag
			if newNick not in aux:
				aux.append(newNick)	
	return aux

def genNicksWithBasic(nicks):
	''' 
			Iterating on the list of nicks to find '.' or "_" and replace them according to:
					- if '.' in n: 
							adding n.replace('.', '_')
							adding n.replace('.', '')
							...
					- if '_' in n: 
							adding n.replace('_', '.')
							adding n.replace('_', '')
							...
			:param nicks:	a list with the already generated nicknames.
			:return:	a list with the new nicknames.
	'''
	listSeparators = ['.', '_', '-']

	aux = []
	for n in nicks:
		# Adding the current nick
		aux.append(n)

		# Initializing candidates list
		candidates = []

		# Checking if the nick contains a separator
		for curSep in listSeparators:
			if curSep in n:
				for newSep in listSeparators:
					candidate = n.replace(curSep, newSep)
					if candidate not in aux:
						aux.append(candidate)
			# trying deleting separator
			if curSep in n:
				candidate = n.replace(curSep, '')
				if candidate not in aux:
					aux.append(candidate)
	return aux
		
	
def getNewNicks(nicks, logName = __name__, modes = ['all'], nonValidChars = '\\|<>='):
	'''
		Method that gets all the new nicks
	'''
	# recovering logger
	logger = logging.getLogger(logName)
	# defining the returning list of nicks
	aux = nicks
	for m in modes:
		if (m == 'words') or (m == 'all'):
			aux = genNicksWithWords(aux)
		if (m == 'l33t') or (m == 'all'):
			aux = genNicksWithL33t(aux)
		if (m == 'years') or (m == 'all'):
			aux = genNicksWithYears(aux)
		if (m == 'local') or (m == 'all'):
			aux = genNicksWithLocal(aux)
		if (m == 'basic') or (m == 'all'):
			aux = genNicksWithBasic(aux)
	final = []
	# Verifying whether the generated nicks have valid or not valid characters...
	for nick in aux:
		valid = True
		for charac in nonValidChars:
			if charac in nick:
				valid = False
				# Stopping... One invalid character is enough to discard the nick
				break
		if valid:
			final.append(nick)
	return final
		
def squaty_main(args = None, logName = __name__):
	'''
		Main function for squaty.
	'''
	# list of nicks to be returned
	if args.nicks:
		nicks = args.nicks
	else:
		# Reading the nick files
		try:
			nicks = args.list.read().splitlines()
		except:
			logger.error("ERROR: there has been an error when opening the file that stores the nicks.\tPlease, check the existence of this file.")
	aux = getNewNicks(nicks = nicks, logName = __name__, modes = args.modes, nonValidChars = args.nonvalid)
	return aux
	
	
if __name__ == "__main__":
	print "squaty.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014"
	print "This program comes with ABSOLUTELY NO WARRANTY."
	print "This is free software, and you are welcome to redistribute it under certain conditions."
	print "For details, run:"
	print "\tpython squaty.py --license"
	print ""
	parser = argparse.ArgumentParser(description='squaty.py - Piece of software that generates a series of derivate series .', prog='squaty.py', epilog='Check the README.md file for further details on the usage of this program.', add_help=False)
	parser._optionals.title = "Input options (one required)"

	# Defining the mutually exclusive group for the main options
	general = parser.add_mutually_exclusive_group(required=True)
	# Adding the main options
	general.add_argument('-l', '--list',  metavar='<path_to_nick_list>', action='store', type=argparse.FileType('r'), help='path to the file where the list of nicks to verify is stored (one per line).')
	general.add_argument('-n', '--nicks', metavar='<nick>', nargs='+', action='store', help = 'the list of nicks to process (at least one is required).')
	
	# Configuring the processing options
	groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which squaty will process the identified profiles.')
	groupProcessing.add_argument('--nonvalid', metavar='<not_valid_characters>', required=False, default = '\\|<>=', action='store', help="string containing the characters considered as not valid for nicknames." )
	groupProcessing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, action='store', help='output folder for the generated documents. While if the paths does not exist, squaty.py will try to create; if this argument is not provided, squaty will NOT write any down any data. Check permissions if something goes wrong.')
	groupProcessing.add_argument('-m', '--modes', metavar='<level>',  nargs='+', choices=['basic', 'l33t', 'local', 'years', 'words', 'all'], required=False, default=['all'], action='store', help="select the level of profilesquatting to be looked for (in order of execution): words (for adding sensitive words such as 'real', 'home', 'news', etc.); l33t (l33t m0d3);  years (ending in numbers); local (looking for localized endings: '_es', '_en', '_fr', etc.); basic (changing '-', '.' and ' '); and all.")
	#groupProcessing.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2, 3], required=False, action='store', default=1, help='select the verbosity level: 0 - none; 1 - normal (default); 2 - debug.', type=int)

	# About options
	groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
	groupAbout.add_argument('-h', '--help', action='help', help='shows the version of the program and exists.')
	groupAbout.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3 license and exists.')
	groupAbout.add_argument('--version', action='version', version='%(prog)s 1.3.0b', help='shows the version of the program and exists.')
	
	args = parser.parse_args()	
	
	print (squaty_main(args, __name__))