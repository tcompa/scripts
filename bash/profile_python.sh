#!/bin/bash

# program: profile_python.sh
# created: 2016-03-17 -- 12 CET
# author: tc

display_help_and_exit() {
    echo
    echo "$(basename "$0") <script>.py <option>"
    echo "    Run <script>.py with cProfile flag, and show profiling output."
    echo "    Allowed <option> flags:"
    echo "        -r, --runsnake : use runsnake"
    echo "        -s, --snakeviz : use snakeviz"
    echo
    echo "$(basename "$0") [-h, --help]"
    echo "    Show this help text and exit."
    echo
    exit 1
}


# Read inputs
if [ "$#" -ne 2 ]; then
    display_help_and_exit
fi
SCRIPT=$1
VIZ=$2

# Preliminary checks on SCRIPT
if [ ! -f $SCRIPT ]; then
    echo "ERROR: $SCRIPT not found."
    exit 2
fi
if ! [[ $SCRIPT == *.py ]]; then
    echo "ERROR: $SCRIPT is not a python script, is it?"
    exit 3
fi

# Verify that VIZ has been set properly
if [[ $VIZ = "-r" || $VIZ == '--runsnake' ]]; then
    VIZ=runsnake
elif [[ $VIZ = "-s" || $VIZ == '--snakeviz' ]]; then
    VIZ=snakeviz
else
    display_help_and_exit
fi

# Sanity check
read -p "WARNING: I will now run $SCRIPT, are you OK with that?
Press [Enter] to confirm "

OUTPUT=${SCRIPT}.cProfile
python -m cProfile -o $OUTPUT $SCRIPT
$VIZ $OUTPUT
