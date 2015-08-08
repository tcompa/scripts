2013-05-02, tc

This is an example of a bash script used to run a program with different parameters.

The executable file (program.x) does the following
- it reads (from an input file) all the parameters 
- it reads (from an input file) the name of the output file
- it computes what is necessary
- it writes the output on the output file

The bash script (script.sh) does the following
- it compiles the program
- it cycles on a set of parameters and for each choice:
  + it prepares the input file
  + it runs program.x

In this way, after running script.sh there will be many different output file in the folder (each one corresponding to a certain choice of the input parameteres).

