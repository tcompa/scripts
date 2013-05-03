#!/bin/bash

NINPUT=$#

if [ $NINPUT -eq 1 ]
then
 FILE=$1
 COL="1:2"
 OPT='w lp'
elif [ $NINPUT -eq 3 ]
then
 FILE=$1
 COL="$2:$3"
 OPT='w lp'
elif [ $NINPUT -eq 0 ]
then
 FILE=fort.21
 COL="1:2"
 OPT='w lp'
elif [ $NINPUT -eq 4 ]
then
 FILE=$1
 COL="$2:$3:$4"
 OPT='w errorbars'
fi

FOLDER=`pwd`


echo '###################################'
echo "plot $FILE u $COL $OPT"
head -n 4 $FILE
echo "..."
tail -n 2 $FILE
echo '###################################'
 gnuplot -persist  <<-TOEND
    reset
    set title "[$FOLDER] plot $FILE u $COL $OPT"
    set terminal wxt size 700,500
    plot "${FILE}" u $COL $OPT
  TOEND

exit 
