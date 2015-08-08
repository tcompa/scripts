#!/bin/bash

nameout=video-1d-N075-VT006J

ffmpeg  -vf "setpts=(1/0.15)*PTS" -sameq -i plot-nx-%03d.png $nameout.mp4
#ffmpeg -i output.mp4 -vf "setpts=(1/0.25)*PTS" -pix_fmt rgb24 -s qcif -loop_output 0 output.gif

#ffmpeg -qscale 5 -r 20 -b 9600 -i plot-nx-%02d.png movie.mp4

#name=out
#newspeed=0.25;
#ffmpeg -r 25 -i plot-nx-%03d.png -vb 20M "$name".mpg -y
#ffmpeg -i "$name".mpg -vf "setpts=(1/$newspeed)*PTS" -vb 20M "$name"_slow.mpg -y

