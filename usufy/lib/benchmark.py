

import time
# global issues
from multiprocessing import Pool

import logging
import urllib2

def testFunction(p):
	'''
		Benchmarcking function...
	'''
	#print p
	resp = urllib2.urlopen('http://www.usufy.com')
	html = resp.read()
	return 
	
def testFunction2(p):
	'''
		Benchmarcking function...
	'''
	a = 1
	for i in range(1000):
		a+=1
	return
	
def multi_run_wrapper(args):
	''' 
	Wrapper for being able to launch all the threads of getPageWrapper. 
	Parameters:
		We receive the parameters for getPageWrapper as a tuple.
	'''
	#print args
	return testFunction(*args)	
	
def doBenchmark(plats):
	'''
		Perform the benchmark...
	'''
	logger = logging.getLogger("usufy")
	# defining the results dict
	res = {}
	
	# args
	args = []
	
	for p in plats:
		args.append( (str(p),) )
	
	# selecting the number of tries to be performed
	tries = [1, 4, 8 ,16, 32, 64]
	
	#for i in range(1, len(plats)/10):
	#	tries.append(i*10)
	
	logger.info("The test is starting recovering webpages by creating the following series of threads: " + str(tries))
	
	for i in tries:
		print "Testing usufy.py creating " + str(i) + " simultaneous threads..."
		# starting 
		t0 = time.clock()
		pool = Pool(i)
		# We call the wrapping function with all the args previously generated
		poolResults = pool.map(multi_run_wrapper, args)  
		
		t1 = time.clock()
		# storing the results
		res[i] = t1 - t0
		print str(i) + "\t" + str(res[i]) + "\n"
	
	return res