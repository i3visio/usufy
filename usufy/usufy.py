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
	python usufy.py --license
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

# global issues
from multiprocessing import Process, Queue, Pool

# configuration and utils
import config_usufy as config
import utils.analyser as analyser
import utils.attributes as attributes
import utils.benchmark as benchmark
import utils.export as export_mod
import utils.profilesquatting as profilesquatting
import utils.usufyparser as usufyparser
import g_usufy as usufygui 
import utils.usufybrowser as usufybrowser

# logging imports
import utils.logger
import logging
	
def getPageWrapper(p, nick, rutaDescarga, avoidProcessing, outQueue=None):
	''' 
		Method that wraps the call to the getUserPage.

		List of parameters that the method receives:
		p:		platform where the information is stored.
		nick:		nick to be searched.
		rutaDescarga:	local file where saving the obtained information.
		avoidProcessing:boolean var that defines whether the profiles will NOT be processed (stored in this version).
		outQueue:	Queue where the information will be stored.

                Return values:
			None if a queue is provided. Note that the values will be stored in the outQueue
			Else (p, url).
	'''
	logger = logging.getLogger("usufy")
	
	logger.debug("\tLooking for profiles in " + str(p) + "...")
	url = p.getUserPage(nick, rutaDescarga, avoidProcessing)			
	if url != None:
		if outQueue != None:
			logger.info("\t" + (str(p) +" - User profile found: ").ljust(40, ' ') + url)
			# Storing in the output queue the values
			outQueue.put((p, url))
		else:
			# If no queue was given, return the value normally
			return (p, url)
	else: 
		logger.debug("\t" + str(p) +" - User profile not found...")


def processNickList(nicks, platforms=None, rutaDescarga=None, avoidProcessing=True, nThreads=12):
	''' 
		Method that receives as a parameter a series of nicks and verifies whether those nicks have a profile associated in different social networks.

		List of parameters that the method receives:
		nicks:		list of nicks to process.
		platforms:	list of <Platform> objects to be processed. 
		rutaDescarga:	local file where saving the obtained information.
		avoidProcessing:boolean var that defines whether the profiles will NOT be processed (stored in this version).

		Return values:
			Returns a dictionary where the key is the nick and the value another dictionary where the keys are the social networks and te value is the corresponding URL.
	'''
	logger = logging.getLogger("usufy")
	
	if platforms == None:
		platforms = config.getPlatforms()
	
	# Defining the output results variable
	res = {}
	
	# Processing the whole list of terms...
	for nick in nicks:
		logger.info("Looking for '" + nick + "' in " + str(len(platforms)) + " different platforms:\n" +str( [ str(plat) for plat in platforms ] ) )
	
		# If the process is executed by the current app, we use the Processes. It is faster than pools.
		if nThreads == 0:
			logger.warning("Launching usufy.py using as many threads as possible. The system may feel unstable. If something happends, try usufy.py appending -T 32, -T 64, etc. to control the maximum number of threads created by the app.")
			# defining the Queue where the results will be stored
			outQueue = Queue()
			
			# List of processes to be used
			processes = []
			for p in platforms:
				# We're setting all the arguments to be used, adding the output queue
				proc = Process(target=getPageWrapper, args=(p, nick, rutaDescarga, avoidProcessing, outQueue))
				# Adding the process to a list:
				processes.append(proc)
				# Starting the computing of the process... 
				proc.start()

			# Wait for all process to finish
			for p in processes:
				p.join()

			profiles = {}

			# Recovering all results and generating the dictionary
			while not outQueue.empty():
				# Recovering the results
				p, url = outQueue.get() 
				profiles[p] = url

			# Storing in a global variable to be returned
			res[nick] = profiles
                # Using threads in a pool if we are not running the program in main
		else:
			args = []
			# We need to create all the arguments that will be needed
			for plat in platforms:
				args.append (( plat, nick, rutaDescarga, avoidProcessing))
			logger.info("Launching " + str(nThreads) + " different threads...")
			# We define the pool
			pool = Pool(nThreads)
			# We call the wrapping function with all the args previously generated

			poolResults = pool.map(multi_run_wrapper,args)
			profiles = {}

			for r in poolResults:
				# We need to recover the results and check if they are not None
				if r != None:
					p, url = r
					profiles[p] = url
			res[nick] = profiles
	return res

def multi_run_wrapper(args):
	''' 
	Wrapper for being able to launch all the threads of getPageWrapper. 
	Parameters:
		We receive the parameters for getPageWrapper as a tuple.
	'''
	return getPageWrapper(*args)


def usufy_main(args):
	''' 
		Main function. This function is created in this way so as to let other applications make use of the full configuration capabilities of the application.	
	'''
	# Recovering the logger
	logger = utils.logger.setupUsufyLogger(args.verbose)
	# From now on, the logger can be recovered like this:
	logger = logging.getLogger("usufy")
	
	logger.info("Starting usufy.py...")

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
		listPlatforms = config.getPlatforms(args.platforms, args.tags)
		logger.debug("Platforms recovered.")

		if args.info:
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
				# Other actions
				pass
		# launching the GUI
		elif args.gui:
			logger.info("Launching GUI...")
			usufygui.UsufyGUI()
		# performing the test
		elif args.benchmark:
			logger.warning("The benchmark mode may last some minutes as it will be performing similar queries to the ones performed by the program in production. ")
			logger.info("Launching the benchmarking tests...")
			platforms = config.getPlatforms()
			res = benchmark.doBenchmark(platforms)
			strTimes = ""
			for e in sorted(res.keys()):
				strTimes += str(e) + "\t" + str(res[e]) + "\n"
			logger.info(strTimes)
			return strTimes
		# Executing the corresponding process...
		else:
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

			logger.debug("Making basic transformations on the provided nicknames...")
			# Iterating to process _ and or .
			nicks = profilesquatting.generatingProfiles(nicks)
			logger.debug("Nicknames recovered.")

			if args.output_folder != None:	
				# if Verifying an output folder was selected
				logger.debug("Preparing the output folder...")
				if not os.path.exists(args.output_folder):
					logger.warning("The output folder \'" + args.output_folder + "\' does not exist. The system will try to create it.")
					os.makedirs(args.output_folder)
				# Launching the process...
				res = processNickList(nicks, listPlatforms, args.output_folder, args.avoid_processing, nThreads=args.threads)
			else:
				res = processNickList(nicks, listPlatforms, nThreads=args.threads)
					
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
				if  "csv" in args.extension:
					logger.info("Writing results to csv file")
					with open (os.path.join(args.output_folder, "results.csv"), "w") as oF:
						oF.write( export_mod.resultsToCSV(res) + "\n" )
				if  "json" in args.extension:
					logger.info("Writing results to json file")
					with open (os.path.join(args.output_folder, "results.json"), "w") as oF:
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
	print "usufy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014"
	print "This program comes with ABSOLUTELY NO WARRANTY."
	print "This is free software, and you are welcome to redistribute it under certain conditions."
	print "For details, run:"
	print "\tpython usufy.py --license"
	print ""

	# recovering the parser
	parser = usufyparser.getParser()

	args = parser.parse_args()	

	# Calling the main function
	usufy_main(args)
