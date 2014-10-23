# (C) 2014 Espen Meidell
# espen.meidell@gmail.com
# All rights reserved

from gi.repository import Gtk


class Preferences(Gtk.Window):
	
	def __init__(self):
		"""
		Constructor for preference window
		"""
		Gtk.Window.__init__(self, title="ENote Preferences")
		
		


def run():
	pref = Preferences()
	pref.show_all()
	Gtk.main()
