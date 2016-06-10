#!/usr/bin/env python3
import codecs

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango


class TextEditor(Gtk.Window):
    """TextEditor
        The main class where all the handling and logic reside.
    """
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("simpletexteditor.glade")
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("window")
        self.textview = self.builder.get_object("textview")
        self.textbuffer = self.builder.get_object("textbuffer")
        self.about = self.builder.get_object("about_page")
        self.fileopen = self.builder.get_object("fileopen")
        self.filesave = self.builder.get_object("filesave")
        self.fontchooser = self.builder.get_object("fontchooser")
        # notsave is msgdialog for asking
        # if user wants to save current textbuffer
        self.notsave = self.builder.get_object("notsave")
        self.notsavetwo = self.builder.get_object("notsavetwo")

        self.currentfile = ""
        self.filechanged = False
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

    def file_new(self, button):
        if (not self.currentfile) and (not self.filechanged):
            self.textbuffer.set_text("")
        else:
            self.notsave.set_transient_for(self.window)
            self.response = self.notsave.run()

            if self.response == Gtk.ResponseType.YES:
                self.save(self.filesave)
                self.textbuffer.set_text()
                self.notsave.hide()
            else:
                self.textbuffer.set_text("")
                self.currentfile = ""
                self.filechanged = False
                self.notsave.hide()

    def file_open(self, button):
        if self.filechanged:
            self.notsavetwo.set_transient_for(self.window)
            self.response = self.notsavetwo.run()

            if self.response == Gtk.ResponseType.YES:
                self.save(self.filesave)

            self.notsavetwo.hide()


        self.fileopen.set_transient_for(self.window)
        self.response = self.fileopen.run()

        if self.response == Gtk.ResponseType.OK:
            self.file_to_open = self.fileopen.get_filename()
            if self.file_to_open:
                self.currentfile = self.file_to_open
                with codecs.open(self.file_to_open,
                                 'r',
                                 encoding="utf-8") as f:
                    self.content_file = f.read()
                    self.textbuffer.set_text(self.content_file)

        self.fileopen.hide()

    def save(self, button):
        if self.currentfile:
            with codecs.open(self.currentfile,
                             'w',
                             encoding="utf-8") as f:
                f.write(self.textbuffer.get_text(
                    self.textbuffer.get_start_iter(),
                    self.textbuffer.get_end_iter(),
                    False
                ))
            self.filechanged = False
        else:
            self.save_as(self.filesave) # ayy imao


    def save_as(self, button):
        self.filesave.set_transient_for(self.window)
        self.response = self.filesave.run()

        if self.response == Gtk.ResponseType.OK:
            self.file_to_save = self.filesave.get_filename()
            if self.file_to_save:
                self.currentfile = self.file_to_save
                with codecs.open(self.file_to_save,
                                 'w',
                                 encoding="utf-8") as f:
                    f.write(self.textbuffer.get_text(
                        self.textbuffer.get_start_iter(),
                        self.textbuffer.get_end_iter(),
                        False
                    ))
        self.filechanged = False
        self.filesave.hide()


    def gtk_main_quit(self, button):
         Gtk.main_quit()

    def cut(self, button):
         self.textbuffer.cut_clipboard(self.clipboard, True)

    def copy(self, button): 
        self.textbuffer.copy_clipboard(self.clipboard)

    def paste(self,button):
        self.textbuffer.paste_clipboard(self.clipboard, None, True)

    def font_choose(self, button):
        self.fontchooser.set_transient_for(self.window)
        self.response = self.fontchooser.run()

        if self.response == Gtk.ResponseType.OK:
            self.font = Pango.font_description_from_string(
                self.fontchooser.get_font()
            )
            self.textview.override_font(self.font)

        self.fontchooser.hide()

    def about_page(self, button):
        self.about.set_transient_for(self.window)
        self.about.run()
        self.about.hide()

    def on_textbuffer_changed(self, buf):
        self.filechanged = True

if __name__ == '__main__':
    win = TextEditor()
    win.window.connect("delete_event", Gtk.main_quit)
    win.window.show_all()
    Gtk.main()
