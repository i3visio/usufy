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
usufy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
For details, run:
	python user-collector.py --license
'''
__author__ = "Felix Brezo, Yaiza Rubio "
__copyright__ = "Copyright 2014, i3visio"
__credits__ = ["Felix Brezo", "Yaiza Rubio"]
__license__ = "GPLv3"
__version__ = "v1.3.0b"
__maintainer__ = "Felix Brezo, Yaiza Rubio"
__email__ = "contacto@i3visio.com"


import urllib2
import os
import time
import argparse

# global issues
from multiprocessing import Process, Queue, Pool

# configuration and utils
import utils.config_usufy as config
import utils.analyser as analyser
#import utils.attributes as attributes
import utils.benchmark as benchmark
import utils.export as export_mod
#import utils.profilesquatting as profilesquatting
import utils.squaty as profilesquatting
import utils.usufyparser as usufyparser
import g_usufy as usufygui 
import utils.usufybrowser as usufybrowser
import utils.general as general

# logging imports
import utils.logger
import logging
	
def collectProfileWrapper(p, outputFolder, action = "start", avoidProcessing = False, avoidDownload = False):
	''' 
		Method that wraps the call to the getUserPage.

		List of parameters that the method receives:
		:param p:		platform where the information is stored.
		:param outputFolder:	local file where saving the obtained information.
		:param action:	string containing the action.
		:param avoidProcessing:boolean var that defines whether the profiles will NOT be processed (stored in this version).
		:param avoidDownload: boolean var that defines whether the profiles will NOT be downloaded (stored in this version).

        :return: 
			None if a queue is provided. Note that the values will be stored in the outQueue
			Else (p, url).
	'''
	logger = logging.getLogger("usufy")
	
	logger.info("Looking for profiles in " + str(p) + "...")
	try: 
		nProfiles = p.collectProfiles(outputFolder, action = action, avoidProcessing = avoidProcessing, avoidDownload = avoidDownload)
		logger.info("Up to " + str(nProfiles) +" processed for " + str(p) +"...")
		return (str(p), nProfiles)

	except:
		# Something happenned in the collectProfile
		logger.error("Something went wrong when processing " + str(p) + "collector")
		return (str(p), 0)
		
def performCollection(platforms = [], outputFolder = "./collector", nThreads = 12,  action = "start", avoidProcessing=False, avoidDownload=False):
	''' 
		Method that receives as a parameter a series of nicks and verifies whether those nicks have a profile associated in different social networks.

		List of parameters that the method receives:
		:param platforms:	list of <Platform> objects to be processed. 
		:param outputFolder:	local file where saving the obtained information.
		:param nThreads:	number of threads to start.
		:param action:	string containing the action.
		:param avoidProcessing:	boolean var that defines whether the profiles will NOT be processed.
		:param avoidDownload: boolean var that defines whether the profiles will NOT be downloaded (stored in this version).
		
		:return:
			Returns a dictionary where the key is the nick and the value another dictionary where the keys are the social networks and te value is the corresponding URL.
	'''
	logger = logging.getLogger("usufy")
	
	if platforms == []:
		platforms = config.getPlatforms(['all'])
	
	# Defining the output results variable
	res = {}
	# list of arguments
	args = []
	# We need to create all the arguments that will be needed
	for plat in platforms:
		args.append (( plat,  outputFolder, action, avoidProcessing, avoidDownload))
	logger.info("Launching " + str(nThreads) + " different threads...")
	# We define the pool
	pool = Pool(nThreads)
	# We call the wrapping function with all the args previously generated

	poolResults = pool.map(multi_run_wrapper,args)
	profiles = {}

	return res

def multi_run_wrapper(args):
	''' 
		Wrapper for being able to launch all the threads of getPageWrapper. 
		:param args: We receive the parameters for getPageWrapper as a tuple.
	'''
	return collectProfileWrapper(*args)


def user_collector_main(args):
	''' 
		Main function. This function is created in this way so as to let other applications make use of the full configuration capabilities of the application.	
	'''
	# Recovering the logger
	logger = utils.logger.setupUsufyLogger(args.verbose)
	# From now on, the logger can be recovered like this:
	logger = logging.getLogger("user-collector")
	
	logger.info("Starting user-collector.py...")

	if args.license:
		logger.info("Looking for the license...")
		# showing the license
		try:
			with open ("COPYING", "r") as iF:
				contenido = iF.read().splitlines()
				for linea in contenido:	
					print linea
				return contenido
		except Exception:
			logger.error("ERROR: there has been an error when opening the COPYING file.\n\tThe file contains the terms of the GPLv3 under which this software is distributed.\n\tIn case of doubts, verify the integrity of the files or contact contacto@i3visio.com.")
	else:
		logger.debug("Recovering the list of platforms to be processed...")
		# Recovering the list of platforms to be launched
		listPlatforms = config.getPlatforms(args.platforms, args.tags, mode = "user-collector")
		
		logger.info("Up to " + str(len(listPlatforms))+ " platforms recovered.")

		"""if args.info:
			# Information actions...
			if args.info == 'list_platforms':
				infoPlatforms="Listing the platforms:\n"
				for p in listPlatforms:
					infoPlatforms += "\t\t" + (str(p) + ": ").ljust(16, ' ') + str(p.tags)+"\n"
				logger.info(infoPlatforms)
				return infoPlatforms
			elif args.info == 'list_tags':
				logger.info("Listing the tags:")
				tags = {}
				# Going through all the selected platforms to get their tags
				for p in listPlatforms:
					for t in p.tags:
						if t not in tags.keys():
							tags[t] = 1
						else:
							tags[t] += 1
				infoTags = "List of tags:\n"
				# Displaying the results in a sorted list
				for t in tags.keys():
					infoTags += "\t\t" + (t + ": ").ljust(16, ' ') + str(tags[t]) + "  time(s)\n"
				logger.info(infoTags)
				return infoTags
			else:
				pass
			elif args.info == 'list_users':
				# Defining the list of users to monitor
				nicks = []
				logger.debug("Recovering nicknames to be processed...")
				if args.nicks:
					nicks = args.nicks
				else:
					# Reading the nick files
					try:
						nicks = args.list.read().splitlines()
					except:
						logger.error("ERROR: there has been an error when opening the file that stores the nicks.\tPlease, check the existence of this file.")			
			
				# Other actions
				logger.debug("Making basic transformations on the provided nicknames...")
				# Iterating to process _ and or .
				#nicks = profilesquatting.generatingProfiles(nicks, args.profilesquatting)
				nicks = profilesquatting.getNewNicks(nicks, logName = "usufy", modes = args.squatting, nonValidChars = args.nonvalid)
				logger.info("Obtained nicks:\n" + str(nicks))
				
				logger.debug("Profilesquatting nicknames recovered.")
						
				strNicks = ""
				for n in nicks:
					strNicks += n + "\n"
				logger.info("Generated nicks:\n\t ----------------\n" + strNicks)
				# Storing the file...
				logger.info("Creating output files as requested.")
				if not args.output_folder:
					args.output_folder = "./"
				else:
					# Verifying if the outputPath exists
					if not os.path.exists (args.output_folder):
						logger.warning("The output folder \'" + args.output_folder + "\' does not exist. The system will try to create it.")
						os.makedirs(args.output_folder)
						
				strTime = general.getCurrentStrDatetime()
				logger.info("Writing generated nicks to a text file.")
				with open (os.path.join(args.output_folder, "nicks_" + strTime +".txt"), "w") as oF:
					oF.write( strNicks )
				# if this option was selected, we will jsut return this and exist
				return nicks
				
		# Executing the corresponding process...
		else:"""
		if True:
			# if Verifying an output folder was selected
			logger.debug("Preparing the output folder...")
			if not os.path.exists(args.output_folder):
				logger.warning("The output folder \'" + args.output_folder + "\' does not exist. The system will try to create it.")
				os.makedirs(args.output_folder)
			# Launching the process...
			res = performCollection(listPlatforms, args.output_folder, nThreads=args.threads, action=args.action)
			print res
			# Generating summary files for each ...
			if args.extension:
				# Storing the file...
				logger.info("Creating output files as requested.")
				if not args.output_folder:
					args.output_folder = "./"
				else:
					# Verifying if the outputPath exists
					if not os.path.exists (args.output_folder):
						logger.warning("The output folder \'" + args.output_folder + "\' does not exist. The system will try to create it.")
						os.makedirs(args.output_folder)

				strTime = general.getCurrentStrDatetime()
				
				if  "csv" in args.extension:
					logger.info("Writing results to csv file")
					with open (os.path.join(args.output_folder, "results_" + strTime +".csv"), "w") as oF:
						oF.write( export_mod.resultsToCSV(res) + "\n" )
				if  "json" in args.extension:
					logger.info("Writing results to json file")
					with open (os.path.join(args.output_folder, "results_" + strTime + ".json"), "w") as oF:
						oF.write( export_mod.resultsToJson(res) + "\n")	
			allResults = []
						
			if len(res.keys()) > 0:
				logger.info("Listing the results obtained...")
				for nick in res.keys():
					if len(res[nick].keys()) > 0:
						results = "Results for '" + nick + "':\n"
						#values = generateProfile({nick: res[nick]})
						#results += str(values) + "\n"
						tags = []
						for plat in res[nick].keys():
							results+= "\t\t" + (str(plat) + ":").ljust(16, ' ') + res[nick][plat] + "\n"
						logger.info(results)
						allResults.append(results)
			return allResults

if __name__ == "__main__":
	print "user-collector.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014"
	print "This program comes with ABSOLUTELY NO WARRANTY."
	print "This is free software, and you are welcome to redistribute it under certain conditions."
	print "For details, run:"
	print "\tpython user-collector.py --license"
	print ""

	parser = argparse.ArgumentParser(description='user-collector.py - Piece of software that collects the users from a given platform.', prog='user-collector.py', epilog='Check the README.md file for further details on the usage of this program.', add_help=False)
	parser._optionals.title = "Input options (one required)"

	# Defining the mutually exclusive group for the main options
	#general = parser.add_mutually_exclusive_group(required=True)
	# Adding the main options
	#general.add_argument('-b', '--benchmark',  action='store_true', default=False, help='perform the benchmarking tasks.')
	#general.add_argument('-g', '--gui',  action='store_true', default=False, help='order to launch the GUI.')
	#general.add_argument('-l', '--list',  metavar='<path_to_nick_list>', action='store', type=argparse.FileType('r'), help='path to the file where the list of nicks to verify is stored (one per line).')
	#general.add_argument('-n', '--nicks', metavar='<nick>', nargs='+', action='store', help = 'the list of nicks to process (at least one is required).')
	#general.add_argument('--info', metavar='<action>', choices=['list_platforms', 'list_tags'], action='store', help='select the action to be performed amongst the following: list_platforms (list the details of the selected platforms), list_tags (list the tags of the selected platforms). Afterwards, it exists.')	


	# Selecting the platforms where performing the search
	groupPlatforms = parser.add_argument_group('Platform selection arguments', 'Criteria for selecting the platforms where performing the search.')
	groupPlatforms.add_argument('-p', '--platforms', metavar='<platform>', choices=['all', 'forocoches'], default = [], nargs='+', required=False, action='store', help='select the platforms where you want to perform the search amongst the following: all, forocoches. More than one option can be selected.')
	groupPlatforms.add_argument('-t', '--tags', metavar='<tag>', default = [], nargs='+', required=False, action='store', help='select the list of tags that fit the platforms in which you want to perform the search. More than one option can be selected.')

	# Configuring the processing options
	groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which usufy will process the identified profiles.')
	groupProcessing.add_argument('--avoid_download', required=False, action='store_true', default=False, help='argument to force usufy NOT to store the downloadable version of the profiles.')
	groupProcessing.add_argument('--avoid_processing', required=False, action='store_true', default=False, help='argument to force usufy NOT to perform any processing task with the valid profiles.')
	groupProcessing.add_argument('--nonvalid', metavar='<not_valid_characters>', required=False, default = '\\|<>=', action='store', help="string containing the characters considered as not valid for nicknames." )
	groupProcessing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'json'], required=False, action='store', help='output extension for the summary files (at least one is required).')
	groupProcessing.add_argument('-a', '--action', metavar='<action>', choices=['start', 'update', 'legacy'], required=False, default='start', action='store', help='action to perform the collection process: start (check all the users in the default range), update (update all the users and look for 1% more) and legacy (to recover the html already downloaded and process them correctly).')
	groupProcessing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, default = './collectors', action='store', help='output folder for the generated documents. While if the paths does not exist, user-collector.py will try to create it; if this argument is not provided, user-collector.py will NOT write any down any data. Check permissions if something goes wrong.')
	#groupProcessing.add_argument('-s', '--squatting', metavar='<level>',  nargs='+', choices=['basic', 'l33t', 'local', 'years', 'words', 'all'], required=False, default=[], action='store', help="select the level of profilesquatting to be looked for (in order of execution): words (for adding sensitive words such as 'real', 'home', 'news', etc.); l33t (l33t m0d3);  years (ending in numbers); local (looking for localized endings: '_es', '_en', '_fr', etc.); basic (changing '-', '.' and ' '); and all.")
	groupProcessing.add_argument('-T', '--threads', metavar='<num_threads>', required=False, action='store', default=32, type=int, help='write down the number of threads to be used (default 32). If 0, the maximum number possible will be used, which may make the system feel unstable.')
	groupProcessing.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2, 3], required=False, action='store', default=1, help='select the verbosity level: 0 - none; 1 - normal (default); 2 - debug.', type=int)

	# About options
	groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
	groupAbout.add_argument('-h', '--help', action='help', help='shows the version of the program and exists.')
	groupAbout.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3 license and exists.')
	groupAbout.add_argument('--version', action='version', version='%(prog)s 0.1.0', help='shows the version of the program and exists.')
		
	# recovering the parser
	args = parser.parse_args()	

	# Calling the main function
	user_collector_main(args)
