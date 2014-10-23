# (C) 2014 Espen Meidell
# espen.meidell@gmail.com
# All rights reserved
from gi.repository import Gtk, Pango
from IO import readFile, writeFile, readPreferences
import preferences

class ENote(Gtk.Window):
	
	def __init__(self):
		"""
		Constructor for ENote main window
		"""
		Gtk.Window.__init__(self, title="E-Note")
		self.connect("delete-event", self.close)
		self.set_default_size(600,400)
		self.set_border_width(1)
		self.fscreen = False
		self.preferences = readPreferences()
		
		settings = Gtk.Settings.get_default()
		if self.preferences[0]:
			settings.set_property("gtk-application-prefer-dark-theme", True)
		
		self.names = []		#different page names
		self.editors = []		#to store editors
		
		#Header bar
		self.headerBar = Gtk.HeaderBar()
		self.headerBar.set_show_close_button(True)
		self.headerBar.props.title = "ENote 1.0"
		#Buttons to header bar
		self.btnbox = Gtk.Box()
		self.addbtn = Gtk.ToolButton.new_from_stock(Gtk.STOCK_ADD)
		self.addbtn.connect("clicked", self.buttonEvent)
		self.delbtn = Gtk.ToolButton.new_from_stock(Gtk.STOCK_DELETE)
		self.delbtn.connect("clicked", self.buttonEvent)
		self.prefbtn = Gtk.ToolButton.new_from_stock(Gtk.STOCK_PREFERENCES)
		self.prefbtn.connect("clicked", self.buttonEvent)
		self.btnbox.add(self.addbtn)
		self.btnbox.add(self.delbtn)
		self.btnbox.add(self.prefbtn)
		self.headerBar.pack_start(self.btnbox)
		self.addbtn.set_tooltip_text("Add Page")
		self.delbtn.set_tooltip_text("Delete Page")
		self.prefbtn.set_tooltip_text("Preferences")
		
		self.set_titlebar(self.headerBar)
		
		self.ntb = Gtk.Notebook()
		self.ntb.set_show_tabs(True)
		self.ntb.set_tab_pos(0)
		
		
		self.connect("key-press-event", self.keyEvent)
		self.createNoteBookTabs()
		self.add(self.ntb)
		
		
	def createNoteBookTabs(self):
		"""
		This method creates the pages for the notebook when the
		application is launched
		"""
		pages = readFile()
		for page in pages:
			scroll = Gtk.ScrolledWindow()
			editor = Gtk.TextView()		#editor
			editor.set_border_width(15)
			pangoFont = Pango.FontDescription(str(self.preferences[1]))	#font from preference
			editor.modify_font(pangoFont)
			editor.get_buffer().set_text(page[1])
			label = Gtk.Label("<b><big>"+page[0]+"</big></b>")	#label
			label.set_alignment(0, 0.5)
			label.set_use_markup(True)
			scroll.add(editor)
			self.ntb.append_page(scroll, label)
			self.editors.append(editor)
			self.names.append(page[0])
		
	def addNewPage(self):
		"""
		This method adds a new page to the workbook
		"""
		entry = Gtk.Entry()
		entry.set_text("")
		dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK_CANCEL, "Name of new page:")
		dialog.set_markup("<b><big>Add a new page</big></b>")
		dialog.format_secondary_text("Please enter new page name below:") 
		dialog.vbox.pack_end(entry, True, True, 0)
		dialog.show_all()
		response  = dialog.run()
		if response == Gtk.ResponseType.OK:
			#New page to GUI
			scroll = Gtk.ScrolledWindow()
			editor = Gtk.TextView()		#editor
			editor.set_border_width(15)
			pangoFont = Pango.FontDescription(str(self.preferences[1]))	#font from preference
			editor.modify_font(pangoFont)
			label = Gtk.Label("<b><big>"+entry.get_text()+"</big></b>")	#label
			label.set_alignment(0, 0.5)
			label.set_use_markup(True)
			scroll.add(editor)
			self.ntb.append_page(scroll, label)
			self.editors.append(editor)
			self.names.append(entry.get_text())
			
		
		dialog.destroy()
		
	def deletePage(self):
		"""
		This method deletes the currently selected notebook
		"""
		dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, "Are you sure you want to delete?")
		dialog.format_secondary_text("This action is irreversible")
		response = dialog.run()
		if response == Gtk.ResponseType.YES:
			i = self.ntb.get_current_page()
			self.editors.pop(i)
			self.names.pop(i)
			self.ntb.remove_page(i)
			
		dialog.destroy()
		
	def buttonEvent(self, widget):
		"""
		This method handles click-events from buttons
		@param widget: The button that has been clicked
		"""
		if widget == self.addbtn:
			self.addNewPage()
		elif widget == self.delbtn:
			self.deletePage()
		elif widget == self.prefbtn:
			preferences.run()
		self.show_all()
		
	def keyEvent(self, widget, event):
		"""
		Handles keyboard events
		"""
		if event.keyval == 65480 and not self.fscreen:
			self.fullscreen()
			self.fscreen = True
		elif event.keyval == 65480 and self.fscreen:
			self.unfullscreen()
			self.fscreen = False
	
		
	def close(self, a,b):
		"""
		This method handles the delete-event for main window
		Upon delete-event all data is saved and window is closed
		"""
		bodies = []
		for editor in self.editors:
			bf = editor.get_buffer()
			text = bf.get_text(bf.get_start_iter(),bf.get_end_iter(), True)
			bodies.append(text)
		writeFile(self.names, bodies)
		Gtk.main_quit()
		
		


win = ENote()
win.show_all()
Gtk.main()

