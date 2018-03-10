#!/usr/bin/env bash

# these variables are set by NAUTILUS giving them a short name
# though not using the variables in this script still naming for future
selected_files=$NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
selected_uris=$NAUTILUS_SCRIPT_SELECTED_URIS
current_uris=$NAUTILUS_SCRIPT_CURRENT_URI
geometry=$NAUTILUS_SCRIPT_WINDOW_GEOMETRY

# NOTE: set global variable $EGPGDEBUG to TRUE for debug mode
# checking debug here
if [[ $EGPGDEBUG = "TRUE" ]]
then
  echo "selected files: $selected_files"
  echo "selected uris: $selected_uris"
  echo "current uris: $current_uris"
fi

for file in $selected_files
do
  if [[ -f $file && $file==*.signature ]]
  then
    if [[ $EGPGDEBUG = "TRUE" ]]
    then
      echo "verifying $file"
    fi
    gnome-terminal "-x" egpg verify $file
  fi
done
