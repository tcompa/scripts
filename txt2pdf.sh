#!/bin/bash

USAGE='Usage: txt2pdf input.txt [output.pdf]'
if [ $# -ge 1 ]; then
    INPUT=$1
    if [ ! -f $INPUT ]; then
        echo "ERROR: $INPUT does not exist. Exit."
        exit
    fi
    if [ $# -eq 1 ]; then
        OUTPUT="${INPUT%%.*}.pdf"
    else
        if [ $# -eq 2 ]; then
            OUTPUT=$2
        else
            echo $USAGE
            exit
        fi
    fi
    echo "in $INPUT"
    echo "out $OUTPUT"
    if [ -f $OUTPUT ]; then
        read -p "WARNING: existing file $OUTPUT, owerwrite? "
        echo    # (optional) move to a new line
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            paps $INPUT | ps2pdf - $OUTPUT
        fi
    else
        paps $INPUT | ps2pdf - $OUTPUT
    fi
else
    echo $USAGE
    exit
fi

