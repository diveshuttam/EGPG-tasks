#!/bin/bash

#Author Divesh Uttamchandani

#Problem: Towers of Hanoi
# Initial states
#    -     |         |         |
#   ---    |         |         |
#  -----   |         |         |
# -------  |         |         |
#-------------------------------
#| Tower A | Tower B | Tower C |
#| (full)  | (empty) | (empty) |

# move all disks from tower A to tower B using tower C such that
# 1. at no point of time a larger disk is on smaller disk.
# 2. you can only move one disk at a time
# 3. the towers follow the stack (fifo) property

# function parameters $1=disks $2=from_tower $3=to_tower $4=aux_tower
total_steps=0
function toh(){
  local disks=$1
  local from_tower=$2
  local to_tower=$3
  local aux_tower=$4
  if [ $disks -eq 1 ]
  then
    echo "move $from_tower to $to_tower"
    total_steps=$(($total_steps+1))
  else
    # recursively move first (disks - 1) disks to aux_tower
    # using to_tower as aux_tower
    toh $(($disks-1)) $from_tower $aux_tower $to_tower

    # move 1 disk for from_tower to to_tower
    echo "move $from_tower to $to_tower"
    total_steps=$(($total_steps+1))

    # move the disks-1 disks in aux_tower to to_tower 
    # using from_tower as aux_tower
    toh $(($disks-1)) $aux_tower $to_tower $from_tower
  fi
}

#initial_disks given by commandline argument
initial_disks=$1
if [ -z $initial_disks ]
then
  echo "please give the inital number of disks as argument"
  exit 1
fi

#check if the number of disks entered is valid
if [ $initial_disks -ge 1 ]
  then
  toh $initial_disks "A" "B" "C"
  echo "total steps taken $total_steps"
fi
