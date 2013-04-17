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


echo '###################################'
echo "plot $FILE u $COL $OPT"
head -n 4 $FILE
echo "..."
tail -n 4 $FILE
echo '###################################'
 gnuplot -persist  <<-TOEND
    reset
    set terminal wxt size 800,600
    plot "${FILE}" u $COL $OPT
  TOEND

exit 
