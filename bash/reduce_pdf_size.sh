#!/bin/bash

# Check 1: number of arguments
if [ $# -eq 0 ]; then
    echo "[$0] ERROR: no arguments supplied."
    exit 1
fi
FILE=$1

# Check 2: FILE exists
if [ ! -f $FILE ]; then
    echo "ERROR: $FILE not found."
    exit 2
fi

# Check 3: FILE has a pdf extension
if ! [[ $FILE == *.pdf ]]; then
    echo "ERROR: $FILE is not a pdf file, is it?"
    exit 3
fi

# Check 4: OUTPUT file not already present
NAME=`basename $FILE ".pdf"`
OUTPUT=${NAME}_compressed.pdf
if [ -f $OUTPUT ]; then
    echo "ERROR: $OUTPUT already exists."
    exit 4
fi

# Actual conversion
# Compression options (http://www.ghostscript.com/doc/current/Ps2pdf.htm):
#-dPDFSETTINGS=configuration
#    Presets the "distiller parameters" to one of four predefined settings:
#        /screen selects low-resolution output similar to the Acrobat Distiller "Screen Optimized" setting.
#        /ebook selects medium-resolution output similar to the Acrobat Distiller "eBook" setting.
#        /printer selects output similar to the Acrobat Distiller "Print Optimized" setting.
#        /prepress selects output similar to Acrobat Distiller "Prepress Optimized" setting.
#        /default selects output intended to be useful across a wide variety of uses, possibly at the expense of a larger output file. 
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/default -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$OUTPUT $FILE
