#!/usr/bin/env python

import pygtk
import gtk
# import sys
# import argparse

pygtk.require('2.0')

DEBUG = True # later set this using command line arguments

class FileSelector:
    def file_ok_handler(self, widget):
        self.selected_file = self.file_widget.get_filename()
        if(DEBUG):
            print(self.selected_file)

    def destroy(self, widget):
        if(DEBUG):
            print("Selected file is %s" % self.selected_file)
        gtk.main_quit()

    def __init__(self):
        # this variable contains the selected file initilaizing to None
        self.selected_file = None

        # creating a file selction widget.
        self.file_widget = gtk.FileSelection("Select a file")

        # connecting widgets destroy's to destroy
        self.file_widget.connect("destroy", self.destroy)

        # ok_button
        # connect the file_ok_handler function to ok_button click
        self.file_widget.ok_button.connect("clicked", self.file_ok_handler)
        # connect destroy to ok_button next i.e exit after selecting file
        self.file_widget.ok_button.connect_object("clicked",
                                                  gtk.Widget.destroy,
                                                  self.file_widget)

        # cancel_button
        # connect destroy to cancel_button click
        self.file_widget.cancel_button.connect_object("clicked",
                                                      gtk.Widget.destroy,
                                                      self.file_widget)
        # show the file selector
        self.file_widget.show()

def main():
    filesel = FileSelector()
    gtk.main()
    print(filesel.selected_file)


if __name__ == "__main__":
    main()
