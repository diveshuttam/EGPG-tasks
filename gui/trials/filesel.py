#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class FileSelectionExample:
    # Get the selected filename and print it to the console
    def file_ok_sel(self, w):
        print("%s" % self.filew.get_filename())

    def destroy(self, widget):
        gtk.main_quit()

    def __init__(self):
        self.filew = gtk.FileSelection("File selection")
        self.filew.connect("destroy", self.destroy)
        #Connect the ok_button to file_ok_sel method
        self.filew.ok_button.connect("clicked", self.file_ok_sel)
        # Connect the cancel_button to destroy
        self.filew.cancel_button.connect_object("clicked", gtk.Widget.destroy, self.filew)
        self.filew.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    FileSelectionExample()
    main()
