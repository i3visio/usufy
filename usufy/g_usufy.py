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

# required imports
from Tkinter import *
from ttk import *
import tkFileDialog
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
import tkMessageBox as box

from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

import utils.usufyparser as usufyparser
import usufy as usufy
# logging imports
import logging


class UsufyGUI(Tk):
	""" 
		Class that will contain the details of the GUI
	"""

	def __init__(self, parent=0):
		""" 
			Recovering an instance of a new Tkinter window.
		"""
		
		self.root = Tk()
		self.root.title("usufy.py - GUI")

		# calling the _menubar private function
		menubar = self._getMenubar()
		# display the menu
		self.root.config(menu=menubar)

		# load notes
		self.note = Notebook(self.root)

		# load searchWindow
		self.tabSearch = Frame(self.note)
		self._packSearchWindow ()

		# load tabResultsWindow
		self.tabResults = Frame(self.note)
		self.data= {}
		self._drawTable()

		# add notes
		self.note.add(self.tabSearch, text = "Search", compound=TOP)
		self.note.add(self.tabResults, text = "Results")

		self.note.pack()

		self.root.mainloop()

	def _onInfo(self):
		""" 
			Defining the window for the About window.
		"""
		box.showinfo("usufy.py - F. Brezo and Y. Rubio (i3visio)", "This program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it under certain conditions.\nFor further info, visit: usufy.com")

	def _hello(self):
		""" 
			Test function for testing
		"""
		print "hello!"

	def _drawTable(self):
		""" 
			Loading table
		"""
		self.tframe = Frame(self.tabResults)
		self.tframe.pack()
		self.table = TableCanvas(self.tframe)
		self.table.createTableFrame()
	
		#self.table.importTable()

		model = TableModel() 
		#self.data = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'}, 'rec2': {'col1': 99.88, 'col2': 108.79, 'label': 'rec2'}}

		model.importDict(self.data) 
		self.table.updateModel(model) 
		self.table.redrawTable()

	def _saveProfile(self):
		""" 
			Save the profile to a file.
		"""
		self.table.save()

	def _openProfile(self):
		""" 
			Load the profile from a file.
		"""
		self.table.load()

	def _getMenubar(self):
		""" 
			Coding the menu options
		"""
		menubar = Menu(self.root)
		# Import Menu
		openFiles = Menu(menubar, tearoff=0)
		openFiles.add_command(label="CSV", command=self._importDataCSV)
		openFiles.add_command(label="Json", command=self._importDataJson)

		# create a pulldown menu, and add it to the menu bar
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="New window...", command=self._newWindow)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.root.quit)
		menubar.add_cascade(label="File", menu=filemenu)


		analysermenu = Menu(menubar, tearoff=0)
		analysermenu.add_command(label="Open profile...", command=self._openProfile)
		analysermenu.add_command(label="Save profile", command=self._saveProfile)
		analysermenu.add_separator()
		analysermenu.add_cascade(label="Import Usufy results", menu=openFiles)
		menubar.add_cascade(label="Analyser", menu=analysermenu)

		# create more pulldown menus
		#viewmenu = Menu(menubar, tearoff=0)
		#viewmenu.add_command(label="Search", command=self._hello)
		#viewmenu.add_command(label="Results", command=self._hello)
		#menubar.add_cascade(label="View", menu=viewmenu)

		helpmenu = Menu(menubar, tearoff=0)
		#helpmenu.add_command(label="Documentation", command=self._hello)
		#helpmenu.add_separator()
		helpmenu.add_command(label="About", command=self._onInfo)
		menubar.add_cascade(label="Help", menu=helpmenu)

		return menubar

	def _packSearchWindow(self):
		""" 
			Loading the search.
		"""
		self.searchGroup = LabelFrame(self.tabSearch, text="New search options...")
		self.searchGroup.pack(padx=10, pady=10)

		self.tabSearchLabInstructions = Label(self.searchGroup, text="Write down the query as if you were in the console:")
		self.tabSearchLabInstructions.pack()

		# Group for the command
		self.code = Frame(self.searchGroup)
		self.code.pack(fill="both", expand=True)
		# Label for the code
		self.tabSearchLabPython = Label(self.code, text="python usufy.py ")
		self.tabSearchLabPython.pack( side = LEFT, fill="both", expand=True)
		# bd is for the width of the text
		self.tabSearchEntPython = Entry(self.code)
		self.tabSearchEntPython.pack(side = RIGHT)

		# button
		self.tabSearchButSearch = Button (self.searchGroup, text="Launch usufy.py", command=self._launchUsufy)
		self.tabSearchButSearch.pack(side = BOTTOM)

		# Output command
		self.terminalOutput = LabelFrame(self.tabSearch, text="Terminal Output")
		self.terminalOutput.pack(padx=40, pady=40)

		# defining the output on root
		self.usufyText = Text(self.terminalOutput, wrap="word")
		self.usufyText.pack(side="top", fill="both", expand=True)
		self.usufyText.tag_configure("stderr", foreground="#b22222")

		# UNCOMMENT IF THE PROBLE WITH FLUSHING IS SOLVED
		#sys.stdout = TextRedirector(self.usufyText, "stdout")
		#sys.stderr = TextRedirector(self.usufyText, "stderr")

		#label = Message( self.terminalOutput, textvariable=self.usufyText, relief=RAISED )

		#self.usufyText.insert(END,"Hey!? How are you doing?")

	def _importDataJson(self):
		""" 
			Import data from a json file.

			TO-DO
		"""
		ftypes = [('Json', '*.json'), ('All files', '*')]
		filename = askopenfilename(filetypes = ftypes)

		f = open(filename)
		text = f.read()
		self.usufyText.insert(END, text)
		f.close()

		
		pass

	def _importDataCSV(self):
		""" 
			Import data from a CSV
		"""
		ftypes = [('CSV', '*.csv'), ('All files', '*')]
		filename = askopenfilename(filetypes = ftypes)
		
		f = open(filename)
		text = f.read()
		self.usufyText.insert(END, text)
		f.close()

		#self.table.importTable()

		# Model...
		model = TableModel() 
		def getNewIndex():	
			max = 0
			for i in self.data:
				if i > max:
					max=i
			return  max+1

		lines = text.splitlines()
		attrib = lines[0].split('\t')
		for l in range(1, len(lines)):
			elements = lines[l].split('\t')
			aux = {}
			for i, at in enumerate(attrib):
				aux[at] = elements[i]
			self.data[getNewIndex()] = aux

		model.importDict(self.data) 
		self.table.updateModel(model) 
		self.table.redrawTable()

	def _launchUsufy(self):
		""" 
			Launching Usufy
		"""
		arguments = self.tabSearchEntPython.get()
		#print arguments
	
		# get Parser
		parser = usufyparser.getParser()
		
		# split arguments
		args = parser.parse_args(arguments.split())
		# Calling the main function
		res = usufy.usufy_main(args)
		for r in res:
			self.usufyText.insert("end", r)


	def _newWindow(self):
		""" 
			Opening a new Usufy window
		"""
		arguments = "--gui"	
		# get Parser
		parser = usufyparser.getParser()
		
		# split arguments
		args = parser.parse_args(arguments.split())
		# Calling the main function
		res = usufy.usufy_main(args)

class TextRedirector(object):
	def __init__(self, widget, tag="stdout"):
		self.widget = widget
		self.tag = tag

	def write(self, str):
		self.widget.configure(state="normal")
		self.widget.insert("end", str, (self.tag,))
		self.widget.configure(state="disabled")


if __name__ == "__main__":
	window = UsufyGUI()
