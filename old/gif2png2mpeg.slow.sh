#!/bin/bash


# This scripts takes all the gif files in the actual folder, converts the frames to some png files and creats a mpg video of these frames.
# The speed is renormalized by a factor newspeed


newspeed=0.5;

rm *mpg

for file in *.gif; do

mv "${file}" "${file/ /_}";

name=`echo "${file/.gif/}"`

convert $file frame%05d.png
convert frame%05d.png -background black -flatten +matte frame%05d.png
ffmpeg -r 25 -i frame%05d.png -vb 20M "$name".mpg -y
ffmpeg -i "$name".mpg -vf "setpts=(1/$newspeed)*PTS" -vb 20M "$name"_slow.mpg -y

rm *.png;

done;

