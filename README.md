	============================================================
	usufy.py  Copyright (C) 2014  F. Brezo and Y. Rubio, i3visio
	============================================================

Description:
============
usufy.py is a GPLv3 piece of software that checks the existence of a profile for a given 
user in a bunch of different platforms using the error messages displayed by most 
platforms when a user profile has not been found as the evidence of the existence or not 
of a given profile. Its inheritance system has been designed to allow an easy development 
of new wrappers while its multiprocessing conception shows the results fastly.

The supported networks in v1.3.0b by 2014-07-26 are:
adtriboo, badoo, bitbucket, bitcointalk, blip, burbuja, 
care2, couchsurfing, dailymotion, delicious, douban, 
ebay, elmundo, epinions, facebook, favstar, flickr, 
forobtc, forocoches, fotolog, foursquare, freebase,
garage4hackers, getsatisfaction, github, gitorious,
googleplus, gsmspain, hellboundhackers, hi5, identica,
instagram, issuu, karmacracy, kickstarter, klout,
linkedin, marca, mediavida, myspace, occupywallst,
pastebin, pearltrees, pinterest, pokerstrategy, qq,
ratemypoo, rebelmouse, reddit, researchgate, scribd,
slideshare, sourceforge, storify, spoj, theguardian,
tradimo, tumblr, twicsy, twitpic, twitter, unsystem,
vk, xing, youtube

License: GPLv3
==============

This is free software, and you are welcome to redistribute it under certain conditions.

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.


For more details on this issue, run:
```
	python usufy.py --license
```

Installation:
=============
The installation under Python 2.7 for the release package Usufy-v1.x.x is as follows:
```
tar xvfz Usufy-v1.x.x.tar.gz
sudo python setup.py install
```
or
```
unzip Usufy-v1.x.x.zip
sudo python setup.py install
```
Supeuser privileges are required so as to complete the installation. Afterwards, 
the module will be importable from any python code. You can check this by typing:
```
python -c "import usufy"
```
If no error is displayed, the installation would have been performed correctly.

Usage:
======
So as to run the program, navigate to Usufy-v1.x.x/usufy and run:
```
python usage.py -h
```
The usage is described as follows:
```
usage: usufy.py
                (--info <action> | -l <path_to_nick_list> | -n <nick> [<nick> ...])
                [-p <platform> [<platform> ...]] [-t <tag> [<tag> ...]] [-a]
                [-e <sum_ext> [<sum_ext> ...]] [-o <path_to_output_folder>]
                [-v <verbosity>] [-h] [--license] [--version]
```

The functionalities are described as follows:
```
Input options (one required):
  There are two different ways of receiving the nicks in usufy.py:

  --info <action>       select the action to be performed amongst the
                        following: list_platforms (list the details of the 
                        selected platforms) or list_tags (list the tags of 
                        the selected platforms).
  -l <path_to_nick_list>, --list <path_to_nick_list>
                        path to the file where the list of nicks to verify is
                        stored (one per line).
  -n <nick> [<nick> ...], --nicks <nick> [<nick> ...]
                        the list of nicks to process (at least one is
                        required).

Platform selection arguments:
  Criteria for selecting the platforms where performing the search.

  -p <platform> [<platform> ...], --platforms <platform> [<platform> ...]
                        select the platforms where you want to perform the
                        search amongst the following: all, badoo, blip, delicious,
                        ebay, facebook, foursquare, googleplus, karmacracy, klout, 
						myspace,pastebin, pinterest, slideshare, twitter, vk, 
						youtube. More than one option can be selected.
  -t <tag> [<tag> ...], --tags <tag> [<tag> ...]
                        select the list of tags that fit the platforms in
                        which you want to perform the search. More than one
                        option can be selected.

Processing arguments:
  Configuring the way in which usufy will process the identified profiles.

  -a, --avoid_processing
                        argument to force usufy NOT to process the downloaded
                        valid profiles.
  -e <sum_ext> [<sum_ext> ...], --extension <sum_ext> [<sum_ext> ...]
                        output extension for the summary file (at least, one 
						required). Currently supported: csv, json.
  -o <path_to_output_folder>, --output_folder <path_to_output_folder>
                        output folder for the generated documents. While if
                        the paths does not exist, usufy.py will try to create;
                        if this argument is not provided, usufy will NOT write
                        any down any data. Check permissions if something goes
                        wrong.

About arguments:
  Showing additional information about this program.

  -h, --help            shows the version of the program and exists.
  --license             shows the GPLv3 license.
  --version             shows the version of the program and exists.
```

Examples:
=========
The capabilities of the tool can be divided as informative, basic searches and processing.

Informative:
------------
These commands can be used to gather information about the state of the application.
- Checking some details of all the platforms to be processed:
```
	python usufy.py --info list_platforms
```
- Checking some details of the platforms labelled as 'social' and 'contact':
```
	python usufy.py -p social contact --info list_platforms
```
- Checking the number of platforms categorised under each and every tag:
```
	python usufy.py --info list_tags
```
To gather additional information about the tool, you may type:
- Checking the help of the application:
```
	python usufy.py -h
```
It may be recommended to be run as to read it step by step:
```
	python usufy.py -h | less
```
- Checking the current version of the application:
```
	python usufy.py --version
```
- Checking the terms of the license:
```
	python usufy.py --license
```
Again, it may be recommended to be run as to read it step by step:
```
	python usufy.py --license | less
```

Basic Searches:
---------------
The basic searches will only print the results in the terminal. Here are some examples:
- Checking if the user 'example' exist in all the platforms ('-p all' is not needed):
```
	python usufy.py -n example
```
We can also use the long version of the commands. In this case, the long version of '-n'
is '--nick'. Check the section before for further details.
```
	python usufy.py --nick example
```
- Checking if the users 'example1' and 'example2' exist in all the platforms ('-p all' is 
not needed):
```
	python usufy.py -n example1 example2
```
- Checking if the users 'example1' and 'example2' exist ONLY in Facebook and Twitter:
```
	python usufy.py -n example1 example2 - p facebook twitter
```
- Checking if the users existing in 'test.txt' exist in the Platforms tagged as 'social':
```
	python usufy.py -l test.txt -t social
```

Additional processing:
----------------------
Apart from the console output, usufy.py is capable of generating additional resources:
- Checking if the user 'example' exist in all the platforms and storing the information of 
the successfully found profiles in a folder called './results' (this will create the folder if 
it does not exist):
```
	python usufy.py -n example -o ./results
```
This option will download the information of the profiles as well as creating a .csv file by 
default with the profiles found. This .csv file can be changed for a Json file:
```
	python usufy.py -n example -o ./results -e json
```
- Checking if the users listed in a 'test.txt' file exist in all the platforms WITHOUT stotring  
the successfully found profiles but keeping the results in a Json file:
```
	python usufy.py -n example -o ./results -e json --avoid_processing
```

