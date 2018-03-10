### references
https://www.ibm.com/developerworks/library/l-script-linux-desktop-2/index.html

### note
this is just a representative solution for the problem, implemented for
learning working of nautilus scripts. Though the soultion works, it is far
from the ideal one.

### Install
- I have created a basic Makefile for installation purpose you may try `make install` . What Makefile basically does is
- make scripts executable(give executable permissions) 
`chmod +x egpg_*.sh`  
- copy these scripts(`egpg_*.sh`) to ~/.local/share/nautilus/scripts/  

### Run
- after installing, restart nautilus, the `scripts` option will be availble in the context menu (right click menu) of nautilus on selecting files. Choosing the respective script will run it for the selected files
- for these scripts to work, I am basically launching the commands within
a gnome-terminal instance so that egpg has a tty to take inputs like password etc. This is just a work arround as I really wanted to implement these in bash with ease, this limitation can easily be overcome if I use python using password dialogs.

### Issues
as this implementation is just for learning about the working of
nautilus scripts, these scripts are not yet powerful and contain many
issues. Major issues:
- `egpg_seal.sh` doesn't ask for the recepients in the seal script.
- launching a new terminal instance for each of the files and asking for
  passwords again and again. 

**caution: don't run these scripts on too many files at once, as it will launch that many terminal instances. couldn't think of a simple solution for this**

### requirements
- nautilus
- egpg
- gnome-terminal


