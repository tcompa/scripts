#!/bin/bash

DELAY=10
# DELAY=100 <-> 1 frame per second, I think. See http://www.imagemagick.org/script/command-line-options.php#delay
OUTPUT=animation.gif

convert -delay $DELAY -dispose Background +page snap*.png -loop 0 $OUTPUT
