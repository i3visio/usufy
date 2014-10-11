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
from wrappers.adtriboo import Adtriboo
from wrappers.anarchy101 import Anarchy101
from wrappers.aporrealos import Aporrealos
from wrappers.apsense import Apsense
from wrappers.arduino import Arduino
from wrappers.ariva import Ariva
from wrappers.armorgames import Armorgames
from wrappers.artbreak import Artbreak
from wrappers.artician import Artician
from wrappers.arto import Arto
from wrappers.askfm import Askfm
from wrappers.audiob import Audiob
from wrappers.audioboo import Audioboo
from wrappers.authorstream import Authorstream
from wrappers.autospies import Autospies
from wrappers.backyardchickens import Backyardchickens
from wrappers.badoo import Badoo
from wrappers.behance import Behance
from wrappers.bennugd import Bennugd
from wrappers.bitbucket import Bitbucket
from wrappers.bitcointalk import Bitcointalk
from wrappers.bitly import Bitly
from wrappers.blackplanet import Blackplanet
from wrappers.bladna import Bladna
from wrappers.blip import Blip
from wrappers.blogspot import Blogspot
from wrappers.bookmarky import Bookmarky
from wrappers.boonex import Boonex
from wrappers.bookofmatches import Bookofmatches
from wrappers.bordom import Bordom
from wrappers.boxedup import Boxedup
from wrappers.breakcom import Breakcom
from wrappers.bucketlistly import Bucketlistly
from wrappers.burbuja import Burbuja
from wrappers.burdastyle import Burdastyle
from wrappers.buzznet import Buzznet
from wrappers.cafemom import Cafemom
from wrappers.carbonmade import Carbonmade
from wrappers.cardomain import Cardomain
from wrappers.care2 import Care2
from wrappers.castroller import Castroller
from wrappers.causes import Causes
from wrappers.ccsinfo import Ccsinfo
from wrappers.chess import Chess
from wrappers.cockos import Cockos
from wrappers.connectingsingles import Connectingsingles
from wrappers.couchsurfing import Couchsurfing
from wrappers.dailymail import Dailymail
from wrappers.dailymotion import Dailymotion
from wrappers.deviantart import Deviantart
from wrappers.digitalspy import Digitalspy
from wrappers.disqus import Disqus
from wrappers.doodle import Doodle
from wrappers.douban import Douban
from wrappers.dribbble import Dribbble
from wrappers.drupal import Drupal
from wrappers.drugbuyersforum import Drugbuyersforum
from wrappers.ebay import Ebay
from wrappers.echatta import Echatta
from wrappers.elmundo import Elmundo
from wrappers.enfemenino import Enfemenino
from wrappers.epinions import Epinions
from wrappers.eqe import Eqe
from wrappers.ethereum import Ethereum
from wrappers.etsy import Etsy
from wrappers.evilzone import Evilzone
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
from wrappers.foursquare import Foursquare
from wrappers.freebase import Freebase
from wrappers.freerepublic import Freerepublic
from wrappers.friendfeed import Friendfeed
from wrappers.gametracker import Gametracker
from wrappers.gapyear import Gapyear
from wrappers.garage4hackers import Garage4hackers
from wrappers.gather import Gather
from wrappers.geeksphone import Geeksphone
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
from wrappers.ibosocial import Ibosocial
from wrappers.identica import Identica
from wrappers.imgur import Imgur
from wrappers.instagram import Instagram
from wrappers.instructables import Instructables
from wrappers.interracialmatch import Interracialmatch
from wrappers.intersect import Intersect
from wrappers.intfiction import Intfiction
from wrappers.islamicawakening import Islamicawakening
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
from wrappers.mcneel import Mcneel
from wrappers.mediavida import Mediavida
from wrappers.medium import Medium
from wrappers.meneame import Meneame
from wrappers.metacafe import Metacafe
from wrappers.migente import Migente
from wrappers.minecraft import Minecraft
from wrappers.musicasacra import Musicasacra
from wrappers.myeloma import Myeloma
from wrappers.myspace import Myspace
from wrappers.naver import Naver
from wrappers.netlog import Netlog
from wrappers.netvibes import Netvibes
from wrappers.occupywallst import Occupywallst
from wrappers.odnoklassniki import Odnoklassniki
from wrappers.openframeworks import Openframeworks
from wrappers.oroom import Oroom
from wrappers.pastebin import Pastebin
from wrappers.pearltrees import Pearltrees
from wrappers.peerbackers import Peerbackers
from wrappers.photobucket import Photobucket
from wrappers.pinterest import Pinterest
from wrappers.pixinsight import Pixinsight
from wrappers.pjrc import Pjrc
from wrappers.plancast import Plancast
from wrappers.pokerred import Pokerred
from wrappers.pokerstrategy import Pokerstrategy
from wrappers.pornhub import Pornhub
from wrappers.proboards import Proboards
from wrappers.pz import Pz
from wrappers.qq import QQ
from wrappers.quartermoonsaloon import Quartermoonsaloon
from wrappers.rankia import Rankia
from wrappers.rapid import Rapid
from wrappers.ratemypoo import Ratemypoo
from wrappers.rawtherapee import Rawtherapee
from wrappers.rebelmouse import Rebelmouse
from wrappers.redtube import Redtube
from wrappers.relatious import Relatious
from wrappers.researchgate import Researchgate
from wrappers.rojadirecta import Rojadirecta
from wrappers.ruby import Ruby
from wrappers.scribd import Scribd
from wrappers.sencha import Sencha
from wrappers.skype import Skype
from wrappers.slashdot import Slashdot
from wrappers.slideshare import Slideshare
from wrappers.smartcitizen import Smartcitizen
from wrappers.sokule import Sokule
from wrappers.soundcloud import Soundcloud
from wrappers.sourceforge import Sourceforge
from wrappers.spaniards import Spaniards
from wrappers.spoj import Spoj
from wrappers.spotify import Spotify
from wrappers.squidoo import Squidoo
from wrappers.steamcommunity import Steamcommunity
from wrappers.steinberg import Steinberg
from wrappers.streakgaming import Streakgaming
from wrappers.stuff import Stuff
from wrappers.stumbleupon import Stumbleupon
from wrappers.teamtreehouse import Teamtreehouse
from wrappers.techcrunch import Techcrunch
from wrappers.thecarcommunity import Thecarcommunity
from wrappers.theguardian import Theguardian
from wrappers.thehoodup import Thehoodup
from wrappers.thesims import Thesims
from wrappers.thestudentroom import Thestudentroom
from wrappers.tradimo import Tradimo
from wrappers.travian import Travian
from wrappers.tripadvisor import Tripadvisor
from wrappers.tripit import Tripit
from wrappers.trulia import Trulia
from wrappers.tumblr import Tumblr
from wrappers.tuporno import Tuporno
from wrappers.tvtag import Tvtag
from wrappers.twicsy import Twicsy
from wrappers.twitch import Twitch
from wrappers.twoplustwo import Twoplustwo
from wrappers.twitpic import Twitpic
from wrappers.twitter import Twitter
from wrappers.ukdebate import Ukdebate
from wrappers.ummahforum import Ummahforum
from wrappers.unsystem import Unsystem
from wrappers.ustream import Ustream
from wrappers.vexforum import Vexforum
from wrappers.vimeo import Vimeo
from wrappers.videohelp import Videohelp
from wrappers.virustotal import Virustotal
from wrappers.vk import Vk
from wrappers.wefollow import Wefollow
from wrappers.wikipediaar import WikipediaAr
from wrappers.wikipediaca import WikipediaCa
from wrappers.wikipediade import WikipediaDe
from wrappers.wikipediaen import WikipediaEn
from wrappers.wikipediaes import WikipediaEs
from wrappers.wikipediaeu import WikipediaEu
from wrappers.winamp import Winamp
from wrappers.wishlistr import Wishlistr
from wrappers.wordpress import Wordpress
from wrappers.wykop import Wykop
from wrappers.xanga import Xanga
from wrappers.xat import Xat
from wrappers.xing import Xing
from wrappers.xtube import Xtube
from wrappers.youku import Youku
from wrappers.youtube import Youtube
from wrappers.zabbix import Zabbix
from wrappers.zentyal import Zentyal
################################
# Automatically generated code #
################################
# <ADD_HERE_THE_NEW_IMPORTS>
# Add any additional import here
#from wrappers.any_new_social_network import Any_New_Social_Network
# ...
# Please, notify the authors if you have written a new wrapper.

from lib.credentials import Credential

# Get logger
import logging

def getPlatforms(sites=["all"], tags=[], mode="usufy"):
	''' 
		Method that defines the list of <Platform> objects to be processed... Note that <Facebook> or <Twitter> objects inherit from <Platform>.

		Parameters:
			:param sites:	A list of platforms: 'all', 'twitter', facebook', ...
			:param tags:	A list of the tags of the looked platforms: 'news', 'social', ...
			:param mode:	A string containing the mode: "usufy", "user-collector", "parser"...
		
		Return values:
			Returns a list [] of <Platform> objects.
	'''
	listAll = []
	listAll.append(Adtriboo())
	listAll.append(Anarchy101())
	listAll.append(Apsense())
	listAll.append(Aporrealos())
	listAll.append(Ariva())
	listAll.append(Arduino())
	listAll.append(Armorgames())
	listAll.append(Artbreak())
	listAll.append(Artician())
	listAll.append(Arto())
	listAll.append(Askfm())
	listAll.append(Audiob())
	listAll.append(Audioboo())
	listAll.append(Authorstream())
	listAll.append(Autospies())
	listAll.append(Backyardchickens())
	listAll.append(Badoo())
	listAll.append(Behance())
	listAll.append(Bennugd())
	listAll.append(Bitbucket())
	listAll.append(Bitcointalk())
	listAll.append(Bitly())
	listAll.append(Blackplanet())
	listAll.append(Bladna())
	listAll.append(Blip())
	listAll.append(Blogspot())
	listAll.append(Bookmarky())
	listAll.append(Bookofmatches())
	listAll.append(Boonex())
	listAll.append(Bordom())
	listAll.append(Boxedup())
	listAll.append(Breakcom())
	listAll.append(Bucketlistly())
	listAll.append(Burbuja())
	listAll.append(Burdastyle())
	listAll.append(Buzznet())
	listAll.append(Cafemom())
	listAll.append(Carbonmade())
	listAll.append(Cardomain())
	listAll.append(Care2())
	listAll.append(Castroller())
	listAll.append(Causes())
	listAll.append(Ccsinfo())
	listAll.append(Chess())
	listAll.append(Cockos())
	listAll.append(Connectingsingles())
	listAll.append(Couchsurfing())
	listAll.append(Dailymail())
	listAll.append(Dailymotion())
	listAll.append(Deviantart())
	listAll.append(Digitalspy())
	listAll.append(Disqus())
	listAll.append(Doodle())
	listAll.append(Douban())
	listAll.append(Dribbble())
	listAll.append(Drugbuyersforum())	
	listAll.append(Drupal())
	listAll.append(Ebay())
	listAll.append(Echatta())
	listAll.append(Elmundo())
	listAll.append(Enfemenino())
	listAll.append(Epinions())
	listAll.append(Eqe())
	listAll.append(Ethereum())
	listAll.append(Etsy())
	listAll.append(Evilzone())
	listAll.append(Facebook())
	listAll.append(Fanpop())
	listAll.append(Fark())
	listAll.append(Favstar())
	listAll.append(Flickr())
	listAll.append(Flixster())
	listAll.append(Foodspotting())
	listAll.append(Forobtc())	
	listAll.append(Forocoches())
	listAll.append(Forosperu())
	listAll.append(Foursquare())
	listAll.append(Freebase())
	listAll.append(Freerepublic())
	listAll.append(Friendfeed())
	listAll.append(Gametracker())
	listAll.append(Gapyear())
	listAll.append(Garage4hackers())
	listAll.append(Gather())
	listAll.append(Geeksphone())
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
	listAll.append(Ibosocial())
	listAll.append(Identica())
	listAll.append(Imgur())
	listAll.append(Instagram())
	listAll.append(Interracialmatch())
	listAll.append(Intersect())
	listAll.append(Intfiction())
	listAll.append(Instructables())
	listAll.append(Islamicawakening())
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
	listAll.append(Mcneel())
	listAll.append(Mediavida())
	listAll.append(Medium())
	listAll.append(Meneame())
	listAll.append(Metacafe())
	listAll.append(Migente())
	listAll.append(Minecraft())
	listAll.append(Musicasacra())
	listAll.append(Myeloma())
	listAll.append(Myspace())
	listAll.append(Naver())
	listAll.append(Netlog())
	listAll.append(Netvibes())
	listAll.append(Occupywallst())
	listAll.append(Odnoklassniki())
	listAll.append(Openframeworks())
	listAll.append(Oroom())
	listAll.append(Pastebin())
	listAll.append(Pearltrees())
	listAll.append(Peerbackers())
	listAll.append(Photobucket())	
	listAll.append(Pinterest())
	listAll.append(Pixinsight())
	listAll.append(Pjrc())
	listAll.append(Plancast())
	listAll.append(Pokerred())
	listAll.append(Pokerstrategy())
	listAll.append(Pornhub())
	listAll.append(Proboards())
	listAll.append(Px500())
	listAll.append(Pz())
	listAll.append(QQ())
	listAll.append(Quartermoonsaloon())
	listAll.append(Rankia())
	listAll.append(Rapid())
	listAll.append(Ratemypoo())
	listAll.append(Rawtherapee())
	listAll.append(Rebelmouse())
	listAll.append(Redtube())
	listAll.append(Relatious())
	listAll.append(Researchgate())
	listAll.append(Rojadirecta())
	listAll.append(Ruby())
	listAll.append(Scribd())
	listAll.append(Sencha())
	listAll.append(Skype())
	listAll.append(Slashdot())
	listAll.append(Slideshare())
	listAll.append(Smartcitizen())
	listAll.append(Sokule())
	listAll.append(Soundcloud())
	listAll.append(Sourceforge())
	listAll.append(Spaniards())
	listAll.append(Spoj())
	listAll.append(Spotify())
	listAll.append(Squidoo())
	listAll.append(Steamcommunity())
	listAll.append(Steinberg())
	listAll.append(Streakgaming())
	listAll.append(Stuff())
	listAll.append(Stumbleupon())
	listAll.append(Teamtreehouse())
	listAll.append(Techcrunch())
	listAll.append(Thecarcommunity())
	listAll.append(Theguardian())
	listAll.append(Thehoodup())
	listAll.append(Thesims())
	listAll.append(Thestudentroom())
	listAll.append(Tradimo())
	listAll.append(Travian())
	listAll.append(Tripadvisor())
	listAll.append(Tripit())
	listAll.append(Trulia())
	listAll.append(Tumblr())
	listAll.append(Tuporno())
	listAll.append(Tvtag())
	listAll.append(Twicsy())
	listAll.append(Twitch())
	listAll.append(Twitpic())
	listAll.append(Twitter())
	listAll.append(Twoplustwo())
	listAll.append(Ukdebate())
	listAll.append(Ummahforum())
	listAll.append(Unsystem())
	listAll.append(Ustream())
	listAll.append(Vexforum())
	listAll.append(Videohelp())
	listAll.append(Vimeo())
	listAll.append(Virustotal())
	listAll.append(Vk())
	listAll.append(Wefollow())
	listAll.append(WikipediaAr())
	listAll.append(WikipediaCa())
	listAll.append(WikipediaDe())
	listAll.append(WikipediaEn())
	listAll.append(WikipediaEs())
	listAll.append(WikipediaEu())
	listAll.append(Winamp())
	listAll.append(Wishlistr())
	listAll.append(Wordpress())
	listAll.append(Wykop())
	listAll.append(Xanga())
	listAll.append(Xat())
	listAll.append(Xing())
	listAll.append(Xtube())
	listAll.append(Youku())
	listAll.append(Youtube())
	listAll.append(Zabbix())
	listAll.append(Zentyal())
	################################
	# Automatically generated code #
	################################
	# append to the list variable whatever new <Platform> object that you want to add.
	#listAll.append(Any_New_Social_Network())
	# <ADD_HERE_THE_NEW_PLATFORMS>

	# sorting the platforms
	listAll.sort()

	if mode == "parser":
		return listAll

	creds = getCredentials()

	for p in listAll:
		if p.platformName.lower() in creds.keys():
			p.setCredentials(creds[p.platformName.lower()])

	listSelected = []	
	
	if "all" in sites:
		for p in listAll:
			# [TO-DO]
			#	Removing exceptions by updating ALL the wrappers
			if mode == "usufy":
				try:
					if p.url:
						listSelected.append(p)
				except:
					# if the hasUsufy parameter was NOT found, we assume that it is because it is an old wrapper
					#	All of them have implemented Usufy
					listSelected.append(p)
			elif mode == "user-collector":
				try:
					if p.urlEnumeration:
						listSelected.append(p)
				except:
					# if the hasUsufy parameter was NOT found, we assume that it is because it is an old wrapper
					#	This platform has not implemented yet the enumeration.
					pass
		return listSelected
	else:
		for plat in listAll:
			added = False
			for s in sites:
				if s in str(plat).lower():
					# [TO-DO]
					#	Removing exceptions by updating ALL the wrappers
					if mode == "usufy":
						try:
							if plat.url:
								listSelected.append(plat)
								added = True
								break
						except:
							# if the hasUsufy parameter was NOT found, we assume that it is because it is an old wrapper
							#	All of them have implemented Usufy
							listSelected.append(plat)
							added = True
							break
					elif mode == "user-collector":
	
						try:
							if plat.urlEnumeration:
								listSelected.append(plat)
								added = True
								break
						except:
							# if the hasUsufy parameter was NOT found, we assume that it is because it is an old wrapper
							#	This platform has not implemented yet the enumeration.				
							pass
			if not added:
				for t in plat.tags:
					if t in tags:
						# [TO-DO]
						#	Removing exceptions by updating ALL the wrappers
						if mode == "usufy":
							try:
								if plat.url:
									listSelected.append(plat)
									added = True
									break
							except:
								# if the hasUsufy parameter was NOT found, we assume that it is because it is an old wrapper
								#	All of them have implemented Usufy
								listSelected.append(plat)
								added = True
								break
						elif mode == "user-collector":
							try:
								if plat.urlEnumeration:
									listSelected.append(plat)
									added = True
									break
							except:
								# if the hasUsufy parameter was NOT found, we assume that it is because it is an old wrapper
								#	This platform has not implemented yet the enumeration.				
								pass
		if len(listSelected) > 0:
			return listSelected
		else:
			return []

def getCredentials(filename=os.path.dirname(os.path.abspath(__file__))+"/creds.txt"):
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
			logger.info(str(len(contenido)) + " credentials have been loaded.")	
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
