#from distutils.core import setup
import os

# Ensuring that Setuptools is install
import ez_setup
ez_setup.use_setuptools()

# Depending on the place in which the project is going to be upgraded
from setuptools import setup
try:
	from pypandoc import convert
	read_md = lambda f: convert(f, 'rst')
except ImportError:
	print("warning: pypandoc module not found, could not convert Markdown to RST")
	read_md = lambda f: open(f, 'r').read()

setup(	name="usufy",
	version="v2.0.1",
	description="usufy - Piece of software to check the existence of a given profile in different platforms developed by i3visio.",
	author="Felix Brezo and Yaiza Rubio",
	author_email="contacto@i3visio.com",
	url="http://github.com/i3visio/usufy",
	license="COPYING",
	packages=["usufy", "usufy.lib"],
#	scripts=["bin/_template.py", "bin/classgenerator.py"],
	long_description=read_md("README.md"),
#	long_description=open('README.md').read(),
	install_requires=[
 	"i3visiotools >= 0.2.2",
	"tkintertable",
	"Pmw",
	"entify >= 0.4.0",
#	"pypandoc",
	],
)

