#!/bin/bash

PROGRAM=script_taking_long_time.py
ARGFILE=arguments.dat

cat $ARGFILE | parallel ./$PROGRAM {}
