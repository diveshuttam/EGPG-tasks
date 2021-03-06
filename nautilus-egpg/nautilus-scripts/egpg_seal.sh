#!/usr/bin/env bash

# these variables are set by NAUTILUS. Giving them a short name
# though not using all these variables in this script, still naming for convinience
selected_files=$NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
selected_uris=$NAUTILUS_SCRIPT_SELECTED_URIS
current_uris=$NAUTILUS_SCRIPT_CURRENT_URI
geometry=$NAUTILUS_SCRIPT_WINDOW_GEOMETRY

# NOTE: export $EGPGDEBUG=TRUE for debug mode
# checking debug here
if [[ $EGPGDEBUG = "TRUE" ]]
then
  echo "selected files: $selected_files"
  echo "selected uris: $selected_uris"
  echo "current uris: $current_uris"
fi

for file in $selected_files
do
  if [[ -f $file ]]
  then
    if [[ $EGPGDEBUG = "TRUE" ]]
    then
      echo sealing file $file
    fi
    # should be a dialog or some thing for asking a recipient
    # currently i don't ask a recipient
    gnome-terminal "-x" egpg seal $file
  fi
done
