+ arguments.dat: each line includes one set of arguments for script_taking_long_time.py
+ script_taking_long_time.py: as the name says.. Note that each line of arguments.dat is passed as a single string, so one might have to split it into variables at the beginning (easy in python).
+ run_with_parallel.sh: run script_taking_long_time.py on all lines of arguments.dat, through GNU parallel (note that some recent version is probably needed, see https://www.gnu.org/software/parallel/parallel_tutorial.html#Prerequisites). Limit the number of simultaneous jobs with the option `-jobs N`.
+ run_detached.sh: loop over arguments and run all detached (note the `&`).
