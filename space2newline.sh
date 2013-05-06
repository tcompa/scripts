#!/bin/bash

#
# 2013-05-06,tc
# convert a one-line data file to a one-column one
# (i.e. replace any space or tab with a newline
#


FILE=$1
OUT=$FILE.col

if [ -e "$FILE" ]; then
  echo "File '$FILE' exists, good."
else
  echo "File '$FILE' doesn't exist. Quit."
  exit
fi


echo "Output file (as a column): '$OUT'"
sed -e 's/\s\+/\n/g' $FILE > $OUT



