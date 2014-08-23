#!/bin/bash
#
# This is just an example. It simply prints all passed parameters and sleeps
# 5 seconds.
#
# Any action tile (eg. any tile with no sub items) will trigger this script.
# The names of the pages and of the clicked tile will be passed as arguments.
# Use those to decide what to do.

echo "$*"
sleep 5
