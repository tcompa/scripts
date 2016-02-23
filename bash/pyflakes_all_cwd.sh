#!/bin/bash

# program: pyflakes_all_cwd.sh
# author: tc
# created: 2016-02-23
# notes: runs pyflakes on all .py files in the current working directory

for f in ./*py; do
    echo Now running: pyflakes $f
    pyflakes $f
    read -p "Press [Enter] key to continue"
    echo
done
