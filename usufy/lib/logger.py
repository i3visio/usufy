import usufy
import logging
import os

def setupUsufyLogger(verbosity):

        """ 
                Returns the logger to be used for the whole app.
        """
	logger = logging.getLogger("usufy")

	# create a logging format
	loginFormat = '%(asctime)s - %(filename)s - %(levelname)s:\n\t %(message)s\n'

	formatter = logging.Formatter(loginFormat)

	# verifying if the logs folder exist
	logFolder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../logs")
	if not os.path.exists(logFolder):
		os.makedirs(logFolder)
	# create a file handler
	logFile = os.path.join(logFolder, "usufy.log")

	# first, defining the type of standard output and verbosity 
        if verbosity == 0:
		logging.basicConfig(level=logging.ERROR, format=loginFormat)
        elif verbosity == 1:
		logging.basicConfig(level=logging.INFO, format=loginFormat)
        elif verbosity == 2:
		logging.basicConfig(level=logging.DEBUG, format=loginFormat)
	
	# This adds a handler to write on a file
	handler = logging.FileHandler(logFile)
	handler.setLevel(logging.DEBUG)
	formatter = logging.Formatter(loginFormat)
	handler.setFormatter(formatter)
	
	# add the handlers to the logger
	logger.addHandler(handler)
	return logger

