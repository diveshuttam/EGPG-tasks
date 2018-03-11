#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk


class HelloWorld:
    def hello(self, widget, data=None):
        print("Hello, World")

    def delete_event(self, widget, data=None):
        print("delete event occured")
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # delete is generated on clicking close button,
        # destroy is generated when delete returns false.
        # we can also destroy by calling gtk_widget_destroy()
        # TING : seems like observer pattern is at work here
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)

        self.window.set_border_width(10)

        # button
        self.button = gtk.Button("Hello World")
        # functions are invoked in order they are connected
        self.button.connect("clicked", self.hello, None) #None is the parameter to hello
        # below, connect object connects gtk.Widget.destroy function with self.button
        # but when invoking it, it invokes the function with window as parameter
        # instead of the current button which is the case in connect above
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

        # attach button and show
        self.window.add(self.button)
        self.button.show()
        self.window.show()

    def main(self):
        gtk.main()


if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()
