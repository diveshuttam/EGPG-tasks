#!/usr/bin/env python

import pygtk
import gtk
import os
import time
import argparse

pygtk.require('2.0')

DEBUG = False  # setting this using command line arguments


class FileSelector:
    def file_ok_handler(self, widget):
        self.selected_file = self.file_widget.get_filename()
        if(DEBUG):
            print(self.selected_file)

    def debug(self, widget):
        if(DEBUG):
            print("Selected file is %s" % self.selected_file)

    def destroy(self, widget):
        gtk.main_quit()

    def destroy_connect(self, function):
        self.file_widget.connect("destroy", function)

    def __init__(self, parent=None):
        # this variable contains the selected file initilaizing to None
        self.selected_file = None

        # creating a file selction widget.
        self.file_widget = gtk.FileSelection("Select a file")

        # connecting debug to destroy
        self.file_widget.connect("destroy", self.debug)

        # setting parent if any
        if (parent is not None):
            self.file_widget.set_transient_for(parent)
        else:
            # connecting self.destroy to widget's destroy event which quits
            # program
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
        self.file_widget.show_all()


# info box for file properties
class FilePropViewer:
    def ok_button_handler(self, widget):
        if(DEBUG):
            print("Exiting message dialog")

    def debug(self, widget):
        if(DEBUG):
            print(self.data)

    def destroy(self, widget):
        gtk.main_quit()

    def __init__(self, filepath, parent=None):
        self.data = []
        self.filepath = filepath

        self.message = gtk.MessageDialog(parent=parent, flags=0,
                                         type=gtk.MESSAGE_INFO,
                                         buttons=gtk.BUTTONS_OK,
                                         message_format=None)

        # adding data for the dialog
        self.data.append("You selected : %s" % filepath)

        if(os.path.isfile(filepath)):
            self.data.append("Type: File")
        elif(os.path.isdir(filepath)):
            self.data.append("Type: Directory")

        self.data.append("Size : %s bytes" % os.path.getsize(filepath))

        self.data.append("Last Metadata change/ Creation time: %s" %
                         time.strftime('%Y-%m-%d %H:%M:%S',
                                       time.gmtime(os.path.getctime(filepath))))
        self.data.append("Last Modification: %s" %
                         time.strftime('%Y-%m-%d %H:%M:%S',
                                       time.gmtime(os.path.getmtime(filepath))))
        self.data.append("Last Access Time: %s" %
                         time.strftime('%Y-%m-%d %H:%M:%S',
                                       time.gmtime(os.path.getatime(filepath))))

        self.message.set_markup("\n".join(self.data))

        # connecting debug to destroy
        self.message.connect("destroy", self.debug)

        if parent is None:
            # connecting self.destroy to widget's destroy event which quits
            # program
            self.message.connect("destroy", self.destroy)

        # ok_button
        self.ok_button = self.message.action_area.get_children()[0]
        # connect the file_ok_handler function to ok_button click
        self.ok_button.connect("clicked", self.ok_button_handler)
        # connect destroy to ok_button next i.e exit after selecting file
        self.ok_button.connect_object("clicked", gtk.Widget.destroy,
                                      self.message)
        # show the info
        self.message.show_all()


class Application:
    def debug(self, widget):
        if(DEBUG):
            print("exiting application")

    def destroy(self, widget):
        gtk.main_quit()

    def view_prop_handler(self, widget):
        selected_file = self.file_selector.selected_file
        if(DEBUG):
            print("in prop handler, selected file:" + selected_file)
        if(selected_file is not None):
            # create a file prop dialog with selected file
            FilePropViewer(selected_file, self.window)

    def file_button_handler(self, widget):
        self.file_selector = FileSelector(self.window)
        self.file_selector.destroy_connect(self.view_prop_handler)

    def __init__(self, parent=None):
        # creating a file selction widget.
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("File Info")
        # add border
        self.window.set_border_width(50)

        # connecting debug to destroy
        self.window.connect("destroy", self.debug)

        # setting parent if any
        if (parent is not None):
            self.window.set_transient_for(parent)
        else:
            # connecting self.destroy to widget's destroy event which quits
            # program
            self.window.connect("destroy", self.destroy)

        # ok_button
        self.file_button = gtk.Button("Select a file")
        # quit_button
        self.quit_button = gtk.Button("Quit")

        # connect the file_ok_handler function to ok_button click
        self.file_button.connect("clicked", self.file_button_handler)

        # connect the quit button to destroy event
        self.quit_button.connect_object("clicked", gtk.Window.destroy,
                                        self.window)

        # create a horizontal box
        self.box1 = gtk.HBox(homogeneous=False, spacing=10)

        # add buttons to boxes
        # experiment with these operations
        self.box1.pack_start(child=self.file_button, expand=True, fill=True,
                             padding=10)
        self.box1.pack_start(child=self.quit_button, expand=True, fill=True,
                             padding=10)

        # add box to window
        self.window.add(self.box1)

        # show the file selector
        self.window.show_all()


def parse_args():
    parser = argparse.ArgumentParser(
        description="A simple file info GUI in PyGTK",
        prog="fileinfo",
        epilog="after starting, click on `select a file`\n."
        "Then Select file from the dialog.\n"
        "Click Ok, the info of the file will be displayed.\n"
        "Click Ok on the info box to close it.\n"
        "You can repeat it on multiple files.\n"
        "To stop running the program, click quit/ cross button")

    parser.add_argument('-d', '--debug', help="enable debug messages",
                        action="store_true", default=False)

    args = parser.parse_args()

    # if debug in args
    if(args.debug):
        global DEBUG
        DEBUG = True


def main():
    parse_args()
    Application()
    gtk.main()


if __name__ == "__main__":
    main()
