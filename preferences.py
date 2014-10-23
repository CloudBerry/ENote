# (C) 2014 Espen Meidell
# espen.meidell@gmail.com
# All rights reserved

from gi.repository import Gtk, Pango


class Preferences(Gtk.Window):
	
	dark_theme = False
	font_size = 11
	
	
	def __init__(self):
		"""
		Constructor for preference window
		"""
		Gtk.Window.__init__(self, title="ENote Preferences")
		self.connect("delete-event", Gtk.main_quit)
		self.set_border_width(25)
		
		self.headerbar = Gtk.HeaderBar()
		self.headerbar.set_show_close_button(True)
		self.headerbar.props.title = "ENote Preferences"
		self.set_titlebar(self.headerbar)
		
		self.mainBox = Gtk.VBox()
		
		self.prefgrid = Gtk.Grid()
		self.prefgrid.set_column_spacing(10)
		self.prefgrid.set_row_spacing(10)
		self.prefgrid.set_column_homogeneous(True)
		
		
		#Theme menu
		self.themelabel = Gtk.Label("Dark Theme:")
		self.themelabel.set_alignment(0, 0.5)
		switchbox = Gtk.Box()
		self.themeswitch = Gtk.Switch()
		switchbox.add(self.themeswitch)
		self.prefgrid.attach(self.themelabel, 0, 0, 1, 1)
		self.prefgrid.attach(switchbox, 1, 0, 1, 1)
		
		#Font size
		
		#~ pangoFont = Pango.FontDescription("11")
		#~ self.themelabel.modify_font(pangoFont)
		
		self.fontlabel = Gtk.Label("Editor Font Size:")
		self.fontlabel.set_alignment(0, 0.5)
		self.fontspin = Gtk.SpinButton()
		adjustment = Gtk.Adjustment(10, 5, 40, 1, 10, 0)
		self.fontspin.set_adjustment(adjustment)
		self.fontspin.update()
		self.fontspin.set_value(11)

		self.prefgrid.attach(self.fontlabel, 0, 1, 1, 1)
		self.prefgrid.attach(self.fontspin, 1, 1, 1, 1)		
		
		#Info and License
		self.aboutbtn = Gtk.Button(label="About")
		self.licensebtn = Gtk.Button(label="License")
		self.aboutbtn.connect("clicked", self.buttonEvent)
		self.licensebtn.connect("clicked", self.buttonEvent)
		
		self.prefgrid.attach(self.aboutbtn, 0, 2, 1, 1)
		self.prefgrid.attach(self.licensebtn, 1, 2, 1, 1)
		
		#OK button
		self.okbtn = Gtk.Button(label="Apply")
		self.okbtn.connect("clicked", self.buttonEvent)
		
		self.prefgrid.attach(self.okbtn, 1, 3, 1, 1)

		self.mainBox.add(self.prefgrid)
		
		self.add(self.mainBox)
		
	def buttonEvent(self, widget):
		pass


def run():
	pref = Preferences()
	pref.show_all()
	pref.move(700, 300)
	Gtk.main()


run()
