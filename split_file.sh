#!/bin/bash

if [ ! -f "$1" ];then
    echo "******************************************************************"
    echo "ERROR, argument 1 wrong"
    echo "The correct way is:"
    echo "      split_file.sh filename startline endline (output file name)"
    echo "******************************************************************"
    exit 1
else
    FILENAME=$1
fi

if [ -z "$2" ];then
    echo "******************************************************************"
    echo "ERROR!"
    echo "The correct way is:"
    echo "      split_file.sh filename startline endline (output file name)"
    echo "******************************************************************"
    exit 1
else
    FROM=$2
fi

if [ -z "$3" ];then
    echo "******************************************************************"
    echo "ERROR!"
    echo "The correct way is:"
    echo "      split_file.sh filename startline endline (output file name)"
    echo "******************************************************************"
    exit 1
else
    TO=$3
fi

if [ -z "$4" ];then
  OUTPUT="$FILENAME.short.$FROM-$TO"
else
  OUTPUT=$4
fi

head $FILENAME -n $TO | tail -n $((TO-FROM+1))|less > $OUTPUT
exit 0

