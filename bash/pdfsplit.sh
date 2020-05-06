#!/bin/bash

echo ""
echo "pdfsplit.sh, custom script based on https://askubuntu.com/a/1091721"
echo "Note: on my laptop it takes around 50 second to split a 13-pages doc"
echo ""

if [ -z "$1" ]; then
    echo "ERROR: No argument (input pdf file) supplied."
    echo ""
    exit
fi


DIR=/tmp/raw_for_pdfsplit
mkdir -p ${DIR}

INPUT=$1
OUTPUT=output-pdfsplit.pdf

convert -density 300 ${INPUT} page_%04d.png
mv page_*.png ${DIR}
echo "Step 1/4 complete (convert command)"

for file in ${DIR}/page_*.png; do
  convert "$file" -crop 100%x50% +repage "$file-split.png"
done
echo "Step 2/4 complete (crop command)"

ls ${DIR}/page_*-split-*.png | cat -n | while read n f; do mv "$f" $(printf "${DIR}/tmp_%04d.png" $n); done
echo "Step 3/4 complete (rename)"

convert `ls ${DIR}/tmp_[0-9][0-9][0-9][0-9].png` ${OUTPUT}
echo "Step 4/4 complete (put back into a single pdf)"

echo "The end."
