#!/usr/bin/env python

# example helloworld2.py

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld2:
    def callback(self, widget, data):
        print "Hello again %s" %data

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Hello Buttons!")

        self.window.connect("delete_event", self.delete_event)

        self.window.set_border_width(10)

        # box for holding widgets
        # TING: (seems like composite pattern is at work)
        self.box1 = gtk.HBox(homogeneous=False, spacing=0) # HorizontalBox
        self.window.add(self.box1)

        # button 1
        self.button1 = gtk.Button("Button 1")
        self.button1.connect("clicked", self.callback, "button 1") # button1 is the para passed

        # pack button1 to box1 at the start
        # complementary method is pack end
        self.box1.pack_start(child=self.button1, expand=True, fill=True, padding=0)
        # show button 1
        self.button1.show()

        # button 2
        self.button2=gtk.Button("Button 2")
        self.button2.connect("clicked", self.callback, "button 2")

        # pack button2 to box1
        self.box1.pack_start(child=self.button2, spacing=True, fill=True, padding=0)

        # show button2
        self.button2.show()

        # the order in which we show the buttons is not that important
        # though we should show window at the last
        self.box1.show()
        self.window.show()

def main():
    gtk.main()

if __name__ == "__main__":
    hello = HelloWorld2()
    main()

