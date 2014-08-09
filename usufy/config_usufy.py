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

import os
import logging
# Importing Classes of <Platform> objects that will be used in the script. The files are stored in the wrappers folder.
# For demo only
#from wrappers.demo import Demo

from wrappers.px500 import Px500
from wrappers.about import About
from wrappers.adtriboo import Adtriboo
from wrappers.anarchy101 import Anarchy101
from wrappers.aporrealos import Aporrealos
from wrappers.backyardchickens import Backyardchickens
from wrappers.badoo import Badoo
from wrappers.bambuser import Bambuser
from wrappers.bebo import Bebo
from wrappers.behance import Behance
from wrappers.bitbucket import Bitbucket
from wrappers.bitcointalk import Bitcointalk
from wrappers.bitly import Bitly
from wrappers.blackplanet import Blackplanet
from wrappers.bladna import Bladna
from wrappers.blip import Blip
from wrappers.blogspot import Blogspot
from wrappers.burbuja import Burbuja
from wrappers.buzznet import Buzznet
from wrappers.cafemom import Cafemom
from wrappers.carbonmade import Carbonmade
from wrappers.care2 import Care2
from wrappers.connectingsingles import Connectingsingles
from wrappers.couchsurfing import Couchsurfing
from wrappers.dailymail import Dailymail
from wrappers.dailymotion import Dailymotion
from wrappers.delicious import Delicious
from wrappers.deviantart import Deviantart
from wrappers.disqus import Disqus
from wrappers.doodle import Doodle
from wrappers.douban import Douban
from wrappers.dribbble import Dribbble
from wrappers.ebay import Ebay
from wrappers.echatta import Echatta
from wrappers.elmundo import Elmundo
from wrappers.elpais import Elpais
from wrappers.enfemenino import Enfemenino
from wrappers.epinions import Epinions
from wrappers.etsy import Etsy
from wrappers.facebook import Facebook
from wrappers.fanpop import Fanpop
from wrappers.fark import Fark
from wrappers.favstar import Favstar
from wrappers.flickr import Flickr
from wrappers.flixster import Flixster
from wrappers.foodspotting import Foodspotting
from wrappers.forobtc import Forobtc
from wrappers.forocoches import Forocoches
from wrappers.forosperu import Forosperu
from wrappers.fotolog import Fotolog
from wrappers.foursquare import Foursquare
from wrappers.freebase import Freebase
from wrappers.friendfeed import Friendfeed
from wrappers.garage4hackers import Garage4hackers
from wrappers.gather import Gather
from wrappers.genspot import Genspot
from wrappers.getsatisfaction import Getsatisfaction
from wrappers.github import Github
from wrappers.gitorious import Gitorious
from wrappers.gogobot import Gogobot
from wrappers.goodreads import Goodreads
from wrappers.googleplus import GooglePlus
from wrappers.gsmspain import Gsmspain
from wrappers.hellboundhackers import Hellboundhackers
from wrappers.hi5 import Hi5
from wrappers.identica import Identica
from wrappers.imgur import Imgur
from wrappers.instagram import Instagram
from wrappers.instructables import Instructables
from wrappers.issuu import Issuu
from wrappers.ixgames import Ixgames
from wrappers.jamiiforums import Jamiiforums
from wrappers.kaboodle import Kaboodle
from wrappers.kali import Kali
from wrappers.karmacracy import Karmacracy
from wrappers.kickstarter import Kickstarter
from wrappers.kinja import Kinja
from wrappers.klout import Klout
from wrappers.kongregate import Kongregate
from wrappers.kupika import Kupika
from wrappers.lastfm import Lastfm
from wrappers.linkedin import Linkedin
from wrappers.livejournal import Livejournal
from wrappers.looki import Looki
from wrappers.marca import Marca
from wrappers.matchdoctor import Matchdoctor
from wrappers.mediavida import Mediavida
from wrappers.medium import Medium
from wrappers.meneame import Meneame
from wrappers.metacafe import Metacafe
from wrappers.migente import Migente
from wrappers.myeloma import Myeloma
from wrappers.myspace import Myspace
from wrappers.naver import Naver
from wrappers.netlog import Netlog
from wrappers.netvibes import Netvibes
from wrappers.occupywallst import Occupywallst
from wrappers.odnoklassniki import Odnoklassniki
from wrappers.pastebin import Pastebin
from wrappers.pearltrees import Pearltrees
from wrappers.peerbackers import Peerbackers
from wrappers.photobucket import Photobucket
from wrappers.pinterest import Pinterest
from wrappers.plancast import Plancast
from wrappers.pokerstrategy import Pokerstrategy
from wrappers.pornhub import Pornhub
from wrappers.qq import QQ
from wrappers.rankia import Rankia
from wrappers.ratemypoo import Ratemypoo
from wrappers.rebelmouse import Rebelmouse
from wrappers.reddit import Reddit
from wrappers.redtube import Redtube
from wrappers.researchgate import Researchgate
from wrappers.scribd import Scribd
from wrappers.sencha import Sencha
from wrappers.slashdot import Slashdot
from wrappers.slideshare import Slideshare
from wrappers.soundcloud import Soundcloud
from wrappers.sourceforge import Sourceforge
from wrappers.spaniards import Spaniards
from wrappers.spoj import Spoj
from wrappers.squidoo import Squidoo
from wrappers.stuff import Stuff
from wrappers.stumbleupon import Stumbleupon
from wrappers.steamcommunity import Steamcommunity
from wrappers.storify import Storify
from wrappers.streakgaming import Streakgaming
from wrappers.technorati import Technorati
from wrappers.theguardian import Theguardian
from wrappers.thehoodup import Thehoodup
from wrappers.thestudentroom import Thestudentroom
from wrappers.tradimo import Tradimo
from wrappers.tripadvisor import Tripadvisor
from wrappers.tumblr import Tumblr
from wrappers.tuporno import Tuporno
from wrappers.tvtag import Tvtag
from wrappers.twicsy import Twicsy
from wrappers.twitch import Twitch
from wrappers.twitpic import Twitpic
from wrappers.twitter import Twitter
from wrappers.ukdebate import Ukdebate
from wrappers.unsystem import Unsystem
from wrappers.ustream import Ustream
from wrappers.vimeo import Vimeo
from wrappers.vine import Vine
from wrappers.vk import Vk
from wrappers.weibo import Weibo
from wrappers.wefollow import Wefollow
from wrappers.winamp import Winamp
from wrappers.wishlistr import Wishlistr
from wrappers.wordpress import Wordpress
from wrappers.wykop import Wykop
from wrappers.xanga import Xanga
from wrappers.xing import Xing
from wrappers.xtube import Xtube
from wrappers.youku import Youku
from wrappers.youtube import Youtube
from wrappers.zabbix import Zabbix
# Add any additional import here
#from wrappers.any_new_social_network import Any_New_Social_Network
# ...
# Please, notify the authors if you have written a new wrapper.

from utils.credentials import Credential

# Get logger
import logging

def getPlatforms(sites=["all"], tags=[]):
	''' 
		Method that defines the list of <Platform> objects to be processed... Note that <Facebook> or <Twitter> objects inherit from <Platform>.

		Return values:
			Returns a list [] of <Platform> objects.
	'''
	listAll = []
	# For demo only
	#listAll.append(Demo())
	
	listAll.append(About())
	listAll.append(Adtriboo())
	listAll.append(Anarchy101())
	listAll.append(Aporrealos())
	listAll.append(Backyardchickens())
	listAll.append(Badoo())
	# Banned by the website
	#listAll.append(Bebo())
	listAll.append(Behance())
	listAll.append(Bitbucket())
	listAll.append(Bitcointalk())
	listAll.append(Bitly())
	listAll.append(Blackplanet())
	listAll.append(Bladna())
	listAll.append(Blip())
	listAll.append(Blogspot())
	listAll.append(Burbuja())
	listAll.append(Buzznet())
	listAll.append(Cafemom())
	listAll.append(Carbonmade())
	listAll.append(Care2())
	listAll.append(Connectingsingles())
	listAll.append(Couchsurfing())
	listAll.append(Dailymail())
	listAll.append(Dailymotion())
	listAll.append(Deviantart())
	listAll.append(Disqus())
	listAll.append(Doodle())
	listAll.append(Douban())
	listAll.append(Dribbble())
	# Pending of solving Issue #03. Requires execution of javascript
	#listAll.append(Delicious())	
	listAll.append(Ebay())
	listAll.append(Echatta())
	listAll.append(Elmundo())
	# Pending of javascript execution
	#listAll.append(Elpais())
	listAll.append(Enfemenino())
	listAll.append(Epinions())
	listAll.append(Etsy())
	listAll.append(Facebook())
	listAll.append(Fanpop())
	listAll.append(Favstar())
	listAll.append(Fark())
	listAll.append(Flickr())
	listAll.append(Flixster())
	listAll.append(Foodspotting())
	listAll.append(Forobtc())	
	listAll.append(Forocoches())
	listAll.append(Forosperu())
	# Too much time to recover the profile
	#listAll.append(Fotolog())
	listAll.append(Foursquare())
	listAll.append(Freebase())
	listAll.append(Friendfeed())
	listAll.append(Garage4hackers())
	listAll.append(Gather())
	listAll.append(Genspot())
	listAll.append(Getsatisfaction())
	listAll.append(Github())
	listAll.append(Gitorious())
	listAll.append(Gogobot())
	listAll.append(Goodreads())
	listAll.append(GooglePlus())
	listAll.append(Gsmspain())
	listAll.append(Hellboundhackers())
	listAll.append(Hi5())
	listAll.append(Identica())
	listAll.append(Imgur())
	listAll.append(Instagram())
	listAll.append(Instructables())
	listAll.append(Issuu())
	listAll.append(Ixgames())
	listAll.append(Jamiiforums())
	listAll.append(Kaboodle())
	listAll.append(Kali())
	listAll.append(Karmacracy())
	listAll.append(Kickstarter())
	listAll.append(Kinja())
	listAll.append(Klout())
	listAll.append(Kongregate())
	listAll.append(Kupika())
	listAll.append(Lastfm())
	listAll.append(Linkedin())
	listAll.append(Livejournal())
	listAll.append(Looki())
	listAll.append(Marca())
	listAll.append(Matchdoctor())
	listAll.append(Mediavida())
	listAll.append(Medium())
	listAll.append(Meneame())
	listAll.append(Metacafe())
	listAll.append(Migente())
	listAll.append(Myeloma())
	listAll.append(Myspace())
	listAll.append(Naver())
	listAll.append(Netlog())
	listAll.append(Netvibes())
	listAll.append(Occupywallst())
	listAll.append(Odnoklassniki())
	listAll.append(Pastebin())
	listAll.append(Pearltrees())
	listAll.append(Peerbackers())
	listAll.append(Photobucket())
	listAll.append(Pinterest())
	listAll.append(Plancast())
	listAll.append(Pokerstrategy())
	listAll.append(Pornhub())
	listAll.append(Px500())
	listAll.append(QQ())
	listAll.append(Rankia())
	listAll.append(Ratemypoo())
	listAll.append(Rebelmouse())
	listAll.append(Redtube())
	listAll.append(Researchgate())
	listAll.append(Scribd())
	listAll.append(Sencha())
	listAll.append(Slashdot())
	listAll.append(Slideshare())
	listAll.append(Soundcloud())
	listAll.append(Sourceforge())
	listAll.append(Storify())
	listAll.append(Stumbleupon())
	listAll.append(Spaniards())
	listAll.append(Spoj())
	listAll.append(Squidoo())
	listAll.append(Stuff())
	listAll.append(Steamcommunity())
	listAll.append(Streakgaming())
	listAll.append(Technorati())
	listAll.append(Theguardian())
	listAll.append(Thehoodup())
	listAll.append(Thestudentroom())
	listAll.append(Tradimo())
	listAll.append(Tripadvisor())
	listAll.append(Tumblr())
	listAll.append(Tuporno())
	listAll.append(Tvtag())
	listAll.append(Twicsy())
	listAll.append(Twitch())
	listAll.append(Twitpic())
	listAll.append(Twitter())
	listAll.append(Ukdebate())
	listAll.append(Unsystem())
	listAll.append(Ustream())
	listAll.append(Vimeo())
	# Pending of javascript execution
	#listAll.append(Vine())
	listAll.append(Vk())
	listAll.append(Xanga())
	listAll.append(Xing())
	listAll.append(Xtube())
	# Pending of javascript execution
	#listAll.append(Weibo())
	listAll.append(Winamp())
	listAll.append(Wefollow())
	listAll.append(Wishlistr())
	listAll.append(Wordpress())
	listAll.append(Wykop())
	listAll.append(Youku())
	listAll.append(Youtube())
	listAll.append(Zabbix())
	# append to the list variable whatever new <Platform> object that you want to add.
	#listAll.append(Any_New_Social_Network())

	creds = getCredentials()

	for p in listAll:
		if p.platformName.lower() in creds.keys():
			p.setCredentials(creds[p.platformName.lower()])

	if "all" in sites:
		return listAll
	else:
		listSelected = []
		for site in listAll:

			if site.platformName.lower() in sites:
				listSelected.append(site)		
			else:
				for tag in tags:
					if tag in site.tags:
						listSelected.append(site)		
		if len(listSelected) > 0:
			return listSelected
		else:
			return listAll


def getCredentials(filename=os.path.dirname(os.path.abspath(__file__))+"/utils/creds.txt"):
	''' 
		Calculating the score from a dictionary:
			{'Twitter': 'twitter.com/nick', 'Facebook': 'facebook.com/nick', ...}

		Values returned:
			score:	a float number.
	'''
	logger = logging.getLogger("usufy")
	# Dictionary of lists:
	# 	{'Twitter': {cred1, cred2, ...}}
	creds = {} 
	try:
		with open(filename, "r") as iF:
			contenido = iF.read().splitlines()
			#contenido = ["demo	champ2001	hacker"]
			for l in contenido:
				plat, user, password = l.split('\t')
				c = Credential(user, password)

				if plat not in creds.keys():
					creds[plat] = [c]
				else:
					creds[plat] = creds[plat].append(c)
			logger.debug(str(len(contenido)) + " were loaded.")	
			return creds
	except:
			logger.error("The credentials file "+filename+" could not be opened. The system will create an empty one instead.")
			try:
				with open(filename, "w") as oF:
					oF.write()
			except:			
				logger.error("An empty credentials file "+filename+" could not be created.")	
	logger.debug("No credentials were loaded.")	
	return {}
