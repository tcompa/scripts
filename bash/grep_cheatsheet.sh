#!/bin/bash

# create temporary file
FILE='tmp_file_for_grep.txt'
echo -e "Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
\nsed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris\
\nnisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in\
\nreprehenderit in voluptate velit esse cillum dolore eu fugiat nulla\
\npariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa\
\nqui officia deserunt mollit anim id est laborum." > $FILE
echo
echo "created \`${FILE}\`"
echo

echo "[exclude word: -v]"
cat $FILE | grep -v Excepteur | grep -v ipsum | grep -v ut
echo

echo "[multiple options: -E 'option1|option2']"
grep -E 'Lorem|mollit' $FILE
echo

echo "[ignore case: -i]"
grep -i ut $FILE
echo

echo "[show line numbers: -n]"
grep -n ut $FILE
echo

rm -v $FILE
echo
