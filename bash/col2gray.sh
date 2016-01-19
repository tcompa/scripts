#!/bin/bash

# program: col2gray.sh
# author: tc
# created: 2016-01-19 -- 12 CEST
# notes: converts a pdf into grayscale


INPUT=$1
if [ $# -eq 0 ] || ! test -f $1; then
    echo ERROR: no argument, or file missing.
    exit
fi
INPUT=$(basename "$INPUT")
EXTENSION="${INPUT##*.}"
if [ ! $EXTENSION = pdf ]; then
    echo ERROR: argument is not a pdf.
    exit
fi
BASE="${INPUT%.*}"
INPUT=${BASE}.pdf
OUTPUT=${BASE}_gray.pdf

echo
echo Creating $OUTPUT from $INPUT
echo
gs -sOutputFile=$OUTPUT -sDEVICE=pdfwrite -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray -dAutoRotatePages=/None -dCompatibilityLevel=1.4 -dNOPAUSE -dBATCH $INPUT
