#!/usr/bin/env python3
"""
Copyright (c) 2016, Vatsal Parekh

All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import subprocess

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
    def help_about(self, button):
        about.set_transient_for(win)
        about.run()
        about.hide()

    def on_fortunebtn_clicked(self, button):
        process = subprocess.Popen("fortune", stdout=subprocess.PIPE)
        out = process.stdout.read()
        buffer.set_text(out.decode("utf-8"))
        win.resize(400, 100)


if __name__ == "__main__":
    builder = Gtk.Builder()
    builder.add_from_file("fortune.glade")
    builder.connect_signals(Handler())
    win = builder.get_object("Window")
    about = builder.get_object("about")
    txt = builder.get_object("text")
    buffer = txt.get_buffer()
    win.connect("delete_event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
