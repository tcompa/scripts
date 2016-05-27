#!/bin/bash

PROGRAM=script_taking_long_time.py

for i in {1..4}; do
    ./$PROGRAM $i &
done
