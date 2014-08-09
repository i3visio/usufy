# -*- coding: cp1252 -*-
#
##################################################################################
#
#       This file is part of usufy.py.
#
#       Usufy is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

import argparse

def getParser():
	''' 
		Get Usufy parser...
	'''
	parser = argparse.ArgumentParser(description='usufy.py - Piece of software that checks the existence of a profile for a given user in a bunch of different platforms.', prog='usufy.py', epilog='Check the README.md file for further details on the usage of this program.', add_help=False)
	parser._optionals.title = "Input options (one required)"

	# Defining the mutually exclusive group for the main options
	general = parser.add_mutually_exclusive_group(required=True)
	# Adding the main options
	general.add_argument('--info', metavar='<action>', choices=['list_platforms', 'list_tags'], action='store', help='select the action to be performed amongst the following: list_platforms (list the details of the selected platforms) or list_tags (list the tags of the selected platforms).')
	general.add_argument('-b', '--benchmark',  action='store_true', default=False, help='perform the benchmarking tasks.')
	general.add_argument('-g', '--gui',  action='store_true', default=False, help='order to launch the GUI.')
	general.add_argument('-l', '--list',  metavar='<path_to_nick_list>', action='store', type=argparse.FileType('r'), help='path to the file where the list of nicks to verify is stored (one per line).')
	general.add_argument('-n', '--nicks', metavar='<nick>', nargs='+', action='store', help = 'the list of nicks to process (at least one is required).')

	# Selecting the platforms where performing the search
	groupPlatforms = parser.add_argument_group('Platform selection arguments', 'Criteria for selecting the platforms where performing the search.')
	groupPlatforms.add_argument('-p', '--platforms', metavar='<platform>', choices=['all', '500px', 'about', 'adtriboo', 'anarchy101', 'aporrealos', 'backyardchickens', 'badoo', 'bambuser', 'behance', 'bitbucket', 'bitcointalk', 'bitly', 'blip', 'blogspot', 'blackplanet', 'bladna', 'burbuja', 'buzznet', 'cafemom', 'carbonmade', 'care2', 'connectingsingles', 'couchsurfing', 'dailymail', 'dailymotion', 'deviantart', 'disqus', 'doodle', 'douban', 'dribbble','ebay','echatta', 'elmundo', 'enfemenino', 'epinions', 'etsy', 'facebook', 'fanpop', 'fark', 'favstar', 'flickr', 'flixster', 'foodspotting', 'forobtc', 'forocoches', 'forosperu', 'foursquare', 'freebase', 'friendfeed', 'garage4hackers', 'gather', 'genspot', 'getsatisfaction', 'github', 'gitorious', 'gogobot', 'goodreads',  'googleplus', 'gsmspain', 'hellboundhackers', 'hi5', 'identica', 'imgur', 'instagram','instructables', 'issuu', 'ixgames', 'jamiiforums', 'kaboodle', 'kali', 'karmacracy', 'kickstarter', 'kinja', 'klout', 'kongregate', 'kupika', 'lastfm', 'linkedin', 'livejournal', 'looki', 'marca', 'matchdoctor', 'mediavida', 'medium', 'meneame', 'metacafe', 'migente', 'myeloma', 'myspace', 'naver', 'netlog', 'netvibes', 'occupywallst', 'odnoklassniki', 'pastebin', 'pearltrees', 'peerbackers', 'pornhub', 'ratemypoo', 'rankia', 'redtube', 'scribd', 'sencha', 'slashdot', 'slideshare', 'soundcloud', 'sourceforge', 'steamcommunity', 'storify', 'spoj', 'spaniards', 'squidoo', 'streakgaming', 'stuff', 'stumbleupon', 'photobucket', 'pinterest', 'plancast', 'pokerstrategy', 'qq', 'rebelmouse', 'reddit', 'researchgate', 'technorati','theguardian', 'thehoodup', 'thestudentroom', 'tradimo', 'tripadvisor', 'tumblr','tuporno','tvtag', 'twicsy', 'twitch', 'twitpic', 'twitter','ukdebate', 'unsystem', 'ustream', 'vimeo', 'vk', 'wefollow', 'winamp', 'wishlistr', 'wordpress', 'wykop', 'xanga', 'xing', 'xtube', 'youku', 'youtube', 'zabbix'], default = [], nargs='+', required=False, action='store', help='select the platforms where you want to perform the search amongst the following: all, 500px, about, adtriboo, anarchy101, aporrealos, backyardchickens, badoo, bambuser, behance, bitbucket, bitcointalk, bitly, blip, blogspot, blackplanet, bladna, burbuja, buzznet, cafemom, carbonmade, care2, connectingsingles, couchsurfing, dailymail, dailymotion, delicious, deviantart, disqus, doodle, douban, dribbble, ebay, echatta, elmundo, enfemenino, epinions, etsy, facebook, fanpop, fark, favstar, flickr, flixster, foodspotting, forobtc, forocoches, forosperu, fotolog, foursquare, freebase, friendfeed, garage4hackers, gather, genspot, getsatisfaction, github, gitorious, gogobot, goodreads, googleplus, gsmspain, hellboundhackers, hi5, identica, imgur, instagram, instructables, issuu, ixgames, jamiiforums, kaboodle, kali, karmacracy, kickstarter, kinja, klout, kongregate, kupika, lastfm, linkedin, livejournal, looki, marca, matchdoctor, mediavida, medium, meneame, metacafe, migente, myeloma, myspace, naver, netlog, netvibes, occupywallst, odnoklassniki, pastebin, pearltrees, peerbackers, photobucket, pinterest, plancast, pokerstrategy, pornhub, qq, ratemypoo, rankia, rebelmouse, reddit, redtube, researchgate, scribd, sencha, slideshare, slashdot, soundcloud, sourceforge, steamcommunity, storify, spaniards, spoj, squidoo, stuff, stumbleupon, streakgaming, theguardian, thehoodup, technorati, thestudentroom, tradimo, tripadvisor, tumblr, tuporno, tvtag, twicsy, twitpic, twitch, twitter, ukdebate, unsystem, ustream, vimeo, vk, wefollow, winamp, wishlistr, wordpress, wykop, xanga, xing, xtube, youku, youtube, zabbix. More than one option can be selected.')

	groupPlatforms.add_argument('-t', '--tags', metavar='<tag>', default = [], nargs='+', required=False, action='store', help='select the list of tags that fit the platforms in which you want to perform the search. More than one option can be selected.')

	# Configuring the processing options
	groupProcessing = parser.add_argument_group('Processing arguments', 'Configuring the way in which usufy will process the identified profiles.')
        groupProcessing.add_argument('-a', '--avoid_processing', required=False, action='store_true', default=False, help='argument to force usufy NOT to process the downloaded valid profiles.')
	groupProcessing.add_argument('-e', '--extension', metavar='<sum_ext>', nargs='+', choices=['csv', 'json'], required=False, action='store', help='output extension for the summary files (at least one is required).')
	groupProcessing.add_argument('-o', '--output_folder', metavar='<path_to_output_folder>', required=False, action='store', help='output folder for the generated documents. While if the paths does not exist, usufy.py will try to create; if this argument is not provided, usufy will NOT write any down any data. Check permissions if something goes wrong.')
	groupProcessing.add_argument('-T', '--threads', metavar='<num_threads>', required=False, action='store', default=32, type=int, help='write down the number of threads to be used (default 32). If 0, the maximum number possible will be used, which may make the system feel unstable.')
	groupProcessing.add_argument('-v', '--verbose', metavar='<verbosity>', choices=[0, 1, 2, 3], required=False, action='store', default=1, help='select the verbosity level: 0 - none; 1 - normal (default); 2 - debug.', type=int)

	# About options
	groupAbout = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
	groupAbout.add_argument('-h', '--help', action='help', help='shows the version of the program and exists.')
        groupAbout.add_argument('--license', required=False, action='store_true', default=False, help='shows the GPLv3 license.')
	groupAbout.add_argument('--version', action='version', version='%(prog)s 1.3.0b', help='shows the version of the program and exists.')

	return parser
