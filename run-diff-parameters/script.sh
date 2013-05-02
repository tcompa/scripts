#!/bin/bash

INPUTFILE=input.dat
SOURCE=program.c
PROGRAM=program.x

#compile the source code (in this case it's very simple)
gcc -Wall $SOURCE -o $PROGRAM

touch $INPUTFILE

#cycle on all the parameters
for ((alpha=1;alpha<=3;alpha++)); do
 for ((beta=1;beta<=3;beta++)); do

  #prepare the input file:
  rm $INPUTFILE
  echo "$alpha $beta" > $INPUTFILE
  echo "out-a$alpha-b$beta.dat" >> $INPUTFILE

  #run the program:
  ./$PROGRAM

  echo "alpha=$alpha, beta=$beta - done"

 done
done

rm $PROGRAM
