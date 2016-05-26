#!/bin/bash

# program: reduce_pdf_size.sh
# created: 2016-05-26 -- 16 CEST

# Choose compression level (http://www.ghostscript.com/doc/current/Ps2pdf.htm):
#     /screen selects low-resolution output similar to the Acrobat Distiller "Screen Optimized" setting.
#     /ebook selects medium-resolution output similar to the Acrobat Distiller "eBook" setting.
#     /printer selects output similar to the Acrobat Distiller "Print Optimized" setting.
#     /prepress selects output similar to Acrobat Distiller "Prepress Optimized" setting.
#     /default selects output intended to be useful across a wide variety of uses, possibly at the expense of a larger output file. 
COMPRESSIONLEVEL=default

FILE=$1
NAME=`basename $FILE ".pdf"`
OUTPUT=${NAME}_compressed.pdf

# Peliminary checks
if [ $# -eq 0 ]; then                # number of arguments should be one
    echo "[$0] ERROR: no arguments supplied."
    exit 1
elif [ ! -f $FILE ]; then            # FILE should exist
    echo "ERROR: $FILE not found."
    exit 2
elif ! [[ $FILE == *.pdf ]]; then    # FILE should be .pdf
    echo "ERROR: $FILE is not a pdf file, is it?"
    exit 3
elif [ -f $OUTPUT ]; then            # OUTPUT should not exist
    echo "ERROR: $OUTPUT already exists."
    exit 4
fi

# Actual conversion
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/$COMPRESSIONLEVEL -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$OUTPUT $FILE
