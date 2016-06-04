#!/usr/bin/env python3
"""
Author: Vatsal Parekh

"""
import sys

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Calc(Gtk.Window):
    """Calc - main class where all the logic is

    """
    def __init__(self):
        Gtk.Window.__init__(self, title="PyGO Calc")

        # Box layout
        box = Gtk.Box.new(Gtk.Orientation.VERTICAL, spacing=15)
        box.set_homogeneous(False)

        # Label where the equation will be see
        # and answer will be displayed
        self.display = Gtk.Label()
        self.display.set_justify(Gtk.Justification.RIGHT)
        box.pack_start(self.display, True, True, 10)

        # Grid layout where all the buttons will reside
        grid= Gtk.Grid()
        box.pack_start(grid, True, True, 10)

        # All the buttons and the function that will be fired
        # on their clicks
        btn1 = Gtk.Button(label="1")
        btn1.connect("clicked", self.btn1_clicked)
        btn2 = Gtk.Button(label="2")
        btn2.connect("clicked", self.btn2_clicked)
        btn3 = Gtk.Button(label="3")
        btn3.connect("clicked", self.btn3_clicked)
        btn4 = Gtk.Button(label="4")
        btn4.connect("clicked", self.btn4_clicked)
        btn5 = Gtk.Button(label="5")
        btn5.connect("clicked", self.btn5_clicked)
        btn6 = Gtk.Button(label="6")
        btn6.connect("clicked", self.btn6_clicked)
        btn7 = Gtk.Button(label="7")
        btn7.connect("clicked", self.btn7_clicked)
        btn8 = Gtk.Button(label="8")
        btn8.connect("clicked", self.btn8_clicked)
        btn9 = Gtk.Button(label="9")
        btn9.connect("clicked", self.btn9_clicked)
        btn0 = Gtk.Button(label="0")
        btn0.connect("clicked", self.btn0_clicked)
        btnplus = Gtk.Button(label="+")
        btnplus.connect("clicked", self.btn_add)
        btnminus = Gtk.Button(label="-")
        btnminus.connect("clicked", self.btn_subtract)
        btnmul = Gtk.Button(label="*")
        btnmul.connect("clicked", self.btn_multiply)
        btndiv = Gtk.Button(label="/")
        btndiv.connect("clicked", self.btn_divide)
        btnequal = Gtk.Button(label="=")
        btnequal.connect("clicked",self.btn_equal)
        btncls = Gtk.Button(label="cls")
        btncls.connect("clicked", self.btn_cls)

        grid.add(btn1)
        grid.attach_next_to(btn2, btn1, 1, 1, 1)
        grid.attach_next_to(btn3, btn2, 1, 1, 1)
        grid.attach_next_to(btnplus, btn3, 1, 1, 1)
        grid.attach_next_to(btn4, btn1, 3, 1, 1)
        grid.attach_next_to(btn5, btn4, 1, 1, 1)
        grid.attach_next_to(btn6, btn5, 1, 1, 1)
        grid.attach_next_to(btnminus, btn6, 1, 1, 1)
        grid.attach_next_to(btn7, btn4, 3, 1, 1)
        grid.attach_next_to(btn8, btn7, 1, 1, 1)
        grid.attach_next_to(btn9, btn8, 1, 1, 1)
        grid.attach_next_to(btnmul, btn9, 1, 1, 1)
        grid.attach_next_to(btn0, btn7, 3, 1, 1)
        grid.attach_next_to(btncls, btn0, 1, 1, 1)
        grid.attach_next_to(btnequal, btncls, 1, 1, 1)
        grid.attach_next_to(btndiv, btnequal, 1, 1, 1)

        self.add(box)

    def btn_equal(self, widget):
        try:
            self.display.set_label(str(eval(self.display.get_label())))
        except SyntaxError:
            self.display.set_label("")


    def btn_add(self, widget):
        self.display.set_label(self.display.get_label()+"+")

    def btn_subtract(self, widget):
        self.display.set_label(self.display.get_label()+"-")

    def btn_multiply(self, widget):
        self.display.set_label(self.display.get_label()+"*")

    def btn_divide(self, widget):
        self.display.set_label(self.display.get_label()+"/")

    def btn_cls(self, widget):
        self.display.set_label("")


    def btn1_clicked(self, widget):
        self.display.set_label(self.display.get_label()+"1")

    def btn2_clicked(self, widget):
        self.display.set_label(self.display.get_label()+"2")

    def btn3_clicked(self, widget):
        self.display.set_label(self.display.get_label()+"3")

    def btn4_clicked(self, widget):
        self.display.set_label(self.display.get_label()+"4")

    def btn5_clicked(self, widget):
        self.display.set_label(self.display.get_label()+"5")

    def btn6_clicked(self, widget):
        self.display.set_label(self.display.get_label()+"6")

    def btn7_clicked(self, widget):
        self.display.set_label(self.display.get_label()+"7")

    def btn8_clicked(self, widget):
        self.display.set_label(self.display.get_label()+"8")

    def btn9_clicked(self, widget):
        self.display.set_label(self.display.get_label()+"9")

    def btn0_clicked(self, widget):
        self.display.set_label(self.display.get_label()+"0")

if __name__ == "__main__":
    try:
        win = Calc()
        win.connect("delete-event", Gtk.main_quit)
        win.show_all()
        Gtk.main()
    except Exception as e:
        print(e)
        sys.exit()
