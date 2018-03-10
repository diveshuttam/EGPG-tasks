#!/usr/bin/env python


# source https://www.ibm.com/developerworks/library/l-script-linux-desktop-2/
# experimenting for learnig nautilus scripting. No copyright/ licence info
# availible
# some comments have been added by me for future reference

import pygtk
import gtk
import os

pygtk.require('2.0')


def alert(msg):
    """Show a simple dialog with msg"""

    dialog = gtk.MessageDialog()
    dialog.set_markup(msg)
    dialog.run()

def main():
    # getting the environment variable set by nautilus for path
    selected = os.environ.get(key='NAUTILUS_SCRIPT_SELECTED_URIS', failobj='')

    # get current directory, fall back to os.chdir
    curdir = os.environ.get(key='NAUTILUS_SCRIPT_CURRENT_URI', failobj=os.curdir)

    if selected:
        targets = selected.splitlines()
    else:
        target = [curdir]

    # test
    alert("\n".join(["curdir:", curdir,"selected",selected]))


if __name__ == "__main__":
    main()
