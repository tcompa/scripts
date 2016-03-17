#!/bin/bash

SCRIPT=script2.py
OUTPUT=${SCRIPT}.cProfile
python -m cProfile -o $OUTPUT script2.py
runsnake $OUTPUT
