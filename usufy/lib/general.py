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

import hashlib
import json
import datetime

def dictToJson(d):
	'''
		Workaround to convert any dictionary to json text.
		
		:param dict:	Dictionary to convert to json.

		:return:	jsonText (string).
	'''
	# creating json
	jsonText =  json.dumps(d)
	return jsonText


def fileToMD5(filename, block_size=256*128, binary=False):
	'''
		:param filename:	Path to the file.
		:param block_size:	Chunks of suitable size. Block size directly depends on the block size of your filesystem to avoid performances issues. Blocks of 4096 octets (Default NTFS).
		:return:	md5 hash.
	'''
	md5 = hashlib.md5()
	with open(filename,'rb') as f: 
		for chunk in iter(lambda: f.read(block_size), b''): 
			 md5.update(chunk)
	if not binary:
		return md5.hexdigest()
	return md5.digest()


def getCurrentStrDatetime():
	'''
		Generating the current Datetime with a given format.

		:return:	strTime
	'''
	# Generating current time
	i = datetime.datetime.now()
	strTime = "%s-%s-%s_%sh%sm" % (i.year, i.month, i.day, i.hour, i.minute)
	return strTime
	
def getFilesFromAFolder(path):
	'''
		Getting all the files in a folder.
		
		:param path:	path in which looking for files.
		
		:return:	list of filenames.
	'''
	from os import listdir
	from os.path import isfile, join
	#onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
	onlyFiles = []
	for f in listdir(path):
		if isfile(join(path, f)):
			onlyFiles.append(f)
	return onlyFiles
	

